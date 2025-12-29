# 🔐 AuthBox

AuthBox is a standalone authentication and user management backend built with **Django + Django REST Framework**.

It provides all core identity features required by modern applications, including:

- User registration & login
- JWT authentication
- Email verification
- Password reset
- Secure token handling
- Production-ready security practices

This project is designed to be reusable across multiple products (e.g., ATS, SaaS apps, internal tools).

---

## 🚀 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL (production)
- JWT Authentication
- SMTP (email verification & password reset)

---

## 🔒 Security

All secrets are stored using **environment variables**.

Never commit:
- `SECRET_KEY`
- Database credentials
- Email passwords

These are loaded via a `.env` file that is excluded from Git.

---

## 🛠 Setup (Local)

1. Clone the repository
2. Create `.env`
3. Add:

```env
SECRET_KEY=your-secret-key
DEBUG=True
