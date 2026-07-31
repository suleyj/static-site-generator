import os
import shutil
import  sys
from web_utils import generate_page_revursive

def copy_tree(source_path, destination_path):
    if not os.path.isdir(source_path):
        return
    ls = os.listdir(source_path) 
    
    for item in ls:
        item_path = os.path.join(source_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination_path)
        else:
            new_path = os.path.join(destination_path, item)
            os.mkdir(new_path)
            copy_tree(item_path, new_path)


def print_tree(path):
    ls = os.listdir(path) 

    for item in ls:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print(item_path)
        else:
            print_tree(item_path)


def main():
    static_path = 'static'  
    build_path = 'docs'  
    content_path = "content"
    template_path = "template.html"
    base_path = "/"

    if os.path.exists(build_path) :
        shutil.rmtree(build_path) 

    os.mkdir(build_path)
    copy_tree(static_path, build_path)

    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    generate_page_revursive(content_path, template_path, build_path, base_path)
    
    

if __name__ == "__main__":
    main()
