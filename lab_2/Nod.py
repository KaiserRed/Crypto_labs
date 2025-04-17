import json
import math
from sympy import isprime

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_factors(target_number, data):
    found = False
    for entry in data:
        b_str = entry["b"]
        b_cleaned = b_str.replace(" ", "").replace("\n", "")
        try:
            b_number = int(b_cleaned)
            common_divisor = math.gcd(target_number, b_number)
            
            if common_divisor > 1:
                print(f"Найден НОД:")
                
                if isprime(common_divisor):
                    p = common_divisor
                    q = target_number // p
                    print(f"Найдены простые множители: p = {p}, q = {q}")
                else:
                    print(f"НОД не является простым числом.")
                found = True
        except ValueError:
            print(f"Ошибка: не удалось преобразовать '{b_str}' в число")
    
    if not found:
        print("Нетривиальные делители не найдены.")

if __name__ == "__main__":
    target_number = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152852154660741055510013902155562081361962081595981911420549243824209510848251746533244000107548822959940247783543758121002469477638485548747439577077807719695549325118927778354644932972475948282546066354431328951111490357896748592181747880280860229387786352173196204698411196098855229174987078109775516711215169207291754767289629699943437953970024590148152458155990164703123080559051765953877965319207279108861098880815297029014831152784536829471762315781781832781690092801
    data = load_json("vars_lr2.json")
    find_factors(target_number, data)