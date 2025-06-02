import requests
from faker import Faker

fake = Faker()

# Add 25 random books
for _ in range(25):
    book = {
        "title": fake.sentence(nb_words=4).replace(".", ""),
        "author": fake.name(),
        "genre": fake.word(),
        "yearPublished": int(fake.year())
    }
    response = requests.post("https://postman-library-api.glitch.me/books", json=book)
    print(f"Added: {book['title']} - Status Code: {response.status_code}")

# Retrieve all books
response = requests.get("https://postman-library-api.glitch.me/books")
books = response.json()

# Delete first five books
for book in books[:5]:
    del_response = requests.delete(f"https://postman-library-api.glitch.me/books/{book['id']}")
    print(f"Deleted: {book['title']} - Status Code: {del_response.status_code}")

# Delete last five books
for book in books[-5:]:
    del_response = requests.delete(f"https://postman-library-api.glitch.me/books/{book['id']}")
    print(f"Deleted: {book['title']} - Status Code: {del_response.status_code}")

