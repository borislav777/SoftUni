def swap(ind1, ind2):
    result = numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]
    return result


def multiply(ind1, ind2):
    numbers[ind1] = numbers[ind1] * numbers[ind2]
    return numbers[ind1]


def decrease(num):
    result = [n - 1 for n in num]
    return result


numbers = [int(el) for el in input().split()]
command = input()

while not command == "end":
    if command == "decrease":
        numbers = decrease(numbers)

    else:
        comm, index1, index2 = command.split()
        index1 = int(index1)
        index2 = int(index2)
        if comm == "swap":

            swap(index1, index2)
        elif comm == "multiply":
            multiply(index1, index2)

    command = input()

print(", ".join([str(nums) for nums in numbers]))
