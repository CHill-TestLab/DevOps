#!/bin/bash

# To create the x10 Files I used 'touch TextFile{1..10}.txt'

# Change all .txt files to .bak files in current directory
for file in *.txt; do
  mv "$file" "${file%.txt}.bak"
done
