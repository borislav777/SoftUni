number=int(input())
for numbers in range(1111,10000):
    number_in_string=str(numbers)
    is_magic=True
    for digit in number_in_string:
        if int(digit)==0:
            is_magic=False
            break
        elif number%int(digit)!=0:
            is_magic=False
            break
    if is_magic:
        print(number_in_string,end=" ")
