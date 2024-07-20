import os

DEFAULT_INDEX_FILE = """---
title: "{title}"
---
"""
ADDITIONAL_INDEX_FILE = """
# {title}

"""


def create_index_file(title, path, depth):
    content = DEFAULT_INDEX_FILE.format(title=title)
    if depth == 1:
        content += ADDITIONAL_INDEX_FILE.format(title=title)

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def create_subject(subject, path, depth):
    if os.path.isdir(path):
        if not os.path.isfile(f"{path}/_index.md"):
            print("_index.md does not exist. I will create this!")
            create_index_file(subject, f"{path}/_index.md", depth)

    else:
        print(f"{subject} does not exist. I will create this!")
        os.makedirs(f"{path}", exist_ok=True)
        create_index_file(subject, f"{path}/_index.md", depth)


def add_to_index_file(subject, sub_subject, sub_subject_ko, index_fn):
    line = f"- [{sub_subject_ko}](/{subject}/{sub_subject})\n"

    with open(index_fn, "a", encoding="utf-8") as file:
        file.write(line)


def require_subject(depth):
    print(f"§ Enter a subject {depth} > ", end="")
    subject = input()
    if subject == "":
        quit("Subject is essential")

    return subject


if __name__ == "__main__":
    subject1 = require_subject(1)
    create_subject(subject1, f"content/{subject1}", depth=1)

    subject2 = require_subject(2)
    subjectk = require_subject("alias")

    create_subject(subject2, f"content/{subject1}/{subject2}", depth=2)
    add_to_index_file(subject1, subject2, subjectk, f"content/{subject1}/_index.md")
