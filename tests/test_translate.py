import pytest
from whatthesub.translate import TextTranslator


@pytest.mark.asyncio  # Mark the test as async
async def test_translation():
    translator = TextTranslator(dest_language="es")
    result = await translator.translate("Hello")  # Use await here
    assert isinstance(result, str)
    assert len(result) > 0
    assert result.lower() in ["hola", "¡hola!"]  # Account for possible variations
