command = input()
participant = {}
language = {}

while not command == "exam finished":
    comm = command.split("-")
    if comm[1] == "banned":
        participant.pop(comm[0])
    else:
        if comm[0] not in participant:
            participant[comm[0]] = int(comm[2])
        else:
            if int(comm[2]) > participant[comm[0]]:
                participant[comm[0]] = int(comm[2])

        if comm[1] not in language:
            language[comm[1]] = 1
        else:
            language[comm[1]] += 1

    command = input()
print("Results:")
for user, result in sorted(participant.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{user} | {result}")

print("Submissions:")

for lang, number in sorted(language.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{lang} - {number}")
