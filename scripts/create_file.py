import os
from datetime import datetime, timedelta

front_matter = """---
title: "{title}"
date: {date}
draft: true
---

"""


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        quit("Invalid date format")
    

def require_name():
    print("§ Enter a post name > ", end = "")
    name = input().replace("_", " ")

    if len(name) == 0:
        quit("Name is essential")

    return name


def require_date():
    print("§ Enter a post date (default: today) > ", end = "")
    date = input()

    if len(date) > 0:
        parse_date(date)
        return date
    
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    name = require_name()
    date = require_date()
    print("§ Enter a subject name > ", end = "")
    subject = input()

    print("§ Enter a sub-subject name (blank: quit) > ", end = "")
    sub_subject = input()

    if subject == "" or sub_subject == "":
        quit("Subject must be essential")

    dest_dir = f"content/{subject}/{sub_subject}"
    if not os.path.isdir(dest_dir):
        quit("No such folder")
    
    file_name = f"{name}.md"

    header = front_matter.format(title=name, date=date)
    content = f"""# {name}

## {name}

## References

1. """
    
    with open(f"{dest_dir}/{file_name}", "w", encoding="utf-8") as f:
        f.write(header + content)
    