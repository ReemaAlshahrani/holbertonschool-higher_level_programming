# Python - RESTful API

This project is part of the Higher-Level Programming curriculum. It covers the fundamentals of web communication, API consumption, server development, and API security using Python and lightweight frameworks.

## Technologies
* Python (Version 3.8.5)
* Flask (Framework for API development)
* Flask-HTTPAuth (For Basic Authentication)
* Flask-JWT-Extended (For Token-based Authentication)
* Style guide: `PEP 8`

## Files & Tasks Description

| File | Description |
| --- | --- |
| `No File (Task 0)` | Theoretical learning covering the basics of HTTP/HTTPS protocols, methods, and status codes. |
| `No File (Task 1)` | Command-line practice utilizing `curl` to fetch webpage content, API endpoints, and response headers. |
| `task_02_requests.py` | A script using the `requests` library to fetch posts from an external API, print titles, and export structured data into a `posts.csv` file. |
| `task_03_http_server.py` | A basic HTTP server built from scratch using Python's standard `http.server` module to handle specific routes and serve JSON data. |
| `task_04_flask.py` | A lightweight RESTful API built with Flask that supports GET requests for user tracking and POST requests to add new user objects dynamically. |
| `task_05_basic_security.py` | A secure Flask API integrating Basic HTTP Authentication, JWT token-based authentication, custom error handlers, and Role-Based Access Control. |

## How to Use
You can run the web server applications directly from the command line. For example, to start and interact with the Flask API containing security mechanisms (`task_05_basic_security.py`):

```bash
# Run the application
python3 task_05_basic_security.py

# In another terminal, test the login endpoint to receive a JWT token
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin1", "password":"password"}' http://localhost:5000/login
