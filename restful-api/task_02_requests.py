import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
            
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
