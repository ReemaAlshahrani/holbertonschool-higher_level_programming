from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users in memory
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    # Returns a list of all usernames stored in the API
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    # Returns the full object corresponding to the provided username
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    # 1. Check if the request body is valid JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    
    # 2. Check if username is missing
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 3. Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # 4. Add the new user to the users dictionary
    users[username] = data
    
    # 5. Return confirmation message with 201 Created status
    response_data = {
        "message": "User added",
        "user": data
    }
    return jsonify(response_data), 201

if __name__ == "__main__":
    app.run()
