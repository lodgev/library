from nicegui import ui
import httpx

API_URL = "http://gateway-service:3000/auth/forgot-password"

@ui.page("/auth/forgot-password")
def forgot_password_page():
    ui.label("🔑 Forgot Password").classes("text-2xl font-bold mb-4")

    email_input = ui.input("Email").props("outlined").classes("mb-4")

    def send_reset_request():
        email = email_input.value

        if not email:
            ui.notify("Please enter your email.", type="negative")
            return

        try:
            response = httpx.post(API_URL, json={"email": email})
            if response.status_code == 200:
                ui.notify("📩 Reset code sent to your email!", type="positive")
                ui.navigate.to("/auth/reset-password")
            else:
                ui.notify(response.json().get("detail", "Something went wrong"), type="negative")
        except Exception as e:
            ui.notify(f"Connection error: {e}", type="negative")

    ui.button("Send Reset Code", on_click=send_reset_request).classes("w-full bg-primary text-white")
    ui.button("Back to Login", on_click=lambda: ui.navigate.to("/login")).props("flat").classes("mt-2")
