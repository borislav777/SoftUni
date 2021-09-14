month = input()
nights = int(input())
studio = 0
apartament = 0
total_apartament = 0
total_studio = 0
if month == "May" or month == "October":
    studio = 50
    apartament = 65
    if nights > 14:
        studio *= 0.70
    elif nights > 7:
        studio *= 0.95
elif month == "June" or month == "September":
    studio = 75.20
    apartament = 68.70
    if nights > 14:
        studio *= 0.80
elif month == "July" or month == "August":
    studio = 76
    apartament = 77
total_studio = nights * studio
if nights > 14:
    apartament *= 0.90
total_apartament = nights * apartament
print(f"Apartment: {total_apartament:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
