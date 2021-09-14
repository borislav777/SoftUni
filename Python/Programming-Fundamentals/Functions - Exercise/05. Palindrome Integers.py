def is_palindrome(num):
    for el in num:

        if el == el[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
is_palindrome(numbers)
