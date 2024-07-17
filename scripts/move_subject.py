import shutil
import os

DEFAULT_1 = "algorithm"
DEFAULT_2 = "boj"

if __name__ == "__main__":
    dest_1 = input("§ Enter subject depth 1 > ")
    dest_2 = input("§ Enter subject depth 2 > ")

    if dest_1 == "":
        print(f"Substitute depth 1 to {DEFAULT_1}")
        dest_1 = DEFAULT_1
    
    if dest_2 == "":
        print(f"Substitute depth 2 to {DEFAULT_2}")
        dest_2 = DEFAULT_2
    
    dest_dir = f"content/{dest_1}/{dest_2}"
    if not os.path.isdir(dest_dir):
        quit("No such folder")

    date = input("§ Enter date > ")
    src_fn = f"content/post/{date}.md"
    
    if not os.path.isfile(src_fn):
        quit("No such file")
    
    shutil.move(src_fn, f"{dest_dir}/{date}.md")


