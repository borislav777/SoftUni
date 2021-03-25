budget=int(input())
season=input()
number_fisherman=int(input())
price=0
if season=="Spring":
    price=3000
elif season=="Summer"or season=="Autumn":
    price=4200
elif season=="Winter":
    price=2600
if number_fisherman<=6:
    price*=0.90
elif 7<=number_fisherman<=11:
    price*=0.85
elif number_fisherman>=12:
    price*=0.75
if number_fisherman%2==0 and season!="Autumn":
    price*=0.95
difference=abs(budget-price)
if budget>=price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
