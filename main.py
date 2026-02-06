import pybreaker
import time
import logging
from calendar_service import get_todays_birthdays
from whatsapp_client import send_whatsapp_message
from templates import MESSAGES
from config import Config, logger

main_logger = logging.getLogger("BdayFlow.Main")


def main():
    """
    Main entry point for the automation flow.
    Ocrchestrates the retrieval of data from Calendar and the delivery via WhatsApp.
    """
    main_logger.info("--- Starting Birthday Flow Automation ---")

    try:
        # Fetch today's birthdays from Google Calendar
        birthdays = get_todays_birthdays()
        main_logger.info(
            f"Retrieved {len(birthdays)} birthdays from Google Calendar."
        )
    except Exception:
        main_logger.critical(
            "Failed to access Google Calendar API", exc_info=True
        )
        return

    if not birthdays:
        main_logger.info("No birthdays found for today. Exiting.")
        return

        # Iterate through each birthday and send the greeting
    for person in birthdays:
        try:
            # Use dynamic templates for personalized messaging
            message_body = MESSAGES["generic"].format(
                client=person["name"], seller=person["seller"]
            )

            # Execute sending progress
            send_whatsapp_message(person["phone"], message_body)

        except pybreaker.CircuitBreakerError:
            main_logger.error(
                "CIRCUIT BREAKER OPEN: Infrastructure failure detected. Aborting mission."
            )
            break

        except Exception as error:
            main_logger.warning(
                f"Failed to send greeting to {person['name']}: {error}"
            )
            main_logger.info("Skipping to next client...")
            continue

        # Delay to filtering spam message
        time.sleep(Config.RETRY_DELAY)

    main_logger.info("--- Birthday Flow Automation Finished ---")


if __name__ == "__main__":
    main()
