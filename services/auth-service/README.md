# 🔐 DevCore Auth Service

This microservice handles authentication and authorization for the DevCore platform.

## ✅ Features

- JWT-based login/logout
- User registration with email verification
- Password reset (with email code)
- Login with email or username
- Role-based access (guest, user, librarian, admin)
- 2FA-ready (stored secret, validation logic extendable)
- Account lockout after 3 failed login attempts
- Microservice-ready (separate auth-db and notification service integration)

---

## ⚙️ Environment Variables (`.env`)

| Variable                  | Description                                |
|---------------------------|--------------------------------------------|
| `POSTGRES_HOST`           | Hostname of the PostgreSQL container       |
| `POSTGRES_PORT`           | Port for PostgreSQL (default: 5432)        |
| `POSTGRES_DB`             | Database name                              |
| `POSTGRES_USER`           | Database username                          |
| `POSTGRES_PASSWORD`       | Database password                          |
| `JWT_SECRET`              | Secret used to sign JWT tokens             |
| `JWT_ALGORITHM`           | Algorithm for JWT (e.g. HS256)             |
| `JWT_EXPIRATION_MINUTES` | Expiration time for access tokens          |
| `NOTIFICATION_SERVICE_URL`| URL to the notification microservice       |
| `FRONTEND_URL`            | Base URL of frontend (for email links)     |

---

## 🛠️ Run Locally (development)

```bash
# From root project directory
docker-compose up --build auth-service
```
Or run with Uvicorn manually:

bash
Копіювати
Редагувати
uvicorn app.main:app --reload --port 8000
🧪 Endpoints

Method	Path	Description
POST	/auth/register	Register a new user
POST	/auth/login	Log in and receive access token
POST	/auth/logout	Invalidate refresh token
POST	/auth/forgot-password	Send reset code to email
POST	/auth/reset-password	Set new password with code
GET	/auth/verify?token=...	Verify email address
📁 Project Structure
pgsql
Копіювати
Редагувати
auth-service/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── services/
├── .env
├── Dockerfile
└── requirements.txt
🔗 Related Services
notification-service → for sending emails

gateway-service → reverse proxy & access control

frontend → UI integration
