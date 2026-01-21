import re


def clean_format_number(number: str) -> str:
    if not number:
        return ""

    only_numbers = re.sub(r"\D", "", number)

    if only_numbers.startswith("54"):
        if not only_numbers.startswith("549"):
            return "549" + only_numbers[2:]
        return only_numbers

    return "549" + only_numbers
