from googletrans import Translator


def translator_word(word: str, lang: str):
    translator = Translator()
    result = translator.translate(word, dest=lang)
    return result.text.lower()






