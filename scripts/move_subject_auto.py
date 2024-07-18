import os
import shutil

def blank_cnt(s):
    return len(s) - len(s.lstrip())

def parse_dest(s):
    return s.split("-")[1].strip()

def parse_date(s):
    import re

    match = re.search(r'/([^/]+)\)$', s)
    return match.group(1) if match else None


if __name__ == "__main__":
    with open("pending/previous.md", "r") as f:
        lines = f.readlines()
        
        dest_1 = ""
        dest_2 = ""
        date = ""
        
        for l in lines:
            if len(l) == 0:
                continue
            
            bc = blank_cnt(l)
            if bc == 0:
                dest_1 = parse_dest(l)
            elif bc == 2:
                dest_2 = parse_dest(l)
            elif bc == 4:
                date = parse_date(l)
                if date is None:
                    raise ValueError("Invalid Format")
                
                dest_dir = f"content/{dest_1}/{dest_2}"
                if not os.path.isdir(dest_dir):
                    raise ValueError(f"No Folder {dest_dir}")
                
                src_fn = f"content/post/{date}"
                if not os.path.isfile(src_fn):
                    continue
                
                shutil.move(src_fn, f"{dest_dir}/{date}")
                print(f"{date} moved")
                
            else:
                raise ValueError("Invalid Indent")
            
    print("DONE")
