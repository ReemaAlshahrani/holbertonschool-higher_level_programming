#!/usr/bin/env python3
"""
Module for basic serialization and deserialization using JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file back into a Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
