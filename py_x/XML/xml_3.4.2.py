import xml.etree.ElementTree as ETree


def root_count_helper(root, count: int):
    if "name" in root.attrib.keys():
        count += 1
    for element in root:
        count = root_count_helper(element, count)
    return count


def root_count(root):
    return root_count_helper(root, 0)


xml1 = ETree.parse('demo.xml')
root = xml1.getroot()
