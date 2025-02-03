from googletrans import Translator

def translate_text(text, lang):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=lang)
        return translation.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return None