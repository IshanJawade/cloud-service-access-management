# 🌩️ Cloud Service Access Management System

A backend system built with FastAPI to manage user access to cloud services based on subscription plans. It supports role-based access control (RBAC), usage tracking, and dynamic enforcement of API access limits.

---

## 🚀 Features

- 🧑‍💼 **Role-based access**: Admins vs Customers
- 📜 **Permission Management**: Define which cloud APIs are accessible
- 📦 **Subscription Plans**: Create plans with API access + usage limits
- 👥 **User Subscriptions**: Users subscribe to plans or get assigned by admins
- 📊 **Usage Tracking**: Count API calls per user, per API
- 🔐 **Access Control**: Auto-block access when limits are exceeded

---

## 📁 API Endpoints Overview

### 🔐 Authentication
- `POST /auth/register` – Register user
- `POST /auth/token` – Login and get token

### 🧑‍💼 Permissions (Admin Only)
- `POST /permissions/` – Create a permission
- `PUT /permissions/{id}` – Update permission
- `DELETE /permissions/{id}` – Delete permission

### 📦 Subscription Plans (Admin Only)
- `POST /plans/` – Create a plan
- `PUT /plans/{id}` – Update a plan
- `DELETE /plans/{id}` – Delete a plan

### 👤 User Subscriptions
- `POST /subscriptions/` – Subscribe user to a plan
- `PUT /subscriptions/{user_id}` – Update a user's plan
- `GET /subscriptions/{user_id}` – View user subscription

### 📊 Usage and Access
- `POST /usage/` – (Internal) Increment API usage
- `GET /usage/check/{user_id}/{api}` – Check if user can access an API
- `GET /cloud/api{1-6}` – Simulated cloud API calls (protected)

---

## 💾 Tech Stack

- ⚡ FastAPI
- 🐘 PostgreSQL (or SQLite for dev)
- 🔐 JWT Authentication
- 📦 SQLAlchemy ORM
- 📄 Swagger/OpenAPI docs at `/docs`

---

## 🧪 How to Run

1. **Clone the repo**
   git clone <your-repo-url>
   cd cloud_access_system

2. **Create and activate a virtualenv**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Run the app**
   uvicorn app.main:app --reload

5. **Open the API docs**
   - Swagger: http://127.0.0.1:8000/docs

---

## 🔑 Default Roles

- **Admin** – Can manage permissions, plans, and assign subcriptions to customers
- **Customer** – Can view and access APIs based on their subscription

---

## ✅ To-Do (Optional Enhancements)

- Add API logs for auditing
- Implement email/password recovery
- Add API for user to view their usage stats
- Frontend dashboard for admins and users

---

## 👨‍💻 Author

- Name : Ishan Jawade 
- CWID : 885186304 

---

## 📜 License

MIT License
