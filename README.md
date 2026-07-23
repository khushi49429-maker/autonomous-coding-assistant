# 🚀 Autonomous Coding Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/Google-Gemini-AI-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/GitHub-OAuth-black?style=for-the-badge&logo=github">
</p>

<p align="center">
An AI-powered coding assistant that helps developers generate, explain, review, and improve source code using Google Gemini AI with GitHub repository integration.
</p>

---

# 📖 About the Project

Code Mentor AI - Autonomous Coding Assistant is an AI-powered web application developed to help programmers throughout the software development lifecycle.

The application uses **Google Gemini AI** to:

- Generate source code
- Explain existing code
- Review code quality
- Detect bugs
- Suggest fixes
- Analyze GitHub repository files

The project is built using **FastAPI**, **MySQL**, **Google Gemini AI**, and the **GitHub REST API**.

---

# 🎯 Objectives

- Generate code from user prompts
- Explain existing source code
- Review source code
- Suggest bug fixes
- Connect GitHub repositories
- Review repository files using AI
- Maintain chat history
- Provide secure user authentication

---

# ✨ Features

## 🤖 AI Features

- AI Code Generation
- AI Code Explanation
- AI Code Review
- AI Bug Detection
- AI Bug Fix Suggestions

## 👤 User Features

- User Registration
- User Login
- Password Authentication
- Chat Interface
- Chat History Storage

## 🐙 GitHub Features

- GitHub OAuth Login
- Fetch User Repositories
- Browse Repository Files
- AI Review Selected File
- AI Fix Selected File

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

## AI

- Google Gemini API

## APIs

- GitHub REST API
- GitHub OAuth

## Tools

- Git
- GitHub
- VS Code
- Swagger UI

---

# 🏗️ Project Architecture

```text
                User
                  │
                  ▼
        Frontend (HTML/CSS/JS)
                  │
                  ▼
          FastAPI Backend
        ┌────────┼─────────┐
        ▼        ▼         ▼
 Google Gemini  MySQL   GitHub API
      AI      Database    OAuth
```

---

# 📂 Project Structure

```text
autonomous-coding-assistant-main/
│
├── backend/
│   ├── database/
│   │   ├── connection.py
│   │   ├── models.py
│   │   └── __init__.py
│   │
│   ├── app.py
│   ├── auth.py
│   ├── create_tables.py
│   ├── database.py
│   ├── llm.py
│   ├── models.py
│   ├── prompts.py
│   ├── routes.py
│   └── services.py
│
├── frontend/
│   ├── ai_coding_assistant.html
│   ├── chat.html
│   ├── chat.js
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── github_api/
│   ├── github_auth.py
│   ├── github_routes.py
│   ├── github_service.py
│   ├── my_coding_assistance.py
│   └── __init__.py
│
├── notebooks/
│   └── evaluation.ipynb
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── vercel.json
└── .gitignore
```

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/khushi49429-maker/autonomous-coding-assistant.git
```

## Move into Project

```bash
cd autonomous-coding-assistant-main
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file inside the **backend** folder.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_NAME=code_mentor_ai

GITHUB_CLIENT_ID=YOUR_GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET=YOUR_GITHUB_CLIENT_SECRET
```

---

# 🗄️ Database

Database Name:

```text
code_mentor_ai
```

### Users Table

- id
- username
- email
- password
- github_username
- github_token

### Chat History Table

- id
- user_id
- prompt
- response
- created_at

---

# ▶️ Running the Project

### Start MySQL

Ensure MySQL Server is running.

### Start Backend

```bash
uvicorn backend.app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

### Start Frontend

Open `frontend/index.html` using Live Server.

---

# 📡 API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | /signup |
| POST | /login |

## Chat

| Method | Endpoint |
|---------|----------|
| POST | /api/chat |
| GET | /chat-history/{user_id} |

## GitHub

| Method | Endpoint |
|---------|----------|
| GET | /github/login |
| GET | /github/callback |
| GET | /github/repos/{user_id} |
| GET | /github/files/{user_id}/{owner}/{repo} |
| POST | /github/review-file |
| POST | /github/fix-file |

---

# 🔄 Workflow

```text
User
 │
 ▼
Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Google Gemini AI
 ├── MySQL Database
 └── GitHub API
```

---

# 👥 Team Members

| Member | Role | Responsibility |
|---------|------|----------------|
| Nancy Daima | Backend Developer & Database Integration | FastAPI backend, authentication, MySQL integration, chat history, GitHub OAuth integration, REST APIs |
| Khushi | Frontend Developer | User interface, chat page, frontend integration |
| Anamika | AI & LLM Developer | Google Gemini integration and AI features |
| Bhawana | GitHub API Developer | GitHub repository integration and API operations |

---

# 🚀 Future Enhancements

- JWT Authentication
- Docker Support
- Cloud Deployment
- AI Code Refactoring
- Commit History Analysis
- Repository Cloning
- Code Execution Sandbox
- Dark Mode
- Voice Assistant

---

# 🤝 Contribution

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project was developed for educational purposes as part of a college group project.

---

# 🙏 Acknowledgements

- Google Gemini AI
- FastAPI
- MySQL
- GitHub
- Python Community
- Open Source Contributors

---

⭐ If you found this project useful, consider giving it a star on GitHub.