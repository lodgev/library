from nicegui import ui
import httpx

API_URL = "http://gateway-service:3000/auth/reset-password"

@ui.page("/auth/reset-password")
def reset_password_page():
    ui.label("🔁 Reset Password").classes("text-2xl font-bold mb-4")

    code_input = ui.input("Reset Code").props("outlined").classes("mb-2")
    password_input = ui.input("New Password", password=True).props("outlined").classes("mb-4")

    def handle_reset():
        code = code_input.value
        new_password = password_input.value

        if not code or not new_password:
            ui.notify("Please fill in both fields.", type="negative")
            return

        try:
            response = httpx.post(API_URL, json={
                "code": code,
                "new_password": new_password
            })

            if response.status_code == 200:
                ui.notify("✅ Password successfully updated!", type="positive")
                ui.navigate.to("/login")
            else:
                ui.notify(response.json().get("detail", "Invalid or expired code."), type="negative")

        except Exception as e:
            ui.notify(f"Connection error: {e}", type="negative")

    ui.button("Reset Password", on_click=handle_reset).classes("w-full bg-primary text-white")
    ui.button("Back to Login", on_click=lambda: ui.navigate.to("/login")).props("flat").classes("mt-2")