import requests
import pybreaker
import logging
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)
from config import Config, logger
from utils.helpers import clean_format_number

ws_logger = logging.getLogger("BdayFlow.WhatsApp")

whatsapp_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)


@whatsapp_breaker
@retry(
    retry=retry_if_exception_type(requests.exceptions.RequestException),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    stop=stop_after_attempt(3),
    reraise=True,
)
def send_whatsapp_message(number, message_body):
    """
    Sends a text message via Evolution API.
    Ensures numbers are properly formatted for international WhatsApp delivery.
    """
    token = Config.EVOLUTION_TOKEN
    url = Config.EVOLUTION_URL

    # Standardize the phone number format using regex helper
    clean_number = clean_format_number(number)

    payload = {
        "number": clean_number,
        "text": message_body,
        "delay": 1200,
        "linkPreview": True,
    }

    headers = {"Content-Type": "application/json", "apikey": token}

    try:
        ws_logger.info(f"Attempting to send message to: {clean_number}")

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Trigger exception for 4xx/5xx status codes

        ws_logger.info(f"Success! Message sent to {clean_number}")
        return True
    except requests.exceptions.RequestException as e:
        ws_logger.error(f"Network error sending to {clean_number}: {str(e)}")
        raise
