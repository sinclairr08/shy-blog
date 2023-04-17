#!/usr/bin/env bash

# 1. 파일 이름 입력 받기
echo -n "§ Enter a post name > "
read NAME_

while [ -z "$NAME_" ]
do
    echo "Please enter a valid post name"
    read NAME_
done

# 2. 입력 받은 파일 이름의 언더바를 공백으로 치환
NAME=$(echo $NAME_ | tr '_' ' ')

# 3. 날짜 입력받기
echo -n "§ Enter a post date (default: today) > "
read DATE

if [ -z "$DATE" ]
then
    # 3-1. 날짜를 입력받지 않은 경우
    LAST_NAME=$(ls ./pending | grep '\;' | tail -n 1)
    if [ -z "$LAST_NAME" ] || [ "${LAST_NAME:0:10}" == "0000-00-00" ]; then
        # 3-1-1. 만약 포스트가 없다면 오늘 날짜의 포스트를 만듦
        DATE=$(date "+%Y-%m-%d")
    else
        # 3-1-2. 만약 포스트가 있다면 그 다음 날의 포스트를 만듦
        LAST_DATE="${LAST_NAME:0:10}"
        DATE=$(date -d "$LAST_DATE next day" "+%Y-%m-%d")
    fi
fi

# 4. 주제 입력받기
echo -n "§ Enter a post subject (default: Else) > "
read SUBJECT

if [ -z "$SUBJECT" ]
then
    # 4-1. 주제가 없는 경우 Else로 설정
    SUBJECT="Else"
elif [ -z "$(ls ./subjects | grep "$SUBJECT")" ]
then
    # 4-2. 주제가 있지만 Subject 폴더에 없는 경우 새로운 주제를 생성할지 물어봄
    echo "$SUBJECT.md is not exist. Do you want to make a new subject?"
    echo -n "(Y / N): "
    read IS_MAKE_SUBJECT

    if [ $IS_MAKE_SUBJECT == "Y" ]
    then
        # 4-2-1. 주제를 생성하기로 한 경우
        ./scripts/new_subject.sh $SUBJECT
    else
        # 4-2-2. 주제를 생성하지 않기로 한 경우 exit
        exit 1
    fi
fi

# 5. 기본 포맷을 이용해 포스트를 pending 폴더에 생성
CONTENTS="# $NAME\n\n## $NAME\n\n## References\n\n1. "
PATH=./pending
FILE_NAME=$DATE\;$SUBJECT\;$NAME.md

echo -e $CONTENTS > "$PATH/$FILE_NAME"
echo "$FILE_NAME was created"
