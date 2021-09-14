type_projection=input()
rows=int(input())
colums=int(input())
price=0
cinema_capacity=rows*colums
if type_projection=="Premiere":
    price=12
elif type_projection=="Normal":
    price=7.50
elif type_projection=="Discount":
    price=5
total=price*cinema_capacity
print(f"{total:.2f}")