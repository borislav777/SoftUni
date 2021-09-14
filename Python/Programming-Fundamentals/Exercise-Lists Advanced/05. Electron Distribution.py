electrons = int(input())
shells = []
electron = 1
while electrons:
    shell = 2 * electron ** 2
    if shell <= electrons:
        shells.append(shell)
        electrons -= shell
    else:
        shells.append(electrons)
        electrons -= electrons
    electron += 1
print(shells)
