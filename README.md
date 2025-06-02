# 📚 School Library API Automation - SEfinal\_122147395

This project simulates interacting with a School Library API using Python and Postman. It includes functionality to add 25 random books and delete the first and last 5 books from the API.

---

## 🧪 Features Implemented

### ✅ Task 1: Postman API Usage

* Added 2 books using `POST` request
* Retrieved all books using `GET` request

### ✅ Task 2: Python Scripting with Git

* Created a Python script (`add100RandomBooks.py`) that:

  * Adds 25 random books to the API
  * Deletes the first 5 and last 5 books from the API
* Used `requests` and `faker` libraries for API interaction and dummy data

---

## 🚀 Getting Started

### Requirements

* Python 3.6+
* `requests` library
* `faker` library

### Setup

```bash
pip install requests faker
```

### Run the Script

```bash
python3 add100RandomBooks.py
```

---

## 🧾 Sample Output

```bash
Added: Title A - Status Code: 201
Added: Title B - Status Code: 201
...
Deleted: Title X - Status Code: 200
Deleted: Title Y - Status Code: 200
```

---

## 🔗 Git Workflow

1. Initialize Repo

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/SEfinal_122147395.git
```

2. Commit & Push

```bash
git add add100RandomBooks.py
git commit -m "Add 25 books and delete first/last 5"
git push -u origin main
```

---

## 🙋‍♂️ Author

* Student ID: 122147395
* Course: Software Engineering Final Project

---

## 🔗 GitHub Link

* [GitHub Repository](https://github.com/YOUR_USERNAME/SEfinal_122147395)

---

Feel free to fork and modify for your own testing and automation projects!
