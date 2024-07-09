import os

def create_index_file(title, path, depth):
    content = f"""---
title: "{title}"
---
"""
    supplemental = f"""
# {title}
"""

    with open(path, 'w', encoding='utf-8') as file:
        if depth == 1:
            file.write(content + supplemental)
        else:
            file.write(content)


def create_subject(subject, path, depth):
    if os.path.isdir(path):
        if not os.path.isfile(f"{path}/_index.md"):
            print("_index.md does not exist. I will create this!")
            create_index_file(subject, f"{path}/_index.md", depth)
            
    else:
        print(f"{subject} does not exist. I will create this!")
        os.makedirs(f"{path}", exist_ok = True)
        create_index_file(subject, f"{path}/_index.md", depth)


if __name__ == "__main__":
    print("§ Enter a subject name > ", end = "")
    subject = input()
    create_subject(subject, f"content/{subject}", depth = 1)

    print("§ Do you want to make sub-subject? Enter anything > ", end = "")
    yn = input()

    if yn == "":
        quit()
    
    print("§ Enter a sub-subject name > ", end = "")
    sub_subject = input()

    create_subject(sub_subject, f"content/{subject}/{sub_subject}", depth = 2)    
