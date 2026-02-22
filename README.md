# ✂️ ShortLink - Fullstack URL Shortener
A modern full-stack URL shortening service with detailed analytics and secure authentication. Built to demonstrate proficiency in **Django REST Framework** and **Vue.js 3 (Composition API)**.

---

## 📸 Dashboard & Analytics

<img width="1912" height="1033" alt="Снимок экрана 2026-02-13 144102" src="https://github.com/user-attachments/assets/0fd793d0-b7b2-46c9-b1ce-0ad7cf017b6a" />
<img width="1918" height="1032" alt="Снимок экрана 2026-02-13 144037" src="https://github.com/user-attachments/assets/c3e55146-8794-4049-b351-b6b26ad1cb82" />
<img width="1881" height="1030" alt="Снимок экрана 2026-02-22 142840" src="https://github.com/user-attachments/assets/37d638fd-02f4-4963-ae3b-a4de1dd7be2b" />


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

