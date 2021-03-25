hour=int(input())
minutes=int(input())
hour_arriving=int(input())
minutes_arriving=int(input())
time_arriving_in_minutes=hour_arriving*60+minutes_arriving
time_exam_in_minutes=hour*60+minutes
difference=abs(time_arriving_in_minutes-time_exam_in_minutes)

if time_arriving_in_minutes>time_exam_in_minutes:
    print("Late")
elif time_exam_in_minutes-30<=time_arriving_in_minutes<=time_exam_in_minutes:
    print("On time")
elif time_arriving_in_minutes<time_exam_in_minutes-30:
    print("Early")
if time_exam_in_minutes-60<time_arriving_in_minutes<time_exam_in_minutes:
    print(f"{difference} minutes before the start")
elif time_exam_in_minutes-60>=time_arriving_in_minutes:
    difference_hour=difference//60
    difference_minutes=difference%60
    if difference_minutes<=9 :
            print(f"{difference_hour}:0{difference_minutes} hours before the start")
    else:
            print(f"{difference_hour}:{difference_minutes} hours before the start")
elif time_exam_in_minutes<time_arriving_in_minutes<time_exam_in_minutes+60:
    print(f"{difference} minutes after the start")
elif time_exam_in_minutes+60<=time_arriving_in_minutes:
    difference_hour=difference//60
    difference_minutes=difference%60
    if difference_minutes<=9 :
            print(f"{difference_hour}:0{difference_minutes} hours after the start")
    else:
            print(f"{difference_hour}:{difference_minutes} hours after the start")



