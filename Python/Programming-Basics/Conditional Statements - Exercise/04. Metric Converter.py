currency=float(input())
in_currency=input()
out_currency=input()
result=0
if in_currency=="mm":
    if out_currency=="cm":
       result= currency/10
    elif out_currency=="m":
        result=currency/1000
if in_currency=="cm":
    if out_currency=="mm":
        result=currency*10
    elif out_currency=="m":
        result=currency/100
if in_currency=="m":
    if out_currency=="cm":
        result=currency*100
    elif out_currency=="mm":
       result= currency*1000
print(f"{result:.3f}")



