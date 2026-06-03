# 🔗 URL Shortener API

A full-stack URL shortening application built using FastAPI, SQLAlchemy, SQLite, HTML, CSS, and JavaScript.

## 🚀 Features

* Shorten long URLs into unique short links
* Redirect users to the original URL
* Track click counts for each shortened URL
* Store URLs permanently using SQLite
* View all shortened URLs
* Search URLs by short code
* Display top clicked URLs
* Delete URLs
* Simple frontend interface for URL shortening

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* HTML
* CSS
* JavaScript

### Tools

* Git
* GitHub
* VS Code

## 📂 Project Structure

```text
url-shortener-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔥 API Endpoints

| Method | Endpoint          | Description              |
| ------ | ----------------- | ------------------------ |
| GET    | /                 | Home Page                |
| POST   | /shorten          | Create Short URL         |
| GET    | /urls             | Get All URLs             |
| GET    | /url/{short_code} | Get URL Details          |
| GET    | /analytics/top    | Top Clicked URLs         |
| DELETE | /url/{short_code} | Delete URL               |
| GET    | /{short_code}     | Redirect to Original URL |

## ▶️ Run Locally

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/app
```

## 📚 Concepts Learned

* REST APIs
* CRUD Operations
* FastAPI Routing
* SQLAlchemy ORM
* SQLite Databases
* Dependency Injection
* URL Redirection
* Git & GitHub Workflow

## 👩‍💻 Developer

**Mounika Sai Yaganti**

Master's Student in Computer Science
Montclair State University

This project was built as a personal learning project to gain hands-on experience in backend development and database integration using FastAPI.
