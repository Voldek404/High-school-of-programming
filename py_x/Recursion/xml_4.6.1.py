import xml.etree.ElementTree as ETree

def find_parent_of_name_tag(xml_file):
    xml1 = ETree.parse(xml_file)
    root = xml1.getroot()
    parent_map = {}
    def traverse(node):
        for child in node:
            parent_map[child] = node
            traverse(child)
    traverse(root)
    for key, value in parent_map.items():
        if 'pc_item' in key.tag:
            print(f"Родительский узел: {value.tag}")
            return value.tag
    return None
