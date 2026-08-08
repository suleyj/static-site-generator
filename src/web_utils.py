import os
from md_to_html import markdown_to_html_node
from build_listing import extract_title, extract_date, format_date

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    md_file = open(from_path)
    md = md_file.read()

    template_file = open(template_path)
    template = template_file.read()

    html_node = markdown_to_html_node(md)
    html = html_node.to_html()

    title = extract_title(md)

    template = template.replace("{{title}}", title)
    template = template.replace("{{content}}", html)
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')

    try:
        date = extract_date(md)
        formatted_date = format_date(date)
        template = template.replace(date, formatted_date)
    except Exception:
        pass

    dest_path_name = os.path.dirname(dest_path)
    os.makedirs(dest_path_name, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_page_revursive(from_path, template_path, dest_path, base_path):
    ls = os.listdir(from_path)

    for item in ls:
        item_path = os.path.join(from_path, item)
        item_dest_path = item_path.replace(from_path, dest_path)
        if os.path.isfile(item_path):
            item_dest_path = item_dest_path.replace("md", "html")
            generate_page(item_path, template_path, item_dest_path, base_path)
        else:
            generate_page_revursive(item_path, template_path, item_dest_path, base_path)
