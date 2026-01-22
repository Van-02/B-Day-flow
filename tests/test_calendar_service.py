import pytest
from unittest.mock import MagicMock, patch
from calendar_service import get_todays_birthdays


@patch("calendar_service.get_calendar_service")
def test_get_todays_birthdays_extracts_correctly(mock_get_service):
    mock_event = {
        "items": [
            {
                "description": "Cliente: Van\nTelefono: +5492604123456\nVendedor: Jarvis",
                "summary": "Cumple de Van",
            }
        ]
    }

    mock_service = MagicMock()
    mock_get_service.return_value = mock_service
    mock_service.events().list().execute.return_value = mock_event

    result = get_todays_birthdays()

    assert len(result) == 1
    assert result[0]["name"] == "Van"
    assert result[0]["seller"] == "Jarvis"
