#!/bin/bash

echo "" > sentences

filename=$1
while read line; do
  # reading each line
  echo "Requesting sentence from word \"$line\":"
  sentence=$(python request-linguee.py "$line")
  echo "-> $sentence"
  echo $sentence >> sentences
  echo ""
done < $filename
