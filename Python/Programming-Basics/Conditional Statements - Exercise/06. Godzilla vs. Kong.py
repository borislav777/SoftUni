film_budget=float(input())
number_statis=int(input())
price_cloths=float(input())
decor=film_budget*0.10

if number_statis>150:
    price_cloths_after=price_cloths*0.10
    price_cloths-=price_cloths_after

total_price_cloth=price_cloths*number_statis
total=decor+total_price_cloth
if total>film_budget:
    print("Not enough money!")
    print(f"Wingard needs {total-film_budget:.2f} leva more.")
elif total<=film_budget:
    print("Action!" )
    print(f"Wingard starts filming with {film_budget-total:.2f} leva left.")
