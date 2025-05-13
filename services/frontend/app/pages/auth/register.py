from nicegui import ui
import httpx

API_URL = "http://gateway-service:3000/auth/register"

@ui.page("/auth/register")
def register_page():
    ui.label("📝 Create Account").classes("text-2xl font-bold mb-4")

    first_name = ui.input("First Name").props("outlined").classes("mb-2")
    last_name = ui.input("Last Name").props("outlined").classes("mb-2")
    email = ui.input("Email").props("outlined").classes("mb-2")
    username = ui.input("Username").props("outlined").classes("mb-2")
    password = ui.input("Password", password=True).props("outlined").classes("mb-4")

    def handle_register():
        data = {
            "first_name": first_name.value,
            "last_name": last_name.value,
            "email": email.value,
            "username": username.value,
            "password": password.value
        }

        if not all(data.values()):
            ui.notify("Please fill in all fields.", type="negative")
            return

        try:
            response = httpx.post(API_URL, json=data)
            if response.status_code == 200:
                ui.notify("✅ Registration successful! Check your email to verify.", type="positive")
                ui.navigate.to("/login")
            elif response.status_code == 400:
                ui.notify("A user with this email or username already exists.", type="warning")
            else:
                ui.notify(f"Unexpected error: {response.status_code}", type="negative")
        except Exception as e:
            ui.notify(f"Connection error: {e}", type="negative")

    ui.button("Register", on_click=handle_register).classes("w-full bg-primary text-white")
    ui.button("Back to Login", on_click=lambda: ui.navigate.to("/login")).props("flat").classes("mt-2")
