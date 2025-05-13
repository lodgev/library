CREATE TABLE public.auth_users (
    id UUID PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    role VARCHAR NOT NULL DEFAULT 'guest', -- guest, user, librarian, admin
    is_verified BOOLEAN DEFAULT FALSE,
    is_locked BOOLEAN DEFAULT FALSE,
    login_attempts INT DEFAULT 0,
    refresh_token VARCHAR,
    two_fa_enabled BOOLEAN DEFAULT FALSE,
    two_fa_secret VARCHAR
);

CREATE TABLE public.auth_meta (
    user_id UUID PRIMARY KEY REFERENCES auth_users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    last_sign_in_at TIMESTAMP,
    reset_token VARCHAR,
    reset_token_expiration TIMESTAMP
);

CREATE TABLE public.auth_password_resets_codes (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES auth_users(id) ON DELETE CASCADE,
    code VARCHAR NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE
);

CREATE TABLE public.auth_email_codes (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES auth_users(id) ON DELETE CASCADE,
    code VARCHAR NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE
);
