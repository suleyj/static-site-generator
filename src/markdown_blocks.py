from enum import Enum

from utils import markdown_to_blocks, text_node_to_html_node, text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    if is_heading_block(block):
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unordered_list_block(block):
        return BlockType.ULIST
    if is_ordered_list_block(block):
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def is_heading_block(block):
    # Count leading '#' characters
    hash_count = 0
    for character in block:
        if character == "#":
            hash_count += 1
        else:
            break

    # Markdown allows headings from hash_count 1 to 6
    if hash_count < 1 or hash_count > 6:
        return False

    # The '#' characters must be followed by a space
    if len(block) <= hash_count:
        return False

    if block[hash_count] != " ":
        return False

    return True

def is_code_block(block):
    start_tick_count = 0
    end_tick_count = 0

    # count leading and trailing ticks
    for character in block:
        if character == '`':
            start_tick_count+=1
        else:
            break

    for character in reversed(block):
        if character == '`':
            end_tick_count+=1
        else:
            break

    # markdown code block must have 3 ticks at start and end
    if start_tick_count != 3 or end_tick_count != 3:
        return False

    # Must have at least one character after opening ticks
    if len(block) <= start_tick_count:
        return False

    # Must be followed by a newline
    if block[start_tick_count] != "\n":
        return False

    return True

def is_quote_block(block):
    lines = block.split('\n')
    
    for line in lines:
        if not line:
            return False
        if line[0] != '>':
            return False

    return True

def is_unordered_list_block(block):
    lines = block.split('\n')

    for line in lines:
        if not line:
            return False
        if line[0] != '-' or line[1] != ' ':
            return False
        
    return True

def is_ordered_list_block(block):
    lines = block.split('\n')
    
    num = 1
    for line in lines:
        if not line:
            return False
        if line[0].isdigit() and int(line[0]) != num:
            return False
        if line[1] != '.':
            return False
        num+=1

    return True
