width = int(input())
lenght = int(input())
counter_piece = width * lenght
command = input()
isNopieces = False
while command != "STOP":
    piece = int(command)

    if piece > counter_piece:
        isNopieces = True

        break
    counter_piece -= piece
    command = input()
difference = abs(counter_piece - piece)
if isNopieces:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{counter_piece} pieces are left.")
