import xml.etree.ElementTree as ET


def xml_parse(file_byte):

    def get_recursive(parent):
        res = {}
        if not parent.getchildren():
            res[parent.tag] = ''
            return res
        res[parent.tag] = []
        for child in parent:
            if child.getchildren():
                res[parent.tag].append(get_recursive(child))
            else:
                res[parent.tag].append({child.tag: child.text})
        return res

    root = ET.fromstring(file_byte)
    return get_recursive(root)
