import os

front_matter = """---
title: "{title}"
date: {date}
---

"""

directory = "./content/post"
cnt = 0

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        file_path = os.path.join(directory, filename)
        date = filename.split(".md")[0]
        
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if content.strip().startswith("---"):
            print(f"File {filename} already has front matter. Skipping.")
            continue

        title = content.split("\n")[0].replace("# ", "")
       
        new_content = front_matter.format(title=title, date=date) + content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"{date} changed")
        cnt += 1

print(f"{cnt} files are changed")
