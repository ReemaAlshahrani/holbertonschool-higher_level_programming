#!/usr/bin/env python3
"""
Module for serializing and deserializing Python dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through dictionary items and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Wrap the root element into an ElementTree and write to file
    tree = ET.ElementTree(root)
    # Using utf-8 encoding and adding XML declaration
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Parses an XML file and reconstructs it back into a Python dictionary.
    Returns None or empty dict if an error occurs.
    """
    try:
        # Parse the XML file to get the tree structure
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary by iterating over child elements
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except (FileNotFoundError, ET.ParseError):
        return None
