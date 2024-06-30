#!/usr/bin/env bash

echo "Select what to do"
echo "(U) Upload a post | (C) Create a post | (S) Create a Subject | (Else) Exit"
read JOB

if [ "$JOB" = "U" ]
then
    ./scripts/upload.sh
elif [ "$JOB" = "C" ]
then
    ./scripts/new.sh
elif [ "$JOB" = "S" ]
then
    ./scripts/new_subject.sh
else
    echo "Exit"
    exit 0
fi
