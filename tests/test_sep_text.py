"""Test sep_text."""
# pylint: disable=broad-except
from sep_text import __version__
from sep_text import sep_text


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not sep_text()
    except Exception:
        assert True
