import os
from dotenv import load_dotenv

# Load environment variables from .env file at the project root
load_dotenv()


class Config:
    """
    Centralized configuration class to manage environment variables
    and application-wide settings.
    """

    # Whapi API Credentials
    WHAPI_TOKEN = os.getenv("WHAPI_TOKEN")
    WHAPI_URL = os.getenv("WHAPI_URL")

    # Google Calendar Settings
    CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")

    # App Setting
    RETRY_DELAY = 5
