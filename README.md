# 🎂 B-Day Flow: Birthday Automation

**Language**

- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

**B-Day Flow** is a professional Python automation tool that synchronizes Google Calendar events with WhatsApp. It automatically identifies today's birthdays from a specific calendar and sends personalized greetings via the Whapi.Cloud API.

## 🚀 Key Features

- **Google Calendar Integration:** Fetches events in real-time using Google Discovery API.
- **Automated WhatsApp Messaging:** Sends personalized messages via Whapi Cloud.
- **Smart Parsing:** Extracts client names, phone numbers, and seller info directly from event descriptions.
- **Robust Testing:** Includes a full suite of unit tests with Mocks for API stability.
- **Configurable:** Centralized management of environment variables and retry delays.

## 🛠️ Tech Stack

- **Language:** Python 3.14+
- **APIs:** Google Calendar API v3, Whapi.Cloud
- **Testing:** Pytest
- **Environment:** Dotenv for secret management

## 📦 Project Structure

```text
BdayFlow/
├── tests/              # Unit tests for services and helpers
├── utils/              # Formatting and regex helpers
├── calendar_service.py # Google Calendar logic
├── whatsapp_client.py  # WhatsApp API integration
├── config.py           # Configuration manager
├── main.py             # Main execution orchestrator
└── templates.py        # Message templates
```

## ⚙️ Setup & Installation

1. **Clone the repository:**

```Bash
git clone https://github.com/Van-02/bday-flow.git
cd bday-flow
```

1. **Create and activate a virtual environment:**

```Bash
python -m venv venv
source venv/bin/activate
```

1. **Install dependencies:**

```Bash
pip install -r requirements.text
```

1. **Configure Environment Variables**: Create a `.env` file in the root directory:

```Code
WHAPI_TOKEN=your_whapi_token_here
WHAPI_URL=[https://gate.whapi.cloud/messages/text](https://gate.whapi.cloud/messages/text)
GOOGLE_CALENDAR_ID=your_calendar_id@group.calendar.google.com
```

1. **Google API Credentials:** Place your `credentials.json` (from Google Cloud Console) in the root directoy. The `token.json` will be generated automatically after the first login.

## 🧪 Running Tests

To ensure everything is working correctly:

```Bash
python -m pytest -v
```
