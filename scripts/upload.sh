#!/usr/bin/env bash

TODAY="$(date "+%Y-%m-%d")"

SOURCE_PATH=./pending
DEST_PATH=./contents/${TODAY:0:7}
SUBJECT_PATH=./subjects

# 1. 업로드할 파일 이름을 찾음
FILE_NAME=$(ls $SOURCE_PATH | grep "$TODAY")

if [ -z "$FILE_NAME" ]
then
    # 1-1. 업로드할 파일 이름이 없는 경우 exit
    echo "No file for upload today"
    exit 1
elif [[ $FILE_NAME == *$'\n'* ]]
then
    # 1-2. 파일 이름에 newline이 들어간 경우 동일한 날짜의 여러 파일일 가능성이 있으므로 exit
    echo -e "Check the duplicate date or newline at file name"
    exit 2
fi

# 2. 파일 이름을 파싱해서 subject, name을 알아냄
IFS=";" read -r -a ARRAY <<< "$FILE_NAME"

SUBJECT="${ARRAY[1]}"
NAME="${ARRAY[2]::-3}"

# 3. Subject가 없는 경우 exit
if [ -z "$SUBJECT" ]
then
    echo "No subject... something went wrong"
    exit 1
fi

# 4. Subject에 해당하는 md 파일을 찾음
SUBJECT_FILE=$(ls $SUBJECT_PATH | grep "$SUBJECT")

# 4-1. Subject에 해당하는 md파일이 없을 경우 종료
if [ -z "$SUBJECT_FILE" ]
then
    echo "Subject name is something wrong"
    exit 1
fi

# 5. 업로드할 달의 폴더 경로가 없는 경우 생성
if [ ! -d $DEST_PATH ]
then
    mkdir $DEST_PATH
fi

# 6. 폴더 업로드
mv "$SOURCE_PATH/$FILE_NAME" "$DEST_PATH/$TODAY.md"

# 7. Subject에 해당하는 md 파일에 내용 업로드

echo "- [$NAME](${DEST_PATH:1}/$TODAY.md)" >> "./subjects/$SUBJECT_FILE"
echo "$NAME uploaded successfully"
