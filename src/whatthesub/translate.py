from googletrans import Translator


class TextTranslator:
    def __init__(self, dest_language="en"):
        self.translator = Translator()
        self.dest_language = dest_language

    async def translate(self, text):
        """Translate text to target language asynchronously"""
        try:
            # Use await for the async translation
            translated = await self.translator.translate(text, dest=self.dest_language)
            return translated.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text  # Return original text on failure
