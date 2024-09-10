import xml.etree.ElementTree as ETree


def root_printing_helper(root, index: int):
    if index == len(root):
        return
    print(root[index].tag, root[index].text)
    if len(root[index]) > 0:
        for element in root[index]:
            print(element.attrib["name"], element.text)
    return root_printing_helper(root, index + 1)


def root_printing_index(root):
    return root_printing_helper(root, 0)


xml1 = ETree.parse('demo.xml')
root = xml1.getroot()
