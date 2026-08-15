# Python - Server-Side Rendering (SSR)

This project explores Server-Side Rendering (SSR) techniques using Python and the Flask framework, along with Jinja templating, reading data from various formats (JSON, CSV), and interacting with SQLite databases.

## Project Structure & Tasks

| Task File / Script | Description |
| :--- | :--- |
| **`task_00_intro.py`** | A Python script that implements a simple templating function to generate personalized invitation files dynamically from a template and a list of attendees, including input validation and error handling. |
| **`task_01_jinja.py`** | A basic Flask application featuring multiple routes (`/`, `/about`, `/contact`) and reusable Jinja components (header and footer includes). |
| **`task_02_logic.py`** | An enhanced Flask application that reads a list of items from a JSON file and renders them dynamically using Jinja loops and conditional statements (`/items`). |
| **`task_03_files.py`** | A Flask route (`/products`) that parses and displays product data from either JSON or CSV files based on query parameters, supporting optional ID filtering and error handling. |
| **`task_04_db.py`** | An extension of the Flask application adding SQLite database support (`/products?source=sql`), alongside JSON and CSV sources, with full query parameter handling and error responses. |

## Requirements
* Python 3.x
* Flask
* Jinja2
