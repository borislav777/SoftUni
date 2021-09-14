number_of_pieces = int(input())
pieces = {}
for _ in range(number_of_pieces):
    curr_pieces = input()
    piece, composer, key = curr_pieces.split("|")
    pieces[piece] = {'composer': composer, 'key': key}

command = input()

while not command == "Stop":
    operations = command.split("|")
    curr_operation = operations[0]
    if curr_operation == "Add":
        piece = operations[1]
        composer = operations[2]
        key = operations[3]
        if piece not in pieces:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif curr_operation == "Remove":
        piece = operations[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif curr_operation == "ChangeKey":
        piece = operations[1]
        new_key = operations[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for name,values in sorted(pieces.items(),key=lambda kvp:(kvp[0],kvp[1]['composer'])):
    print(f"{name} -> Composer: {values['composer']}, Key: {values['key']}")
