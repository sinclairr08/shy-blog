#!/usr/bin/env bash

if [ -z "$1" ]
then
    echo -n "§ Enter a subject name > "
    read NAME
else
    NAME="$1"
fi

echo -e "# $NAME\n" > "subjects/$NAME.md"
echo "$NAME.md was created"
