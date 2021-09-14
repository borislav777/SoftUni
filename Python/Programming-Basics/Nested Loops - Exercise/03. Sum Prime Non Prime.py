command = input()

sum_prime = 0
sum_no_prime = 0
while command != "stop":
    number = int(command)
    is_prime = True
    if number < 0:
        print("Number is negative.")
    else:
        for cheking in range(2, number):
            if number % cheking == 0:
                is_prime = False
                break
        if is_prime:
            sum_prime += number
        else:
            sum_no_prime += number

    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_no_prime}")
