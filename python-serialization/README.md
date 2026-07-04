# Python - Serialization

This repository explores the core computer science concepts of **Serialization** and **Marshaling**. Through these tasks, we practice converting complex in-memory Python data structures and objects into persistent or transmittable formats (JSON, Pickle, CSV, XML) and reconstructing them back.

## Learning Objectives
* Understand the explicit differences and similarities between serialization and marshaling.
* Persist object states using Python's built-in libraries.
* Evaluate efficiency, safety, and performance trade-offs between text-based (JSON, XML) and binary (Pickle) serialization formats.
* Implement robust error-handling when deserializing potentially corrupt or missing files.

## Environment & Requirements
* **OS:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** Code conforms to the `pycodestyle` guidelines.

---

## Project Structure and Tasks

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Basic Serialization** | `task_00_basic_serialization.py` | Serializes a Python dictionary to a JSON file and deserializes it back using the `json` module. |
| **1. Pickling Custom Classes** | `task_01_pickle.py` | Serializes and deserializes custom object instances using the binary `pickle` module with comprehensive exception handling. |
| **2. Converting CSV Data to JSON** | `task_02_csv.py` | Reads structural data from a comma-separated values (`.csv`) file via `DictReader` and exports it into a JSON array format. |
| **3. Serializing/Deserializing with XML** | `task_03_xml.py` | Implements data serialization using hierarchal tree objects with the `xml.etree.ElementTree` module. |

---

