from src.extraction import extract_title
from src.markdown_to_html import markdown_to_html_node
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"working on path: {dir_path_content}")
    if os.path.isfile(dir_path_content):
        generate_page(
            dir_path_content, template_path, dest_dir_path.replace("md", "html")
        )
    else:
        dir_content = os.listdir(dir_path_content)
        for dir in dir_content:
            cp_path = os.path.join(dir_path_content, dir)
            print(f"listing file {dir}")
            dest_path = os.path.join(dest_dir_path, dir)
            if os.path.isdir(cp_path):
                print(f"creating dir: {dest_path}")
                os.mkdir(dest_path)
            generate_pages_recursive(cp_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_string = ""
    template_string = ""
    with open(from_path, "r") as file:
        from_string = file.read()
    with open(template_path, "r") as file:
        template_string = file.read()

    html_string = markdown_to_html_node(from_string).to_html()
    title = extract_title(from_string)

    final_string = template_string.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_string
    )

    with open(dest_path, "w") as f:
        f.write(final_string)
