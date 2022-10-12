#! /bin/bash

sql_docs_path="/home/goksel/Documents/DataWarehousing/SQL"

host="46.101.167.19"
port="5432"


psql -h $host -U postgres -p $port postgres < $sql_docs_path/drop_db.sql
