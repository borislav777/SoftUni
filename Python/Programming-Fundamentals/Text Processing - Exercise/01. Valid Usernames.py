users = input().split(", ")

for user in users:
    if len(user) in range(3, 17):
        if user.isalnum() or "-" in user or "_" in user:
            print(user)
