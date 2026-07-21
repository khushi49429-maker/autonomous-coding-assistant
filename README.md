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

# 📖 About the Project

Autonomous Coding Assistant is an AI-powered web application designed to assist developers throughout the software development lifecycle. The application uses **Google Gemini AI** to generate code, explain existing code, review source code, and suggest improvements.

The project also integrates the **GitHub API** for repository-related operations and uses **FastAPI** as the backend framework with **MySQL** for database management.

This project was developed as a **college group project** to demonstrate the integration of Artificial Intelligence, backend development, frontend technologies, database management, and GitHub APIs into a single application.

---

# 📑 Table of Contents

- About the Project
- Problem Statement
- Objectives
- Features
- Technologies Used
- Project Architecture
- Folder Structure
- Installation Guide
- Requirements
- Environment Variables
- Running the Project
- API Endpoints
- Database
- GitHub API Module
- Team Members
- Future Enhancements
- Contributing
- License

---

# ❗ Problem Statement

Developers often spend a significant amount of time writing repetitive code, debugging programs, understanding unfamiliar codebases, and reviewing repositories. These manual tasks reduce productivity and increase development time.

The objective of this project is to build an intelligent AI-powered assistant capable of automating these tasks while improving coding efficiency.

---

# 🎯 Objectives

- Generate source code from user prompts.
- Explain existing source code.
- Review code and identify bugs.
- Suggest improvements and fixes.
- Integrate GitHub repositories.
- Provide secure user authentication.
- Store chat history for future reference.
- Build an interactive web interface.

---

# ✨ Features

## 🤖 AI Features

- AI Code Generation
- Code Explanation
- Code Review
- Bug Detection
- Bug Fix Suggestions

## 👤 User Features

- User Registration
- Secure Login
- Interactive Chat Interface
- Chat History

## 🔗 GitHub Features

- GitHub Repository Integration
- Repository Information Retrieval
- Repository Analysis

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

## Version Control

- Git
- GitHub

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
        Frontend (HTML/CSS/JS)
                  │
                  ▼
          FastAPI Backend
        ┌─────────┴─────────┐
        ▼                   ▼
 Google Gemini API      MySQL Database
        │
        ▼
   GitHub API Module
```

---

# 📂 Project Structure

```
autonomous-coding-assistant/
│
├── backend/
│   ├── database/
│   ├── app.py
│   ├── auth.py
│   ├── llm.py
│   ├── models.py
│   ├── prompts.py
│   ├── services.py
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── chat.html
│   ├── chat.js
│   ├── script.js
│   └── style.css
│
├── github_api/
│
├── docs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/khushi49429-maker/autonomous-coding-assistant.git
```

## 2️⃣ Open the Project

```bash
cd autonomous-coding-assistant
```

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate the Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 5️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Before running the project, make sure the following software is installed:

- Python 3.10 or above
- MySQL Server
- Git
- Visual Studio Code (Recommended)
- Google Gemini API Key

---

# 🔐 Environment Variables

Create a `.env` file inside the **backend** folder.

Example:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/database_name
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Running the Project

## Step 1: Start MySQL

Ensure that the MySQL server is running.

---

## Step 2: Run Backend

Navigate to the backend folder:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Step 3: Run Frontend

Open the **frontend** folder.

Launch:

```
index.html
```

using Live Server or your preferred web browser.

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|----------|----------------|-------------------------|
| GET | / | Home Route |
| GET | /health | Health Check |
| POST | /signup | Register User |
| POST | /login | Login User |
| POST | /generate-code | Generate AI Code |
| POST | /explain-code | Explain Source Code |
| POST | /review-code | Review Source Code |

---

# 🗄️ Database

The project uses **MySQL** as the relational database.

## Users Table

- User ID
- Username
- Email
- Password

## Chat History Table

- Chat ID
- User ID
- Prompt
- Response
- Timestamp

---

# 🔗 GitHub API Module

The GitHub API module provides:

- Repository Integration
- Repository Information Retrieval
- Repository Analysis
- Future Support for Repository Automation

---

# 👥 Team Members

Our project was developed collaboratively, with each member responsible for a specific module.

| Team Member | Role | Responsibilities |
|------------|------|------------------|
| **Nancy Daima** | Backend Developer & Database Integration | Developed the FastAPI backend, designed REST APIs, integrated the MySQL database, implemented authentication, and managed backend business logic. |
| **Khushi** | Frontend Developer | Designed and developed the user interface using HTML, CSS, and JavaScript, connected frontend pages with backend APIs, and improved the user experience. |
| **Anamika** | AI & LLM Integration | Integrated Google Gemini AI, implemented AI-powered code generation, code explanation, code review, and prompt engineering. |
| **Bhawana** | GitHub API Integration | Developed GitHub API functionality, implemented repository integration, fetched repository data, and managed GitHub-related operations. |

---

# 🚀 Future Enhancements

- Dark Mode
- Voice Assistant
- Multi-language Support
- JWT Authentication
- AI Code Refactoring
- Docker Deployment
- Cloud Deployment
- Repository Cloning
- Commit History Analysis
- Code Execution Sandbox

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push to your branch.
6. Open a Pull Request.

---

# 📄 License

This project is developed for **educational purposes** as part of a college group project.

---

# 🙏 Acknowledgements

We would like to thank:

- Google Gemini AI
- FastAPI
- MySQL
- GitHub API
- Python Community
- Open Source Contributors

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

Thank you for visiting our project!