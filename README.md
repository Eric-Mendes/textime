# Convert plain text to datetime
[![PyPI version](https://badge.fury.io/py/textime.svg)](https://badge.fury.io/py/textime)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/textime)](https://pypi.org/project/textime/)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/Eric-Mendes/textime/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
> Currently only supporting English.

Python library that converts a date written as plain text to a datetime object.

## How to use it :computer:
First you install it in you environment like this
```bash
pip install textime
```
Then you can start using it already! Pass any string to the `text` parameter containing a date in the format: "`DAY` of `MONTH` of `YEAR`" where `YEAR` must be written out completely, like "first of May of two thousand and twenty one" or "second of August of one thousand nine hundred and ninety nine".
```python
from datetime import datetime

from textime import textime


text_to_dt: datetime = textime.to_datetime(text="Fifteenth of July of two thousand and eight")
```

## Contribution :pencil:
This project is open source. Contributions are welcome and appreciated. Please check our [guide for contributing](https://github.com/Eric-Mendes/textime/blob/main/CONTRIBUTING.md) and our [code of conduct](https://github.com/Eric-Mendes/textime/blob/main/CODE_OF_CONDUCT.md) as well.