#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
        This will take a Python dictionary and a filename as parameters.
        It should serialize the dictionary into XML
        and save it to the given filename.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
        This will take a filename as a parameter.
        It should read the XML file and return a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
