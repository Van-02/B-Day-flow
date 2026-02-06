from calendar_service import get_todays_birthdays
from whatsapp_client import send_whatsapp_message
from templates import MESSAGES
from config import Config
import time


def main():
    """
    Main entry point for the automation flow.
    Ocrchestrates the retrieval of data from Calendar and the delivery via WhatsApp.
    """
    print("--- Starting B-Day Flow Automation ---")

    try:
        # Fetch today's birthdays from Google Calendar
        birthdays = get_todays_birthdays()
    except Exception as e:
        print(f"Error: Google Calendar could not be accessed: {e}")
        return

    if not birthdays:
        print("No birthdays found for today.")
        return

        # Iterate through each birthday and send the greeting
    for person in birthdays:
        try:
            # Use dynamic templates for personalized messaging
            message_body = MESSAGES["generic"].format(
                client=person["name"], seller=person["seller"]
            )

            print(f"Sending greeting to {person['name']}...")

            # Execute sending progress
            send_whatsapp_message(person["phone"], message_body)
            print(f"Message successfully send to {person['name']}!")

        except Exception as error:
            print(f"Error to send message to {person['name']}. -> {error}")
            print("Skip to next client...")
            continue

        # Delay to filtering spam message
        time.sleep(Config.RETRY_DELAY)


if __name__ == "__main__":
    main()
