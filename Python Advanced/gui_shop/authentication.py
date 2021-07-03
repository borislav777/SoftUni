import json

from tkinter import *
from canvas import tk
from helpers import clean_screen
from products import render_products


def login(usrname, pswrd):
    with open("db/user_credentials.txt", 'r') as file:
        data = file.readlines()
        for line in data:
            name, password = line[:-1].split(", ")
            if usrname == name and pswrd == password:
                with open("db/current_user.txt", 'w') as curr_file:
                    curr_file.write(name)
                    render_products()
                    return
        render_login_form(error="Invalid username or password")


def register(**user):
    user.update({'products': []})
    with open("db/users.txt", 'a', newline='\n') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open("db/user_credentials.txt", 'a') as file:
        file.write(f"{user['username']}, {user['password']}")
        file.write('\n')
    render_register_form()


def render_login_form(error=None):
    clean_screen()
    username = Entry(tk)
    Label(tk, text="Username:").grid(row=0, column=0)
    username.grid(row=0, column=1)
    password = Entry(tk)
    Label(tk, text="Password:").grid(row=1, column=0)
    password.grid(row=1, column=1)
    if error is not None:
        Label(tk, text="Invalid username or password").grid(row=3, column=1)
    Button(tk, text="OK", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2, column=1)


def render_register_form():
    clean_screen()
    Label(tk, text="Username").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    Label(tk, text="Password").grid(row=1, column=0)
    password = Entry(tk)
    password.grid(row=1, column=1)
    Label(tk, text="First Name").grid(row=2, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=1)
    Label(tk, text="Last Name").grid(row=3, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=1)
    Button(tk, text="Register", bg="green",
           command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(),
                                    last_name=last_name.get())).grid(row=4, column=1)


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", command=render_login_form).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", command=render_register_form).grid(row=0, column=1)
