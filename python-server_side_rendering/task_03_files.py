from flask import Flask, render_template, request
import json
import csv
import os

# Initialize the Flask application
app = Flask(__name__)

# Function to read data from a JSON file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception:
        return []

# Function to read data from a CSV file
def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id and price to appropriate types for accurate comparison and display
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception:
        return []
    return data

# Route for displaying products based on source and optional id
@app.route('/products')
def products():
    # Get query parameters from the request
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    error_message = None
    products_data = []

    # Check if the source is valid
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            # If id is not a valid integer, treat it as not found
            return render_template('product_display.html', error="Product not found")

        filtered_data = [p for p in products_data if p['id'] == product_id]
        
        if not filtered_data:
            error_message = "Product not found"
            return render_template('product_display.html', error=error_message)
        
        products_data = filtered_data

    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
