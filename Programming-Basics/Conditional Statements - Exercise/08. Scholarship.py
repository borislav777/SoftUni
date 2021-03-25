income = float(input())
average_success = float(input())
min_salary = float(input())
excellent_result = int(average_success * 25)
social = int(min_salary * 0.35)
if average_success >= 5.50:
    if income < min_salary:
        if excellent_result >= social:
            print(f"You get a scholarship for excellent results {excellent_result} BGN")
        else:
            print(f"You get a Social scholarship {social} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_result} BGN")
elif average_success > 4.50:
    if income < min_salary:
        print(f"You get a Social scholarship {social} BGN")
    else:
        print("You cannot get a scholarship!")

else:
    print("You cannot get a scholarship!")
