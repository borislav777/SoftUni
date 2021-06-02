number_usernames = int(input())
usernames = set(input() for el in range(number_usernames))
for username in usernames:
    print(username)