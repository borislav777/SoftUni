palindrome = [pal for pal in input().split() if pal == pal[::-1]]
searched_palindrome = input()
print(palindrome)
print(f"Found palindrome {palindrome.count(searched_palindrome)} times")
