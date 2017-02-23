def compact(text):
    result = text
    replacements = [("VIIII", "IX"), ("IIII", "IV"), ("LXXXX", "XC"), ("XXXX", "XL"), ("DCCCC", "CM"), ("CCCC", "CD")]
    for old, new in replacements:
        result = result.replace(old, new)
    return result

current = 0
final = 0
for i in open("p089_roman.txt"):
    roman = i.strip()
    current += len(roman)
    final += len(compact(roman))
print(current - final)
