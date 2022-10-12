#! /bin/bash

path_orig=$(pwd)
python_docs_path="Python"
shell_docs_path="Shell"

cd $python_docs_path

echo "    *Data ingestion from multiple sources... (API), (Web Scraping)"; echo "..."
python main.py
echo "Data is ready!"

cd $path_orig; cd $shell_docs_path

echo "    *Connecting to server..."
./local_to_server.sh
echo "    *All csv files are uploaded to server"; echo
 
./etl.sh
 
 

