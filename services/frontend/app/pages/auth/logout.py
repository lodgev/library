from nicegui import ui

@ui.page("/auth/logout")
def logout_page():
    ui.store.clear()
    ui.notify("👋 You have been logged out", type="info")
    ui.navigate.to("/login")
