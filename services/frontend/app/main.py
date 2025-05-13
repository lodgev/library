from nicegui import ui
from dotenv import load_dotenv
import os
from app.pages import home
from app.pages.auth import (
    login,
    register,
    forgot_password,
    reset_password,
    logout,
    verify_email
)


load_dotenv()




# 📦 Запуск UI
ui.run(title="DevCore UI", port=8500)
