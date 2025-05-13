from nicegui import ui
from app.components.navbar import navbar

@ui.page("/")
def home():
    navbar()

    ui.label("👋 Welcome to DevCore Library").classes("text-2xl font-bold mb-4")

    if ui.store.get("access_token"):
        user_id = ui.store.get("user_id")
        role = ui.store.get("role")
        ui.label(f"✅ Logged in as {role} (ID: {user_id})").classes("text-green-600")
    else:
        ui.label("🕵️ You are browsing as a guest").classes("text-yellow-600")

    ui.button("Browse Books", on_click=lambda: ui.navigate.to("/books")).props("flat").classes("mt-4")
