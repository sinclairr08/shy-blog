import os
from datetime import datetime, timedelta

DEFAULT_HEADER = """---
title: "{title}"
date: {date}
draft: true
---

"""

DEFATULT_CONTENT = """# {name}

## {name}

## References

1. """


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        quit("Invalid date format")


def require_name():
    print("§ Enter a post name > ", end="")
    name = input().replace("_", " ")

    if len(name) == 0:
        quit("Name is essential")

    return name


def require_date():
    print("§ Enter a post date (default: today) > ", end="")
    date = input()

    if len(date) > 0:
        parse_date(date)
        return date

    return datetime.now().strftime("%Y-%m-%d")


def require_subject():
    print("§ Enter a subject1 > ", end="")
    subject1 = input()
    if subject1 == "":
        quit("Subject 1 is essential")

    print("§ Enter a subject2 > ", end="")
    subject2 = input()

    if subject2 == "":
        quit("Subject 2 is essential")

    return subject1, subject2


if __name__ == "__main__":
    name = require_name()
    date = require_date()
    subject1, subject2 = require_subject()

    dest_dir = f"content/{subject1}/{subject2}"
    if not os.path.isdir(dest_dir):
        quit("No such folder")

    file_name = f"{name}.md"

    header = DEFAULT_HEADER.format(title=name, date=date)
    content = DEFATULT_CONTENT.format(name=name)

    with open(f"{dest_dir}/{file_name}", "w", encoding="utf-8") as f:
        f.write(header + content)
