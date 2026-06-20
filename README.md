# 📚 StudyBud – Collaborative Learning & Discussion Platform

A modern full-stack collaborative learning platform built with **Python, Django, Django REST Framework (DRF), MySQL, and JWT Authentication**. StudyBud enables users to create topic-based study rooms, join discussions, exchange messages, and manage learning communities through a responsive web interface and secure REST APIs.

---

## 🚀 Features

### 👤 Authentication
- User Registration
- User Login
- User Logout
- JWT Authentication (SimpleJWT)
- Protected API Endpoints
- Session Management
- CSRF Protection

---

### 📚 Study Rooms
- Create Room
- Update Room
- Delete Room
- Join Topic-Based Rooms
- Browse All Rooms
- Search Rooms

---

### 💬 Messaging
- Post Messages
- View Discussions
- Topic-Based Conversations

---

### 🏷 Topics
- Create Topics
- Browse Topics
- Search Topics
- Room Filtering

---

### 👤 User Profile
- Profile Page
- Update User Information
- Profile Image Upload *(Optional Upgrade)*

---

### ⚙ Admin Dashboard
- Django Admin Panel
- Manage Users
- Manage Rooms
- Manage Topics
- Manage Messages
- Search & Filters
- Custom Admin UI

---

### 🌐 REST API
- Room API
- Topic API
- Message API
- Register API
- Login API
- JWT Authentication
- Protected Endpoints

---

### 🎨 Frontend
- Responsive UI
- Bootstrap
- HTML5
- CSS3
- JavaScript
- Modern Animations
- Mobile Friendly

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Framework | Django 5/6 |
| API | Django REST Framework |
| Authentication | JWT (SimpleJWT) |
| Database | MySQL |
| ORM | Django ORM |
| Frontend | HTML5, CSS3, JavaScript |
| UI | Bootstrap |
| Version Control | Git & GitHub |
| Containerization | Docker |
| Image Upload | Pillow |
| Email | SMTP (Gmail) |

---

# 📂 Project Structure

```
StudyBud/
│
├── base_app/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── api_views.py
│   │   ├── urls.py
│   │
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
│
├── studybud/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── static/
├── templates/
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/studybud.git

cd studybud
```

---

## Create Virtual Environment

Windows

```bash
python -m venv env
```

Activate

```bash
env\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv env

source env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install mysqlclient
pip install pillow
```

---

# Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

Example

```
Username : admin

Email : admin@gmail.com

Password : ********
```

---

# Run Server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```

---

# Admin Panel

```
http://127.0.0.1:8000/admin/
Username=bankukr
Password=123@Banku
# 📚 StudyBud – Collaborative Learning & Discussion Platform

A modern full-stack collaborative learning platform built with **Python, Django, Django REST Framework (DRF), MySQL, and JWT Authentication**. StudyBud enables users to create topic-based study rooms, join discussions, exchange messages, and manage learning communities through a responsive web interface and secure REST APIs.

---

## 🚀 Features

### 👤 Authentication
- User Registration
- User Login
- User Logout
- JWT Authentication (SimpleJWT)
- Protected API Endpoints
- Session Management
- CSRF Protection

---

### 📚 Study Rooms
- Create Room
- Update Room
- Delete Room
- Join Topic-Based Rooms
- Browse All Rooms
- Search Rooms

---

### 💬 Messaging
- Post Messages
- View Discussions
- Topic-Based Conversations

---

### 🏷 Topics
- Create Topics
- Browse Topics
- Search Topics
- Room Filtering

---

### 👤 User Profile
- Profile Page
- Update User Information
- Profile Image Upload *(Optional Upgrade)*

---

### ⚙ Admin Dashboard
- Django Admin Panel
- Manage Users
- Manage Rooms
- Manage Topics
- Manage Messages
- Search & Filters
- Custom Admin UI

---

### 🌐 REST API
- Room API
- Topic API
- Message API
- Register API
- Login API
- JWT Authentication
- Protected Endpoints

---

### 🎨 Frontend
- Responsive UI
- Bootstrap
- HTML5
- CSS3
- JavaScript
- Modern Animations
- Mobile Friendly

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Framework | Django 5/6 |
| API | Django REST Framework |
| Authentication | JWT (SimpleJWT) |
| Database | MySQL |
| ORM | Django ORM |
| Frontend | HTML5, CSS3, JavaScript |
| UI | Bootstrap |
| Version Control | Git & GitHub |
| Containerization | Docker |
| Image Upload | Pillow |
| Email | SMTP (Gmail) |

---

# 📂 Project Structure

```
StudyBud/
│
├── base_app/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── api_views.py
│   │   ├── urls.py
│   │
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
│
├── studybud/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
├── static/
├── templates/
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/studybud.git

cd studybud
```

---

## Create Virtual Environment

Windows

```bash
python -m venv env
```

Activate

```bash
env\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv env

source env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install mysqlclient
pip install pillow
```

---

# Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

Example

```
Username : admin

Email : admin@gmail.com

Password : ********
```

---

# Run Server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```

---

# Admin Panel

```
http://127.0.0.1:8000/admin/
```

Login using superuser credentials.

---

# JWT Authentication

Install

```bash
pip install djangorestframework-simplejwt
```

Add to settings.py

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

---

# API Endpoints

## Register

```
POST /api/register/
```

Body

```json
{
    "username":"john",
    "email":"john@gmail.com",
    "password":"12345678"
}
```

Response

```json
{
    "message":"User created successfully"
}
```

---

## Login

```
POST /api/login/
```

Request

```json
{
    "username":"john",
    "password":"12345678"
}
```

Response

```json
{
    "refresh":"...",
    "access":"..."
}
```

---

## Protected API

```
GET /api/test/
```

Headers

```
Authorization: Bearer ACCESS_TOKEN
```

---

## Rooms

| Method | Endpoint |
|---------|----------|
| GET | /api/rooms/ |
| GET | /api/rooms/1/ |
| POST | /api/rooms/create/ |
| PUT | /api/rooms/update/1/ |
| DELETE | /api/rooms/delete/1/ |

---

## Topics

```
GET /api/topics/
```

---

## Messages

```
GET /api/messages/
```

---

# Docker

Build

```bash
docker build -t studybud .
```

Run

```bash
docker run -p 8000:8000 studybud
```

Using Docker Compose

```bash
docker-compose up --build
```

---

# Email Verification (Optional)

Configure SMTP

```python
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=AppPassword
```

---

# Profile Image Upload

Install Pillow

```bash
pip install pillow
```

Configure

```python
MEDIA_URL="/media/"

MEDIA_ROOT=BASE_DIR/"media"
```

---

# Git Commands

Initialize

```bash
git init
```

Add Files

```bash
git add .
```

Commit

```bash
git commit -m "Initial Commit"
```

Create Branch

```bash
git branch -M main
```

Add Remote

```bash
git remote add origin https://github.com/username/studybud.git
```

Push

```bash
git push -u origin main
```

---

# Performance Features

- Optimized Django ORM Queries
- JWT Authentication
- REST API Architecture
- Responsive UI
- Search & Filtering
- Protected Routes
- Django Admin
- Modular Project Structure

---

# Future Improvements

- Email Verification
- Profile Picture Upload
- Real-time Chat (WebSockets)
- Notifications
- Redis Caching
- Dark Mode
- AWS Deployment
- CI/CD Pipeline
- Nginx + Gunicorn
- Docker Compose

---

# Technologies Used

- Python
- Django
- Django REST Framework
- JWT Authentication
- MySQL
- Django ORM
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Git
- GitHub
- Docker
- Pillow

---

# Author

**Siddharth Gupta**

Backend Developer | Python | Django | REST API | MySQL

GitHub:
https://github.com/yourusername

LinkedIn:
https://linkedin.com/in/yourprofile

---

## ⭐ If you like this project, don't forget to give it a Star!
```

Login using superuser credentials.

---

# JWT Authentication

Install

```bash
pip install djangorestframework-simplejwt
```

Add to settings.py

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

---

# API Endpoints

## Register

```
POST /api/register/
```

Body

```json
{
    "username":"john",
    "email":"john@gmail.com",
    "password":"12345678"
}
```

Response

```json
{
    "message":"User created successfully"
}
```

---

## Login

```
POST /api/login/
```

Request

```json
{
    "username":"john",
    "password":"12345678"
}
```

Response

```json
{
    "refresh":"...",
    "access":"..."
}
```

---

## Protected API

```
GET /api/test/
```

Headers

```
Authorization: Bearer ACCESS_TOKEN
```

---

## Rooms

| Method | Endpoint |
|---------|----------|
| GET | /api/rooms/ |
| GET | /api/rooms/1/ |
| POST | /api/rooms/create/ |
| PUT | /api/rooms/update/1/ |
| DELETE | /api/rooms/delete/1/ |

---

## Topics

```
GET /api/topics/
```

---

## Messages

```
GET /api/messages/
```

---

# Docker

Build

```bash
docker build -t studybud .
```

Run

```bash
docker run -p 8000:8000 studybud
```

Using Docker Compose

```bash
docker-compose up --build
```

---

# Email Verification (Optional)

Configure SMTP

```python
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=AppPassword
```

---

# Profile Image Upload

Install Pillow

```bash
pip install pillow
```

Configure

```python
MEDIA_URL="/media/"

MEDIA_ROOT=BASE_DIR/"media"
```

---

# Git Commands

Initialize

```bash
git init
```

Add Files

```bash
git add .
```

Commit

```bash
git commit -m "Initial Commit"
```

Create Branch

```bash
git branch -M main
```

Add Remote

```bash
git remote add origin https://github.com/username/studybud.git
```

Push

```bash
git push -u origin main
```

---

# Performance Features

- Optimized Django ORM Queries
- JWT Authentication
- REST API Architecture
- Responsive UI
- Search & Filtering
- Protected Routes
- Django Admin
- Modular Project Structure

---

# Future Improvements

- Email Verification
- Profile Picture Upload
- Real-time Chat (WebSockets)
- Notifications
- Redis Caching
- Dark Mode
- AWS Deployment
- CI/CD Pipeline
- Nginx + Gunicorn
- Docker Compose

---

# Technologies Used

- Python
- Django
- Django REST Framework
- JWT Authentication
- MySQL
- Django ORM
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Git
- GitHub
- Docker
- Pillow

---

# Author

**Siddharth Gupta**

Backend Developer | Python | Django | REST API | MySQL

GitHub:
https://github.com/yourusername

LinkedIn:
https://linkedin.com/in/yourprofile

---

## ⭐ If you like this project, don't forget to give it a Star!