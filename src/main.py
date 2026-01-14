import os
import shutil

from src.generate_page import generate_pages_recursive


def main():
    generate_public_folder()


def generate_public_folder():
    if os.path.exists("public"):
        shutil.rmtree("public/")
    os.mkdir("public")

    copy_files("static/", "public/")

    generate_pages_recursive("content/", "template.html", "public/")


def copy_files(path, dest):
    print(f"working on path: {path}")
    if os.path.isfile(path):
        print(f"coping file {path}")
        shutil.copy(path, dest)
    else:
        dir_content = os.listdir(path)
        for dir in dir_content:
            cp_path = os.path.join(path, dir)
            print(f"listing file {dir}")
            dest_path = os.path.join(dest, dir)
            if os.path.isdir(cp_path):
                print(f"creating dir: {dest_path}")
                os.mkdir(dest_path)
            copy_files(cp_path, dest_path)


main()
