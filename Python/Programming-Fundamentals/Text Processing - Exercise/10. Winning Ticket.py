def jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
                return True
            return False


def winning(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for symbol in winning_symbols:
        if symbol * 6 in left_half and symbol * 6 in right_half:
            match = min(left_half.count(symbol), right_half.count(symbol))
            print(f'ticket "{ticket}" - {match}{symbol}')
            return True
    return False


tickets = [el.strip() for el in input().split(", ")]

winning_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")

        continue
    if jackpot(ticket):
        continue

    if winning(ticket):
        continue
    print(f'ticket "{ticket}" - no match')
