time_first=int(input())
time_secont=int(input())
time_third=int(input())
total_time=time_first+time_secont+time_third
minutes=total_time//60
second=total_time%60
if second<10:
    print(f"{minutes}:0{second}")
else:
    print(f"{minutes}:{second}")

