import pytest
from utils.helpers import clean_format_number


def test_clean_format_number_removes_plus_correctly():
    assert clean_format_number("+5492604123456") == "5492604123456"


def test_clean_format_number_adds_prefix_if_missing():
    assert clean_format_number("2604123456") == "5492604123456"


def test_clean_format_number_handles_already_clean_number():
    assert clean_format_number("5492604123456") == "5492604123456"
