#! /bin/bash

path_orig=$(pwd)
destination="data_from_server"
python_docs_path="/home/goksel/Documents/DataWarehousing/Python"
shell_docs_path="/home/goksel/Documents/DataWarehousing/Shell"
sql_docs_path="/home/goksel/Documents/DataWarehousing/SQL"

host="46.101.167.19"
port="5432"

extract(){
    print_line
    info_ "EXTRACT PHASE STARTED"
    cd $destination; sftp root@$host:*.csv; cd $path_orig
    echo; echo "    Data Extracted from the Server"; info_ "EXTRACT PHASE ENDED"; print_line
}

transform(){
    info_ "TRANSFORM PHASE STARTED"
    cd $python_docs_path; python transform.py; cd $path_orig
    echo "    Extracted data Transformed"; info_ "TRANSFORM PHASE ENDED"; print_line
}

load(){
    info_ "LOAD PHASE STARTED"
    import_csv_to_dbtable datawarehouse data $sql_docs_path/data/transformed_data.csv
    echo "    Transformed data loaded to Database in the Server"; info_ "LOAD PHASE ENDED"; print_line
}


import_csv_to_dbtable(){
    local db_name="$1"
    local table_name="$2"
    local data_path="$3"
    psql -h $host -U postgres -p $port "$db_name" -c "\copy $table_name from $data_path delimiter ',' csv header;"
}

create_star_schema(){
    echo "    *Creating the schema*"; echo
    psql -h $host -U postgres -p $port datawarehouse < $sql_docs_path/star_schema.sql
    echo ; print_line
}


verify_database(){
    echo "    *Verifying the database*"; echo
    psql -h $host -U postgres -p $port datawarehouse < $sql_docs_path/verify.sql
    print_line
}

print_line(){
    echo ; echo "#######################################################################"; echo
}

info_(){
    local message="$1"
    echo ; echo "****$1****"; echo
}


run(){
    ./create_db.sh
    extract; transform; load
    create_star_schema 
    verify_database
}

run







