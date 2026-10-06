#!/bin/bash

for file in *.bak; do
  mv "$file" "${file%.bak}.txt"
done
