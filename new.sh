#!/usr/bin/env bash

if [ -z "$1" ]
then
    echo "File is not made. Please enter a title"
    exit 1
fi

TITLE=$(echo $1 | tr '_' ' ')
echo $TITLE

if [ -z "$2" ]
then
    DATE="0000-00-00"
else
    DATE=$2
fi

CONTENTS="# $TITLE\n\n## $TITLE\n\n## References\n\n1. "
PATH=./pending
FILENAME=$DATE\;$TITLE.md

echo -e $CONTENTS > "$PATH/$FILENAME"
