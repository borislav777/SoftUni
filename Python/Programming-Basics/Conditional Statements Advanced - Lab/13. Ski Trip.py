day=int(input())
room_type=input()
feedback=input()
nights=day-1
price=0
if room_type=="room for one person":
    price=nights*18
elif room_type=="apartment":
    price=nights*25
    if day<=10:
        price=price-price*0.30
    elif 10<day<=15:
        price=price-price*0.35
    elif day>15:
        price=price-price*0.50
elif room_type=="president apartment":
    price=nights*35
    if day<=10:
        price=price-price*0.10
    elif 10<day<=15:
        price=price-price*0.15
    elif day>15:
        price=price-price*0.20
if feedback=="positive":
    price=price+price*0.25
elif feedback=="negative":
    price=price-price*0.10
print(f"{price:.2f}")




