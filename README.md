# 🎂 B-Day Flow: Birthday Automation

**Language**

- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

**B-Day Flow** is a professional Python automation tool that synchronizes Google Calendar events with WhatsApp. The system automatically identifies birthdays for the current day and sends personalized greetings using Evolution API.

## 🚀 Key Features

- **Google Calendar Integration:** Fetches events in real-time using Google Discovery API.
- **Automated WhatsApp Messaging:** Sends personalized messages via Evolution API.
- **Smart Parsing:** Extracts client names, phone numbers, and seller info directly from event descriptions.
- **Robust Testing:** Includes a full suite of unit tests with Mocks for API stability.

## 🛠️ Tech Stack

- **Language:** [Python 3.14+](www.python.org)
- **APIs:** [Google Calendar API v3](https://developers.google.com/workspace/calendar/api/guides/overview?hl=es-419), [Evolution API](https://github.com/EvolutionAPI/evolution-api)
- **Testing:** [Pytest](https://docs.pytest.org/en/stable/index.html)

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

## 🐳 Docker Deployment (Recommended)

1. Build and start the containers:

```Bash
docker-compose up -d --build
```

1. Google Auth

The first time you run it, the container will need you to log in to Google. Check the logs to find the authentication link:

```Bash
docker logs -f bday-flow
```

_Note: Ensure `credentials.json` is in the root directory before starting_

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
AUTHENTICATION_API_KEY=your_evolution_api_key
GOOGLE_CALENDAR_ID=your_calendar_id@group.calendar.google.com
```

1. **Google API Credentials:** Place your `credentials.json` (from Google Cloud Console) in the root directoy. The `token.json` will be generated automatically after the first login.

## 🧪 Running Tests

To ensure everything is working correctly:

```Bash
python -m pytest -v
```
