#! /bin/bash

python_docs_path="/home/goksel/Documents/DataWarehousing/Python/"
host="46.101.167.19"

sftp root@$host << ,
  put "$python_docs_path/data/customers.csv"
  put "$python_docs_path/data/cities.csv"
  put "$python_docs_path/data/products.csv"
  bye
,
 
