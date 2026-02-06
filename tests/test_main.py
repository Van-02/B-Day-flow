import pytest
import main
from whatsapp_client import send_whatsapp_message
import requests


def test_main_loop_continues_on_failure(mocker):
    mock_birthdays = [
        {"name": "Client fail", "phone": "123", "seller": "Seller 1"},
        {"name": "Client success", "phone": "456", "seller": "Seller 2"},
    ]
    mocker.patch("main.get_todays_birthdays", return_value=mock_birthdays)

    mock_send = mocker.patch("main.send_whatsapp_message")

    mock_send.side_effect = [
        requests.exceptions.RequestException("API down"),
        True,
    ]

    mocker.patch("time.sleep", return_value=None)

    main.main()

    assert mock_send.call_count == 2
