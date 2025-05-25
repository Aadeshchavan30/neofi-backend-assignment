# Collaborative Event Management System - NeoFi Backend Assignment

This project is a fully functional RESTful API built with FastAPI for collaborative event scheduling. It supports user authentication, role-based access, event sharing, version history, rollback, and change diffs.

## 🚀 Features Implemented
- JWT-based Authentication (Register/Login)
- Event CRUD with Recurrence Support
- Role-based Sharing (Owner, Editor, Viewer)
- Versioning & Rollback of Events
- View History & Difference Between Event Versions
- Swagger API Documentation

## 🛠️ Tech Stack
- Python 3.9+
- FastAPI
- Tortoise ORM
- SQLite (can be changed to PostgreSQL)
- Uvicorn
- JWT Auth via `python-jose`
- Password Hashing with `passlib`

## ✅ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/neofi-backend-assignment.git
cd neofi-backend-assignment

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Initialize DB (SQLite)
python
>>> import asyncio
>>> from app.database import init_db
>>> asyncio.run(init_db())
>>> exit()

# Run the server
uvicorn main:app --reload
