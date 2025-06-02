import requests
from faker import Faker

fake = Faker()

for _ in range(25):
    book = {
        "title": fake.sentence(nb_words=4),
        "author": fake.name(),
        "genre": fake.word(),
        "yearPublished": fake.year()
    }
    response = requests.post("https://postman-library-api.glitch.me/books", json=book)
    print(f"Added: {book['title']} - Status Code: {response.status_code}")
