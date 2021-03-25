type_flowers=input()
quantity=int(input())
budget=int(input())
price=0
total=0
if type_flowers=="Roses":
    price=5
    if quantity>80:
        price*=0.90
elif type_flowers=="Dahlias":
    price=3.80
    if quantity>90:
        price*=0.85
elif type_flowers == "Tulips":
    price=2.80
    if quantity>80:
        price*=0.85
elif type_flowers == "Narcissus":
    price=3
    if quantity<120:
        price*=1.15
elif type_flowers=="Gladiolus":
    price=2.50
    if quantity<80:
        price*=1.20
total=quantity*price
difference=abs(budget-total)
if total<=budget:
    print(f"Hey, you have a great garden with {quantity} {type_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")


