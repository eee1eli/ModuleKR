import asyncio
from googletrans import Translator, LANGUAGES

def calculate_bonus(salary: float, experience: float):
    if experience >= 10:
        percent = 10
    elif experience >= 5:
        percent = 5
    elif experience >= 2:
        percent = 2
    else:
        percent = 0
        
    bonus_amount = salary * (percent / 100.0)
    total_amount = salary + bonus_amount
    return percent, bonus_amount, total_amount

async def _translate_async(text: str, dest_lang: str) -> str:
    if dest_lang == 'uk': return text
    try:
        translator = Translator()
        result = await translator.translate(text, src='uk', dest=dest_lang)
        return result.text
    except:
        return text

def translate_text(text: str, dest_lang: str) -> str:
    if not dest_lang or dest_lang == 'uk':
        return text
    return asyncio.run(_translate_async(text, dest_lang))

def get_full_language_name(lang_code: str) -> str:
    return LANGUAGES.get(lang_code.lower(), lang_code).capitalize()