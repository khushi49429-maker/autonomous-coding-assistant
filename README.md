# 🚀 Autonomous Coding Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/Google-Gemini-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/GitHub-API-black?style=for-the-badge&logo=github">
</p>


<p align="center">
An AI-powered coding assistant that helps developers generate, explain, review, and improve code using Google Gemini AI with GitHub API integration.
</p>


---

# 📖 About The Project

Autonomous Coding Assistant is an AI-powered web application designed to assist developers throughout the software development lifecycle.

The application uses **Google Gemini AI** to perform:

- Code Generation
- Code Explanation
- Code Review
- Bug Detection
- Bug Fix Suggestions

The project integrates the **GitHub REST API** for repository operations and uses **FastAPI** as the backend framework with **MySQL** for database management.

This project was developed as a college group project combining Artificial Intelligence, Backend Development, Database Management, Frontend Development, and API Integration.


---

# 🎯 Objectives

- Generate source code using AI prompts.
- Explain existing source code.
- Review code quality and detect issues.
- Suggest improvements and fixes.
- Integrate GitHub repositories.
- Analyze GitHub files using AI.
- Provide user authentication.
- Store user chat history.
- Build an interactive coding assistant.


---

# ✨ Features


## 🤖 AI Features

- AI Code Generation
- AI Code Explanation
- AI Code Review
- Bug Detection
- Bug Fix Suggestions
- GitHub File Analysis using Gemini AI


## 👤 User Features

- User Registration
- User Login
- Password Authentication
- Chat Interface
- Chat History Storage


## 🔗 GitHub Features

- Fetch GitHub Repositories
- Fetch Repository Files
- Fetch File Content
- AI Review of GitHub Files


---

# 🛠️ Technologies Used


## Frontend

- HTML5
- CSS3
- JavaScript


## Backend

- Python
- FastAPI
- SQLAlchemy


## Database

- MySQL


## Artificial Intelligence

- Google Gemini API


## APIs

- GitHub REST API


## Tools

- Git
- GitHub
- VS Code
- Swagger UI


---

# 🏗️ Project Architecture


```
                    User
                      |
                      |
              Frontend Interface
                      |
                      |
              FastAPI Backend
                      |
        --------------------------------
        |              |               |
        |              |               |
   Gemini AI       MySQL DB       GitHub API
        |              |               |
        |              |               |
 AI Code Features  User Data   Repository Analysis
```


---

# 📂 Project Structure


```
autonomous-coding-assistant/

│
├── backend/
│
│   ├── database/
│   │     ├── connection.py
│   │     └── __init__.py
│   │
│   ├── app.py
│   ├── models.py
│   ├── llm.py
│   ├── services.py
│   ├── prompts.py
│   └── .env
│
├── github_api/
│   ├── github_routes.py
│   └── github_service.py
│
├── frontend/
│
├── docs/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

```


---

# ⚙️ Installation Guide


## 1. Clone Repository

```bash
git clone https://github.com/khushi49429-maker/autonomous-coding-assistant.git
```


## 2. Open Project Folder

```bash
cd autonomous-coding-assistant
```


## 3. Create Virtual Environment

```bash
python -m venv venv
```


## 4. Activate Virtual Environment


### Windows

```bash
venv\Scripts\activate
```


### Linux/Mac

```bash
source venv/bin/activate
```


## 5. Install Dependencies

```bash
pip install -r requirements.txt
```


---

# 🔐 Environment Variables


Create a `.env` file inside the **backend folder**.


Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=code_mentor_ai

GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```


---

# 🗄️ Database


The project uses MySQL database.


Database:

```
code_mentor_ai
```


## Users Table

| Column | Description |
|---|---|
| id | User ID |
| username | Username |
| email | Email |
| password | Password |


## Chat History Table

| Column | Description |
|---|---|
| id | Chat ID |
| user_id | User ID |
| prompt | User Query |
| response | AI Response |
| created_at | Timestamp |


---

# ▶️ Running The Project


## Step 1: Start MySQL

Ensure MySQL server is running.


## Step 2: Start Backend


From the project root folder:


```bash
uvicorn backend.app:app --reload
```


Backend URL:

```
http://127.0.0.1:8000
```


Swagger Documentation:

```
http://127.0.0.1:8000/docs
```


---

# 📡 API Endpoints


## Authentication

| Method | Endpoint | Description |
|-|-|-|
| POST | /signup | Register User |
| POST | /login | Login User |


## AI Features

| Method | Endpoint | Description |
|-|-|-|
| POST | /generate-code | Generate Code |
| POST | /explain-code | Explain Code |
| POST | /review-code | Review Code |
| POST | /fix-bug | Fix Bugs |


## Chat

| Method | Endpoint | Description |
|-|-|-|
| POST | /api/chat | AI Chat |
| GET | /chat-history/{user_id} | Get Chat History |


## GitHub API

| Method | Endpoint | Description |
|-|-|-|
| GET | /github/repos | Fetch Repositories |
| GET | /github/files/{owner}/{repo} | Fetch Repository Files |
| GET | /github/file-content/{owner}/{repo}/{path} | Fetch File Content |
| POST | /github/review-file | Review GitHub File using AI |


---

# 🔗 GitHub API Module


The GitHub API module provides:

- Repository Integration
- Repository Information Retrieval
- Repository File Fetching
- AI-powered File Review


Workflow:

```
GitHub Repository
        |
        |
 GitHub REST API
        |
        |
 FastAPI Backend
        |
        |
 Gemini AI
        |
        |
 Code Review Result
```


---

# 👥 Team Members


| Member | Role | Responsibility |
|-|-|-|
| Nancy Daima | Backend Developer & Database Integration | Developed FastAPI backend, REST APIs, MySQL integration, authentication, and backend logic |
| Khushi | Frontend Developer | Developed frontend interface and connected frontend with backend APIs |
| Anamika | AI & LLM Developer | Integrated Google Gemini AI and implemented AI features |
| Bhawana | GitHub API Developer | Implemented GitHub API integration and repository operations |


---

# 🚀 Future Enhancements


- JWT Authentication
- Docker Deployment
- Cloud Deployment
- Code Execution Sandbox
- Repository Cloning
- Commit History Analysis
- AI Code Refactoring
- Dark Mode
- Voice Assistant


---

# 🤝 Contribution


1. Fork the repository.
2. Create a new branch.
3. Make changes.
4. Commit changes.
5. Push changes.
6. Create Pull Request.


---

# 📄 License


This project is developed for educational purposes as part of a college group project.


---

# 🙏 Acknowledgements


Special thanks to:

- Google Gemini AI
- FastAPI
- MySQL
- GitHub API
- Python Community
- Open Source Contributors


---

⭐ If you found this project useful, consider giving it a star on GitHub.