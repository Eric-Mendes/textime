from datetime import datetime
from typing import Dict, List


def to_datetime(text: str, lang: str = "ENG") -> datetime:
    """Converts a date in written text to a datetime object.

    The text should have the format "`DAY` of `MONTH` of `YEAR`", where `YEAR` is
    the full number written out, like "two thousand and twenty two", or "one thousand nine hundred and ninety nine" (notice the lack of punctuation also).

    #### CURRENTLY ONLY SUPPORTS ENGLISH

    ### Parameters
    - :param text: the text with the date
    - :param lang: the language of the `text`. Defaults to `"ENG"` (English)

    ### Return
    - :return: a datetime object with the date specified in the `text` param."""
    day: int = 1
    month: int = 1
    year: int = 1970

    months: Dict[str, int] = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }
    days: Dict[str, int] = {
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4,
        "fifth": 5,
        "sixth": 6,
        "seventh": 7,
        "eighth": 8,
        "nineth": 9,
        "tenth": 10,
        "eleventh": 11,
        "twelveth": 12,
        "thirteenth": 13,
        "fourteenth": 14,
        "fifteenth": 15,
        "sixteenth": 16,
        "seventeenth": 17,
        "eighteenth": 18,
        "nineteenth": 19,
        "twentieth": 20,
        "twenty first": 21,
        "twenty second": 22,
        "twenty third": 23,
        "twenty fourth": 24,
        "twenty fifth": 25,
        "twenty sixth": 26,
        "twenty seventh": 27,
        "twenty eighth": 28,
        "twenty nineth": 29,
        "thirtieth": 30,
        "thirty first": 31,
    }
    numbers: Dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "twenty": 20,
        "thirty": 30,
        "fourty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    text = text.lower()
    new_text: List[str] = text.split()

    # day
    day = (
        days[new_text[0]]
        if days.get(new_text[1]) is None
        else days[" ".join(new_text[:2])]
    )

    # month
    for m, i in months.items():
        if m in text:
            month = i

    # year
    y = ""
    for i, word in enumerate(new_text):
        if word == "thousand":
            y += str(numbers[new_text[i - 1]])
            y += str(numbers.get(new_text[i + 1], 0))
            if y[-1] == "0":
                aux = str(numbers[new_text[i + 2]])
                if i + 2 == len(new_text)-1:
                    aux = "0" + str(numbers[new_text[i + 2]])
                if i + 3 < len(new_text):
                    aux = str(numbers[new_text[i + 2]] + numbers[new_text[i + 3]])
                y += aux
            else:
                aux = str(numbers[new_text[i + 4]])
                if i + 5 < len(new_text):
                    aux = str(numbers[new_text[i + 4]] + numbers[new_text[i + 5]])
                y += aux
    year = int(y)

    return datetime(year, month, day)
