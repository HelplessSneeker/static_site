import os
import shutil
import sys

from src.generate_page import generate_pages_recursive


def main():
    base_path = sys.argv[1]
    generate_public_folder(base_path)


def generate_public_folder(base_path="/"):
    if os.path.exists("docs"):
        shutil.rmtree("docs/")
    os.mkdir("docs")

    copy_files("static/", "docs/")

    generate_pages_recursive("content/", "template.html", "docs/", base_path)


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
