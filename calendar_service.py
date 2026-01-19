import datetime
import os.path
import os
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

load_dotenv()
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def get_todays_birthdays():
    service = get_calendar_service()

    calendar_id = os.getenv("GOOGLE_CALENDAR_ID")
    if not calendar_id:
        raise ValueError("FATAL ERROR: GOOGLE_CALENDAR_ID not found")

    now = datetime.datetime.now(datetime.timezone.utc)
    start_of_day = now.replace(
        hour=0, minute=0, second=0, microsecond=0
    ).isoformat()
    end_of_day = now.replace(
        hour=23, minute=59, second=59, microsecond=0
    ).isoformat()

    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=start_of_day,
            timeMax=end_of_day,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])
    birthday_list = []

    for event in events:
        description = event.get("description", "")
        if description:
            client_name = "Unknown"
            phone_number = ""

            lines = description.split("\n")
            for line in lines:
                if "Nombre cliente:" in line:
                    client_name = line.split("Nombre cliente:")[1].strip()
                if "Celular:" in line:
                    phone_number = (
                        line.split("Celular:")[1]
                        .strip()
                        .replace(" ", "")
                        .replace("-", "")
                    )

            if phone_number:
                birthday_list.append(
                    {"name": client_name, "phone": phone_number}
                )

    return birthday_list
