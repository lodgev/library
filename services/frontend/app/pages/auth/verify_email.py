from nicegui import ui
import httpx

@ui.page("/auth/verify-email")
def verify_email_page():
    ui.label("📩 Verifying Email...").classes("text-xl mb-4")

    token = ui.query.get("token")
    if not token:
        ui.notify("Missing verification token", type="negative")
        ui.navigate.to("/login")
        return

    try:
        response = httpx.get(
            "http://gateway-service:3000/auth/verify", params={"token": token}
        )
        if response.status_code == 200:
            ui.label("✅ Email successfully verified!").classes("text-green-600 text-xl")
            ui.button("Go to Login", on_click=lambda: ui.navigate.to("/login")).classes("mt-4")
        else:
            ui.label("❌ Verification failed. Token may be expired or invalid.").classes("text-red-600")
            ui.button("Back to Register", on_click=lambda: ui.navigate.to("/auth/register")).classes("mt-4")
    except Exception as e:
        ui.label(f"❌ Server error: {e}").classes("text-red-600")
        ui.button("Back", on_click=lambda: ui.navigate.to("/")).classes("mt-4")
