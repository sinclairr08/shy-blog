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


def add_sub_subject(subject, sub_subject, sub_subject_ko, index_fn):
    line = f"- [{sub_subject_ko}](/{subject}/{sub_subject})\n"
    
    with open(index_fn, 'a', encoding='utf-8') as file:
        file.write(line)



if __name__ == "__main__":
    print("§ Enter a subject name > ", end = "")
    subject = input()
    create_subject(subject, f"content/{subject}", depth = 1)
    
    print("§ Enter a sub-subject name (blank: quit) > ", end = "")
    sub_subject = input()

    if sub_subject == "":
        quit()

    print("§ Enter a sub-subject name in korean > ", end = "")
    sub_subject_ko = input()

    create_subject(sub_subject, f"content/{subject}/{sub_subject}", depth = 2)    
    add_sub_subject(subject, sub_subject, sub_subject_ko, f"content/{subject}/_index.md")
