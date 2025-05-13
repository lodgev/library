from nicegui import ui
import httpx
import jwt

API_URL = "http://gateway-service:3000/auth/login"
JWT_SECRET = "ed73c27f0152572f885e87d1435153c56865d7ee379ffa0c89c6242616effade"

@ui.page("/login")
def login_page():
    ui.label("🔐 Login").classes("text-2xl font-bold mb-4")

    email_input = ui.input("Email or Username").props("outlined").classes("mb-2")
    password_input = ui.input("Password", password=True).props("outlined").classes("mb-4")

    def handle_login():
        email = email_input.value
        password = password_input.value

        if not email or not password:
            ui.notify("Please fill in all fields", type="negative")
            return

        try:
            response = httpx.post(API_URL, json={"email_or_username": email, "password": password})
            if response.status_code == 200:
                data = response.json()
                decoded = jwt.decode(data["access_token"], JWT_SECRET, algorithms=["HS256"])

                ui.store.set("access_token", data["access_token"])
                ui.store.set("user_id", decoded["user_id"])
                ui.store.set("role", decoded["role"])

                ui.notify("Login successful!", type="positive")
                ui.navigate.to("/")
            elif response.status_code == 403:
                ui.notify("Email not verified", type="warning")
            elif response.status_code == 401:
                ui.notify("Invalid credentials", type="negative")
            else:
                ui.notify(f"Error {response.status_code}", type="negative")
        except Exception as e:
            ui.notify(f"Connection error: {e}", type="negative")

    ui.button("Login", on_click=handle_login).classes("w-full bg-primary text-white")
    ui.button("Forgot Password", on_click=lambda: ui.navigate.to("/auth/forgot-password")).props("flat")
    ui.button("Register", on_click=lambda: ui.navigate.to("/auth/register")).props("flat")
