import json
import os
import sys
from module_function import calculate_bonus, translate_text, get_full_language_name

DATA_FILE = "MyData.json"

def format_money(amount):
    return f"{amount:,.2f}".replace(",", " ").replace(".00", "")

def main():
    data = None
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = None

   
    if not data or "language" not in data:
     
        lang = input("Введіть мову інтерфейсу (uk, en, de, fr, pl...): ").strip().lower()
        if not lang: lang = 'uk'

    
        prompt_exp = translate_text("Введіть стаж (кількість років):", lang)
        prompt_sal = translate_text("Введіть розмір зарплати (грн):", lang)
        
        try:
            exp_input = input(f"{prompt_exp} ")
            experience = float(exp_input)
            
            sal_input = input(f"{prompt_sal} ").replace(' ', '')
            salary = float(sal_input)
            
            if not (0 <= experience <= 70):
                raise ValueError("Стаж поза межами")
        except ValueError:
            print(translate_text("Помилка: введено некоректні дані.", lang))
            return

      
        new_data = {"experience": experience, "salary": salary, "language": lang}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
        
        print(translate_text(f"Дані збережено в файл {DATA_FILE}", lang))
        return

  
    exp = data["experience"]
    sal = data["salary"]
    lang = data["language"]

    percent, bonus, total = calculate_bonus(sal, exp)
    

    full_lang = get_full_language_name(lang)

    results = [
        f"Мова: {full_lang}",
        f"Зарплата: {format_money(sal)} грн. Стаж: {int(exp)} років.",
        f"Надбавка (%): {percent}%",
        f"Надбавка (грн): {format_money(bonus)} грн",
        f"Всього: {format_money(total)} грн"
    ]

    for line in results:
        print(translate_text(line, lang))

if __name__ == "__main__":
    main()