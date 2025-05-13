# Auth database (PostgreSQL)

This is the PostgreSQL database schema for the `auth-service`  
It handles everything related to authentication and access control, including:

- user accounts and roles
- two-factor authentication (2FA) codes
- email verification tokens
- password reset functionality
- login attempt tracking

---

## Schema overview

### Tables:
| Table Name                | Description                              |
|---------------------------|------------------------------------------|
| `users`                   | Main table for registered users          |
| `two_factor_codes`        | Temporary codes for login/registration   |
| `password_reset_tokens`   | Tokens for password reset flows          |
| `email_verification_tokens` | Tokens for email verification          |
| `login_attempts`          | Records login attempts (success/failure) |

### Enums:
- `user_role`: `'admin'`, `'librarian'`, `'user'`, `'guest'`

---

## Files

| File             | Purpose                                       |
|------------------|-----------------------------------------------|
| `1-schema.sql`   | Main schema definition                        |
| `2-data.sql`     | Optional seed data (e.g. test users)          |

---

## Docker integration

When using Docker, this database is initialized automatically via mounted SQL files:

```yaml
volumes:
  - ./infrastructure/auth-db/1-schema.sql:/docker-entrypoint-initdb.d/1-schema.sql
  - ./infrastructure/auth-db/2-data.sql:/docker-entrypoint-initdb.d/2-data.sql
```

