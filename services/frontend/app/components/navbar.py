from nicegui import ui

def navbar():
    with ui.header().classes("bg-primary text-white items-center"):
        with ui.row().classes("w-full justify-between items-center px-4 py-2"):
            ui.label("📚 DevCore").classes("text-lg font-bold")

            with ui.row().classes("gap-2"):
                if ui.store.get("access_token"):
                    _extracted_from_navbar_8("My Profile", "/profile", "Logout", "/auth/logout")
                else:
                    _extracted_from_navbar_8("Login", "/login", "Register", "/auth/register")


# TODO Rename this here and in `navbar`
def _extracted_from_navbar_8(arg0, arg1, arg2, arg3):
    ui.button("Home", on_click=lambda: ui.navigate.to("/")).props("flat")
    ui.button(arg0, on_click=lambda: ui.navigate.to(arg1)).props("flat")
    ui.button(arg2, on_click=lambda: ui.navigate.to(arg3)).props("flat")
