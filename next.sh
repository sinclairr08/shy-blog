#!/bin/bash

if [ -z "$1" ]
then
    echo "File is not made. Please enter a title"
    exit 1
fi

FILENAME=$(ls ./pending | grep '\;' | tail -n 1)

if [ -z "$FILENAME" ]
then
    LAST_DAY=$(date "+%Y-%m-%d")
else
    LAST_DAY="${FILENAME:0:10}"
fi

NEXT_DAY=$(date -d "$LAST_DAY next day" "+%Y-%m-%d")

./new.sh $1 $NEXT_DAY