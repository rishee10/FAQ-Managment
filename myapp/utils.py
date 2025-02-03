# faq/utils.py
from googletrans import Translator
from .models import FAQ

def translate_faq(faq):
    """
    Translate the question and answer of a FAQ into multiple languages (e.g., Hindi and Bengali).
    """
    translator = Translator()
    languages = ['hi', 'bn']  # List of languages you want to translate to
    
    # Translate the question and answer to other languages
    for lang in languages:
        translated_question = translator.translate(faq.question, dest=lang).text
        translated_answer = translator.translate(faq.answer, dest=lang).text
        
        # Set translated text on FAQ object
        setattr(faq, f'question_{lang}', translated_question)
        setattr(faq, f'answer_{lang}', translated_answer)
    
    faq.save()

def save_faq(faq):
    """
    Save the FAQ object and trigger translation for multiple languages.
    """
    translate_faq(faq)
