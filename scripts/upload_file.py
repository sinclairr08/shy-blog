from datetime import datetime
import shutil
import os


if __name__ == "__main__":
    current_date = datetime.now().strftime("%Y-%m-%d")

    posts = os.listdir("./pending")
    dates = [post.split(";")[0] for post in posts if ";" in post]

    cnt = dates.count(current_date)

    if cnt == 0:
        raise Exception("No file for upload today")
    
    if cnt > 1:
        raise Exception("Check the duplicate date or newline at file name")
    
    for post in posts:
        if current_date in post:
            current_post = post
            break
    
    splitted = current_post.replace(";", ".").split(".")
    renamed_post = ".".join([splitted[0], splitted[2]])
    shutil.move(f"./pending/{current_post}", f"./content/post/{renamed_post}")
