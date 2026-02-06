import pytest
from unittest.mock import MagicMock, patch

import requests
from whatsapp_client import send_whatsapp_message


@patch("whatsapp_client.requests.post")
def test_send_whatsapp_message_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    result = send_whatsapp_message("5492604123456", "Hi test")

    assert result is True

    args, kwargs = mock_post.call_args
    assert kwargs["json"]["text"] == "Hi test"


@patch("whatsapp_client.requests.post")
def test_send_whatsapp_message_failure(mock_post):
    mock_post.side_effect = requests.exceptions.RequestException("API Error")

    with pytest.raises(requests.exceptions.RequestException):
        send_whatsapp_message("5492604123456", "Hi test")
