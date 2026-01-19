from calendar_service import get_todays_birthdays
from whatsapp_client import send_whatsapp_message
import time


def main():
    print("--- Starting B-Day Flow Automation ---")

    try:
        birthdays = get_todays_birthdays()

        if not birthdays:
            print("No birthdays found for today.")
            return

        for person in birthdays:
            message_body = f"Hola {person['name']}!."
            print(f"Sending greeting to {person['name']}...")

            result_sid = send_whatsapp_message(person["phone"], message_body)

            if result_sid:
                print(f"Success! SID: {result_sid}")

            time.sleep(2)

    except Exception as error:
        print(f"An error occurred in main execution: {error}")


if __name__ == "__main__":
    main()
