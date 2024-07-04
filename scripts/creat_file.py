import os
from datetime import datetime, timedelta

front_matter = """---
title: "{title}"
date: {date}
---

"""


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


def require_name():
    print("§ Enter a post name > ", end = "")
    name = input().replace("_", " ")

    return name


def require_date():
    print("§ Enter a post date (default: today) > ", end = "")
    date = input()

    if len(date) > 0:
        parse_date(date)
        return date

    posts = os.listdir("./pending")
    dates = [post.split(";")[0] for post in posts if ";" in post]
    dates.sort()

    last_date = "0000-00-00" if len(dates) == 0 else dates[-1]

    if last_date == "0000-00-00":
        current_date = datetime.now().strftime("%Y-%m-%d")
    else:
        current_date = parse_date(last_date) + timedelta(days=1)
        current_date = current_date.strftime("%Y-%m-%d")
    
    return current_date


if __name__ == "__main__":
    name = require_name()
    date = require_date()
    
    file_name = f"{date};{name}.md"

    header = front_matter.format(title=name, date=date)
    content = f"""# {name}

## {name}

## References

1. """
    
    with open(f"pending/{file_name}", "w", encoding="utf-8") as f:
        f.write(header + content)
    