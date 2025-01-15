# Zoso - A Social Media Web Application

Zoso is a fully functional social media web application built using the Django framework. It includes features such as user authentication, posting media, adding friends, real-time chatting, and more. This document provides instructions on setting up and running the application locally.

---

## Features
- User authentication (sign up, log in, log out)
- Posting text and media
- Searching for and adding friends
- Real-time chat using WebSockets
- Profile management
- REST API for data access and manipulation

---

## Prerequisites
- Python 3.10.2 or higher
- Django 4.0.3
- Redis (or Memurai for Windows users)

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the repository or download the project as a zip file.
```bash
git clone https://github.com/your-repo/zoso.git
cd zoso
```

### Step 2: Create a Virtual Environment
Create and activate a virtual environment for the project:
```bash
python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Configure Redis/Memurai
- Install Redis (for Linux/Mac) or Memurai (for Windows).
- Ensure Redis/Memurai is running on port 6379.

### Step 5: Apply Migrations
Run Django migrations to set up the database:
```bash
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)
Create an admin account for managing the application:
```bash
python manage.py createsuperuser
```

### Step 7: Start the Development Server
Run the Django development server:
```bash
python manage.py runserver
```
The application will be accessible at http://127.0.0.1:8000.


### REST API
The REST API provides endpoints for managing users, profiles, posts, comments, and chats. Access the API root at: http://127.0.0.1:8000/zoso/api/
