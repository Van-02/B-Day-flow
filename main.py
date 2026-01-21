from calendar_service import get_todays_birthdays
from whatsapp_client import send_whatsapp_message
from templates import MESSAGES
from config import Config
import time


def main():
    """
    Main entry point for the automation flow.
    Orchestrates the retrieval of data from Calendar and the delivery via WhatsApp.
    """
    print("--- Starting B-Day Flow Automation ---")

    try:
        # Fetch today's birthdays from Google Calendar
        birthdays = get_todays_birthdays()

        if not birthdays:
            print("No birthdays found for today.")
            return

        # Iterate through each birthday and send the greeting
        for person in birthdays:
            # Use dynamic templates for personalized messaging
            message_body = MESSAGES["generic"].format(
                client=person["name"], seller=person["seller"]
            )

            print(f"Sending greeting to {person['name']}...")

            # Execute sending progress
            result_sid = send_whatsapp_message(person["phone"], message_body)

            if result_sid:
                print(f"Success! SID: {result_sid}")

            # Politeness delay to avoid API rate limiting or anti-spam filters
            time.sleep(Config.RETRY_DELAY)

    except Exception as error:
        # Global catch-all to prevent unhandled app crashes
        print(f"An error occurred in main execution: {error}")


if __name__ == "__main__":
    main()
