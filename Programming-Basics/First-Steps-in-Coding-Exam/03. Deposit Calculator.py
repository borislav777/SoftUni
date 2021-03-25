#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
money=float(input())
mouth=int(input())
year_precent=float(input())
precent=money*year_precent/100/12
cash=money+(mouth*precent)
print(cash)

