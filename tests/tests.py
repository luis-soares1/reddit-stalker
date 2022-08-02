import translate_api_handler as api
import pytest
import logging

@pytest.mark.parametrize(
"language", "origin_text, translated_text", [("ENG", "Olá", "Hello")]
                                            [("GER", "Como estás?", "Wie geht es dir?")]
                                            [("NED", "O meu nome é", "Mijn naam is")]
)
def test_translate_to_english() -> str:
    assert api.translate("origin_text", "language") == "translated_text"

def test_type_bag_of_words():
    assert isinstance(bag_of_words, list)

