#! /bin/bash

sql_docs_path="/home/goksel/Documents/DataWarehousing/SQL"
host="46.101.167.19"
port="5432"

echo "    *Creating the Database"
createdb -h $host -U postgres -p $port datawarehouse
echo ; echo "    *Creating the Table"

psql -h $host -U postgres -p $port datawarehouse < $sql_docs_path/create_table_whole_data.sql
echo ; echo
