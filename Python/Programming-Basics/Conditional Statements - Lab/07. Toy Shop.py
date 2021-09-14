ekskurziq=float(input())
number_puzzel=int(input())
number_dolls=int(input())
number_bears=int(input())
number_minions=int(input())
number_trucks=int(input())
cash=number_puzzel*2.60+number_dolls*3+number_bears*4.10+number_minions*8.20+number_trucks*2
number_toys=number_puzzel+number_dolls+number_bears+number_minions+number_trucks
if number_toys>=50:
    cash=cash-cash*0.25
rent=cash-cash*0.10
if rent>=ekskurziq:

        print(f"Yes! {rent-ekskurziq:.2f} lv left.")
else:
        print(f"Not enough money! {ekskurziq-rent:.2f} lv needed.")
