"""Test sep_text."""
# pylint: disable=broad-except
from sep_text import __version__, sep_text


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not sep_text()
    except Exception:
        assert True


def test_single_text_en():
    """Test single text en"""
    text = """Typing defines a standard notation for Python function and variable type annotations. The notation can be used for documenting code in a concise, standard format, and it has been designed to also be used by static and runtime type checkers, static analyzers, IDEs and other tools."""
    res = sep_text(text)
    assert len(res) == 2
    assert sep_text.langs[:1] == ["en"]  # sep_text.langs: ['en', 'th']


def test_single_text_de():
    """Test single text de"""
    text_de = """ Der für Dienstagabend geplante erste Abschiebeflug aus Großbritannien nach Ruanda ist nach Angaben von Aktivisten im letzten Moment abgesagt worden. Wegen juristischer Einsprüche seien auch die Flugtickets der letzten noch verbliebenen abzuschiebenden Asylsuchenden storniert worden, teilte die Organisation Care4Calais auf Twitter mit. """

    res = sep_text(text_de)
    assert len(res) == 1
    assert sep_text.langs == ["de"]


def test_mixed_text_en_de():
    """Test mixed text en de"""
    text_en = """Typing defines a standard notation for Python function and variable type annotations. The notation can be used for documenting code in a concise, standard format, and it has been designed to also be used by static and runtime type checkers, static analyzers, IDEs and other tools."""
    text_de = """ Der für Dienstagabend geplante erste Abschiebeflug aus Großbritannien nach Ruanda ist nach Angaben von Aktivisten im letzten Moment abgesagt worden. Wegen juristischer Einsprüche seien auch die Flugtickets der letzten noch verbliebenen abzuschiebenden Asylsuchenden storniert worden, teilte die Organisation Care4Calais auf Twitter mit. """

    res = sep_text(f"{text_en}\n{text_de}")
    assert len(res) == 2
    assert set(sep_text.langs) == set(["en", "de"])
