hours=int(input())
minutes=int(input())
after_fifteen_minutes=minutes+15
if after_fifteen_minutes>59:
    hours+=1
    after_fifteen_minutes-=60
if hours>23:
    hours=24-24
if after_fifteen_minutes<10:
    print(f"{hours}:0{after_fifteen_minutes}")
else:
    print(f"{hours}:{after_fifteen_minutes}")




