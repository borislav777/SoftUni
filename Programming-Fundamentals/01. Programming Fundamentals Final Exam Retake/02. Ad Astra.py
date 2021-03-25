import re

text = input()
pattern = r"(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<date>\d{2}/\d{2}/\d{2})(?P=separator)(?P<calories>[0-9][0-9]{0,3})(?P=separator)"
total_calories = 0
foods = [obj.groupdict() for obj in re.finditer(pattern, text)]
for food in foods:
    total_calories += int(food['calories'])

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for print_food in foods:
    print(f"Item: {print_food['item']}, Best before: {print_food['date']}, Nutrition: {print_food['calories']}")
