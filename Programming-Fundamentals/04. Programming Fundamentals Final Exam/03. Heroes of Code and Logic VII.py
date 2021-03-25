number_heroes = int(input())
heroes = {}

for hero in range(number_heroes):
    current_hero = input()
    name, hp, mp = current_hero.split()
    hp = int(hp)
    mp = int(mp)
    if name not in heroes:
        heroes[name] = {'name': name, 'hp': hp, 'mp': mp}
    else:
        heroes[name]['hp'] += hp
        heroes[name]['mp'] += mp
command = input()

while not command == "End":
    split_command = command.split(" - ")
    curr_command = split_command[0]
    name = split_command[1]
    if curr_command == "CastSpell":
        need_mp = int(split_command[2])
        spell_name = split_command[3]
        if heroes[name]['mp'] >= need_mp:

            print(
                f"{name} has successfully cast {spell_name} and now has {abs(heroes[name]['mp'] - need_mp)} MP!")
            heroes[name]['mp'] -= need_mp
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif curr_command == "TakeDamage":
        damage = int(split_command[2])
        attacker = split_command[3]
        heroes[name]['hp'] -= damage
        if heroes[name]['hp'] > 0:
            print(
                f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hp']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
    elif curr_command == "Recharge":
        amount = int(split_command[2])
        if heroes[name]['mp'] + amount > 200:
            print(f"{name} recharged for {abs(200 - heroes[name]['mp'])} MP!")
            heroes[name]['mp'] = 200

        else:
            heroes[name]['mp'] += amount
            print(f"{name} recharged for {amount} MP!")
    elif curr_command == "Heal":
        amount = int(split_command[2])
        if heroes[name]['hp'] + amount > 100:
            print(f"{name} healed for {abs(100 - heroes[name]['hp'])} HP!")
            heroes[name]['hp'] = 100

        else:
            heroes[name]['hp'] += amount
            print(f"{name} healed for {amount} HP!")
    command = input()
for name, value in sorted(heroes.items(), key=lambda kvp: (-kvp[1]['hp'], kvp[0])):
    print(f"{name}\n  HP: {value['hp']}\n  MP: {value['mp']}")
