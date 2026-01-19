import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("WHAPI_TOKEN")
API_URL = os.getenv("WHAPI_URL")


def send_whatsapp_message(number, message_body):
    if not API_TOKEN:
        print("ERROR: WHAPI_TOKEN not found")
        return None

    clean_number = number.replace("+", "")

    payload = {
        "typing_time": 0,
        "to": f"{clean_number}@s.whatsapp.net",
        "body": message_body,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {API_TOKEN}",
    }
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Message sent via Whapi to {clean_number}!")
        return response.json().get("message", {}).get("id")
    except Exception as e:
        print(f"Error calling Whapi API: {e}")
        if "response" in locals():
            print(f"Response: {response.text}")
        return None
