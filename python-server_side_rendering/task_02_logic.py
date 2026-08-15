from flask import Flask, render_template
import json

# Initialize the Flask application
app = Flask(__name__)

# Function to read items from the JSON file
def get_items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            return data.get("items", [])
    except FileNotFoundError:
        return []

# Route for the items page
@app.route('/items')
def items():
    # Fetch items from items.json
    item_list = get_items()
    # Pass the items list to the template
    return render_template('items.html', items=item_list)

# (Optional) Retain previous routes if needed for the app structure
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
