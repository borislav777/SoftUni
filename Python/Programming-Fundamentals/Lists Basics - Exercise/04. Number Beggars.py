numbers = input().split(", ")
number_beggars = int(input())
sum_of_beggars = [0] * number_beggars
for number in range(len(numbers)):
    for number_1 in range(number_beggars):

        if not numbers:
            break
        sum_of_beggars[number_1] += int(numbers[0])
        numbers.remove(numbers[0])
print(sum_of_beggars)
