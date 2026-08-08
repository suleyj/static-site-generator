import re
import os
from datetime import datetime
from dateutil import parser

def extract_title(markdown):
    for line in markdown.splitlines():
        stripped = line.strip()
        parts = stripped.split(" ", 1)
        if len(parts) == 2 and parts[0] == "#":
            return parts[1].strip()
    raise Exception("no h1 in markdown")

def extract_date(markdown):
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", markdown)

    if date_match is None:
        raise Exception("no date found")

    date = date_match.group()
    return date

def format_date(date_str):
    date_obj = parser.parse(date_str)
    return date_obj.strftime("%b %d %Y")


    
# extract title and date from md func
def get_blog_list_item(md):
    title = extract_title(md)
    date = format_date(extract_date(md))
    return title, date

# crete blog_list dictionary from path 
def get_blog_list_arr(blogs_path):
    ls = os.listdir(blogs_path)
    blog_list = []
    for item in ls:
        item_path = os.path.join(blogs_path, item)
        if os.path.isfile(item_path):
            with open(item_path) as f:
                md = f.read()
            link = os.path.basename(os.path.dirname(item_path))
            title, date = get_blog_list_item(md)
            blog_list.append((title, date, link))
        else:
            blog_list.extend(get_blog_list_arr(item_path)) 
    return blog_list

def sort_blog_list_arr(blog_list):
    blog_list.sort(key=lambda x: datetime.strptime(x[1], '%b %d %Y'), reverse=True)
    return blog_list


# create blog-list-component with title and date
def get_post_component(title, date, link, component_path):
    component_file = open(component_path)
    component = component_file.read()
    
    #replace title and date
    component = component.replace("{{link}}", link)
    component = component.replace("{{title}}", title)

    # year from date
    component = component.replace("{{date}}", " ".join(date.split()[:-1]))

    return component

def get_year_component(year, posts, component_path):
    with open(component_path) as f:
        component = f.read()

    component = component.replace("{{year}}", year)
    component = component.replace("{{posts}}", posts)
    return component


def get_blog_list(blogs_path, year_component_path, post_component_path ):
    blogs_list_arr = get_blog_list_arr(blogs_path)

    blogs_by_year = {}

    blog_list = ""

    for item in blogs_list_arr:
        title, date, link = item
        post_component = get_post_component(title, date, link, post_component_path)
        year = datetime.strptime(date, '%b %d %Y').strftime('%Y')
        blogs_by_year.setdefault(year, []).append(post_component)

    for year, posts in blogs_by_year.items():
        year_component = get_year_component(year, "".join(posts), year_component_path)
        blog_list += year_component

    return blog_list

def create_blog_listing(index_file_path, template_path, blog_list):
    
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    template = template.replace("{{content}}", blog_list)

    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(template)


