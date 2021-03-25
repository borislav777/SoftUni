command = input()
companys = {}
while not command == "End":
    company, user_id = command.split("->")
    if company not in companys:
        companys[company] = []
    if user_id not in companys[company]:
        companys[company].append(user_id)
    command = input()

for company, users in sorted(companys.items(), key=lambda kvp: kvp[0]):
    print(f"{company}")
    for user in users:
        print(f"--{user}")
