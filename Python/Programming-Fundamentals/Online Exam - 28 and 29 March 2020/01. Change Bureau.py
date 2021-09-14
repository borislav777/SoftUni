
number_bitcoin=int(input())
number_china=float(input())
commission=float(input())

number_china=number_china*0.15*1.76
number_bitcoin=number_bitcoin*1168
cash_in_euro=(number_bitcoin+number_china)/1.95
new_commission=cash_in_euro*commission/100
result=cash_in_euro-new_commission
print(f"{result:.2f}")
