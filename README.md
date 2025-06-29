# 📝 Blog API with FastAPI

A fully functional **Blog API** built using **FastAPI**, featuring:

- ✅ Full CRUD operations
- 🔐 JWT-based user authentication
- 🛡️ Password hashing with `passlib`
- 🗃️ Database ORM using `SQLAlchemy`

---

## 🚀 Features

- **User Registration & Login**
  - Secure password hashing with `passlib`
  - JWT token generation and verification with `python-jose`

- **Post Management**
  - Create, Read, Update, and Delete (CRUD) blog posts
  - Only authenticated users can create or modify content

- **Database Integration**
  - Uses `SQLAlchemy` ORM
  - Compatible with SQLite or PostgreSQL

---

## 📦 Tech Stack

- **FastAPI** – High-performance web framework
- **SQLAlchemy** – ORM for database interaction
- **SQLite/PostgreSQL** – Database
- **python-jose** – JWT authentication
- **passlib** – Secure password hashing
- **Pydantic** – Data validation and serialization
