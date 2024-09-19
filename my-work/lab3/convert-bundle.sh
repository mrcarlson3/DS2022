#!/bin/bash

#fetch tarball
curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz 

#unzip tarball
tar -xvzf lab3-bundle.tar.gz

#remove spaces
awk '!/^[[:space:]]*$/' lab3_data.tsv

#store as csv
sed 's/'$'\t''/,/g' lab3_data.tsv > lab3_data.csv 

#count number of lines and store it

count=$(tail -n +2 lab3_data.csv | wc -l)
echo "The number of data lines is $count"

tar -czvf converted-archive.tar.gz lab3_data.csv

