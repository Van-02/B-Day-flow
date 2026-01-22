import pytest
from unittest.mock import patch, MagicMock
from whatsapp_client import send_whatsapp_message


@patch("whatsapp_client.requests.post")
def test_send_whatsapp_message_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": {"id": "ABC_123"}}
    mock_post.return_value = mock_response

    result = send_whatsapp_message("5492604123456", "Hi Test")

    assert result == "ABC_123"
    args, kwargs = mock_post.call_args
    assert (
        "https://gate.whapi.cloud/messages/text" in args
        or kwargs.get("url") == "https://gate.whapi.cloud/messages/text"
    )
    assert kwargs["json"]["body"] == "Hi Test"


@patch("whatsapp_client.requests.post")
def test_send_whatsapp_message_failure(mock_post):
    mock_post.side_effect = Exception("API Error")

    result = send_whatsapp_message("5492604123456", "Hi Test")

    assert result is None
