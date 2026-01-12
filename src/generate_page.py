from src.extraction import extract_title
from src.markdown_to_html import markdown_to_html_node


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
