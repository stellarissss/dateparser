import pytest

from tests.linear_time import assert_fast

SETUP = """
from dateparser.conf import settings
from dateparser.languages import default_loader

def simplify(shortname, text):
    default_loader.get_locale(shortname)._simplify(text, settings=settings)
"""


@pytest.mark.parametrize("shortname", ["zh", "zh-Hans", "zh-Hant"])
@pytest.mark.parametrize("unit", ["一", "〇", "一〇", "1"])
def test_repeated_year_digits_do_not_take_quadratic_time(
    shortname: str, unit: str
) -> None:
    text = f"{unit!r} * (45_000 // {len(unit)}) + '年'"
    assert_fast(SETUP, [f"simplify({shortname!r}, {text})"])
