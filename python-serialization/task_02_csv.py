#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file named data.json.
    Returns True if successful, False if the file is not found or an error occurs.
    """
    try:
        # Open and read the CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # DictReader automatically maps rows into dictionaries using headers
            csv_reader = csv.DictReader(csv_file)
            # Convert the reader object into a standard Python list of dictionaries
            data_list = list(csv_reader)

        # Write the serialized list to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
