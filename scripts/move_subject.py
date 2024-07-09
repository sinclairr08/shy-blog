import shutil
import os

if __name__ == "__main__":
    dest_1 = input("§ Enter subject depth 1 > ")
    dest_2 = input("§ Enter subject depth 2 > ")
    
    if dest_1 == "" or dest_2 == "":
        quit("Blank path")
    
    dest_dir = f"content/{dest_1}/{dest_2}"
    if not os.path.isdir(dest_dir):
        quit("No such folder")

    date = input("§ Enter date > ")
    src_fn = f"content/post/{date}.md"
    
    if not os.path.isfile(src_fn):
        quit("No such file")
    
    shutil.move(src_fn, f"{dest_dir}/{date}.md")


