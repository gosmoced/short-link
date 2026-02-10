# ✂️ ShortLink - Fullstack URL Shortener
A modern full-stack URL shortening service with detailed analytics and secure authentication. Built to demonstrate proficiency in **Django REST Framework** and **Vue.js 3 (Composition API)**.

---

## 📸 Dashboard & Analytics

<img width="1919" height="1023" alt="Снимок экрана 2026-02-10 152517" src="https://github.com/user-attachments/assets/83854f51-133b-43c8-b8a3-ce9ea3706103" />

*Real-time analytics showing visitor IP addresses and timestamps for each link.*

* 🚀 **Deployment:** [View Website on Vercel](https://short-link-gilt.vercel.app/)

---

## ✨ Key Features

- **🚀 URL Shortening:** Instantly convert long URLs into short, shareable links.
- **📊 Analytics & Tracking:**
  - **Click Counter:** See the total number of visits for each link.
  - **Visitor Details:** Track **who** clicked (IP Address) and **when** (Timestamp).
- **👤 User Account Management:**
  - Secure **Registration & Login** via JWT.
  - Ability to **change password** and **update profile details** (username/email).
- **📱 Smart UI:** "Accordion" style interface allows viewing history for specific links without clutter.
- **☁️ Deployed:**
  - **Frontend:** Hosted on Vercel for high performance.
  - **Backend:** Hosted on PythonAnywhere.

---

## 🛠️ Tech Stack

### Backend (API)
- **Framework:** Django 5, Django REST Framework (DRF).
- **Database:** SQLite.
- **Authentication:** Simple JWT.
- **Security:** CORS headers configuration, secure password hashing.

### Frontend (Client)
- **Framework:** Vue.js 3 (Composition API, Script Setup).
- **Routing:** Vue Router.
- **HTTP Client:** Axios with interceptors for token management.
- **Build Tool:** Vite.
- **Styling:** CSS3, Responsive Design.

---
## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/auth/users/` | Register a new user (Djoser) |
| **POST** | `/auth/jwt/create/` | Login / Get Token (JWT) |
| **POST** | `/api/create/` | Create a new short link |
| **GET** | `/api/get-link/` | Get user's links with analytics |
| **DELETE** | `/api/delete-link/<id>/` | Delete a link by ID |
| **GET** | `/link/<title>/` | Public redirect to original URL |


## 🚀 How to Run Locally

If you want to run this project on your machine:

### 1. Clone the repository
```bash
git clone [https://github.com/gosmoced/short-link]
```
### 2. Backend Setup
```bash
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
## 📞 Contact
Created by **[gosmoced]**
* Telegram: [@gosmoced]
* Email: [danyliuk.erik@gmail.com]

