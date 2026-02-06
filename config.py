import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file at the project root
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.FileHandler("bday_flow.log"), logging.StreamHandler()],
)

logger = logging.getLogger("BdayFlow")


class Config:
    """
    Centralized configuration class to manage environment variables
    and application-wide settings.
    """

    # Evolution API Credentials
    EVOLUTION_TOKEN = os.getenv("AUTHENTICATION_API_KEY")
    EVOLUTION_URL = "http://localhost:8080/message/sendText/BdayFlow"

    # Google Calendar Settings
    CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID")

    # App Setting
    RETRY_DELAY = 15
