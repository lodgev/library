import requests
import os

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALGORITHM = "HS256"

def notify_user(email: str, subject: str, message: str):
    try:
        response = requests.post(
            "http://notification-service:80/send",
            json={
                "recipient_email": email,
                "subject": subject,
                "message": message
            },
            headers={"Content-Type": "application/json"}
        )
        if response.status_code != 200:
            print("❌ Failed to notify user:", response.text)
    except Exception as e:
        print("❌ Notification service error:", e)
