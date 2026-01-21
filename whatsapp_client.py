import os
import requests
from config import Config
from utils.helpers import clean_format_number


def send_whatsapp_message(number, message_body):
    """
    Sends a text message via Whapi Cloud API.
    Ensures numbers are properly formatted for international WhatsApp delivery.
    """
    token = Config.WHAPI_TOKEN
    url = Config.WHAPI_URL
    if not token:
        print("ERROR: WHAPI_TOKEN not found")
        return None

    # Standardize the phone number format using regex helper
    clean_number = clean_format_number(number)

    # Construct the JSON payload required by Whapi
    payload = {
        "typing_time": 0,
        "to": f"{clean_number}@s.whatsapp.net",
        "body": message_body,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
    }

    try:
        # Perform the HTTP POST request to Whapi
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Trigger exception for 4xx/5xx status codes
        print(f"Message sent via Whapi to {clean_number}!")
        return response.json().get("message", {}).get("id")
    except Exception as e:
        print(f"Error calling Whapi API: {e}")
        # Safe check for response object existence in case of connection failure
        if "response" in locals():
            print(f"Response: {response.text}")
        return None
