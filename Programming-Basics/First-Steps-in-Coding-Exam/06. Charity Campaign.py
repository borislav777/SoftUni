days=int(input())
broi_sladkari=int(input())
broi_torti=int(input())
broi_gofreti=int(input())
broi_palachinki=int(input())
cake=broi_torti*45
gofreti=broi_gofreti*5.8
palachinki=broi_palachinki*3.2
cash_by_day=(cake+gofreti+palachinki)*broi_sladkari
total=cash_by_day*days
after_total=total-(total/8)
print(after_total)
