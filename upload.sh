#!/bin/bash

TODAY="$(date "+%Y-%m-%d")"
SOURCE_PATH=./pending
DEST_PATH=./contents/${TODAY:0:7}
FILENAME=$(ls $SOURCE_PATH | grep "$TODAY")

if [ -z "$FILENAME" ]
then
    echo "No file for upload today"
    exit 1
elif [[ $FILENAME == *$'\n'* ]]
then
    echo -e "FILENAME: $FILENAME\nPlease check the duplicate date or file name"
    exit 2
fi

TITLE="${FILENAME:11:-3}"

if [ ! -d $DEST_PATH ]
then
    mkdir $DEST_PATH
fi

mv "$SOURCE_PATH/$FILENAME" "$DEST_PATH/$TODAY.md"

echo "- [$TITLE]($DEST_PATH/$TODAY.md)" >> ./README.md
