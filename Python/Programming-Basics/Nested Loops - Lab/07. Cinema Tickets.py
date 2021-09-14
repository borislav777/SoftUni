command = input()
count_ticket_students = 0
count_ticket_kid = 0
count_ticket_standard = 0
count_seats = 0
is_finish = False

while command != "Finish":
    number_seats = int(input())

    movie_seats = 0
    while movie_seats < number_seats:

        type_ticket = input()
        if type_ticket == "student":
            count_ticket_students += 1
            count_seats += 1
            movie_seats += 1
        elif type_ticket == "kid":
            count_ticket_kid += 1
            count_seats += 1
            movie_seats += 1
        elif type_ticket == "standard":
            count_ticket_standard += 1
            count_seats += 1
            movie_seats += 1

        elif type_ticket == "End":

            break

    print(f"{command} - {movie_seats / number_seats * 100:.2f}% full.")
    command = input()
print(f"Total tickets: {count_seats}")
print(f"{count_ticket_students / count_seats * 100:.2f}% student tickets.")
print(f"{count_ticket_standard / count_seats * 100:.2f}% standard tickets.")
print(f"{count_ticket_kid / count_seats * 100:.2f}% kids tickets.")
