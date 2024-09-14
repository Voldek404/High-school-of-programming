import xml.etree.ElementTree as ETree


def remove_nodes_by_tag(root, tag):
    for element in list(root):
        if element.tag == tag:
            root.remove(element)
        else:
            remove_nodes_by_tag(element, tag)
    if root.tag == tag:
        root.clear()


xml1 = ETree.parse('demo.xml')
root = xml1.getroot()
remove_nodes_by_tag(root, 'data')
ETree.dump(root)
