#!/bin/bash

# I accidentally appended .bak.bak
# It was easier to just make another script to fix it
for file in *.bak; do
  mv "$file" "${file%.bak.bak}.bak"
done
