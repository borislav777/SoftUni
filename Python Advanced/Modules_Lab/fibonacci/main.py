from ex_fibunci import *

comm = input()
list_numbers = []
while not comm == "Stop":
    curr_command = comm.split()
    if curr_command[0] == "Create":
        list_numbers = generate_numbers(int(curr_command[2]))
        print(*list_numbers)
    else:
        locate_number(int(curr_command[1]), list_numbers)
    comm = input()
