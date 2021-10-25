#!usr/bin/env python3.9
from cipher import User
from cipher import Attributes


def function():
    print("                                                                                                ")
    print("                                                                                                ")
    print("               010101   01010  010101010   10101  01010  1010101010  010101010                  ")
    print("              010  010   010    010    010  101    010    101         010    101                ")
    print("             101         101    101   101   0101010101    0101010     101  010                  ")
    print("             010         010    0101010     1010101010    1010101     010101                    ")
    print("              010  101   101    101         010    101    010         101 010                   ")
    print("               010101   10101  10101       01010  10101  0101010101  10101 01010                ")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~               ")
    print("                                                                                                ")
    print("                                                                                                ")


function()


def create_new_user(username, password):
    """
    Function to create a new user with a username and password
    """
    rookie_user = User(username, password)
    return rookie_user


def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()


def display_user():
    """
    Function to display existing user
    """
    return User.display_user()