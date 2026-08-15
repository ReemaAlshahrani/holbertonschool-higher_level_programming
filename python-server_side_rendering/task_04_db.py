from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
                # Convert id to integer and price to float for correct formatting and comparison
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception:
        return []
    return data

# Function to read data from the SQLite database
def read_sql():
    data = []
    try:
        conn = sqlite3.connect('products.db')
        # Use Row factory to access columns by name
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception:
        return []
    return data

# Route for displaying products based on source ('json', 'csv', 'sql') and optional id
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    error_message = None
    products_data = []

    # Determine data source based on query parameter
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    elif source == 'sql':
        products_data = read_sql()
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        filtered_data = [p for p in products_data if p['id'] == product_id]
        
        if not filtered_data:
            error_message = "Product not found"
            return render_template('product_display.html', error=error_message)
        
        products_data = filtered_data

    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
