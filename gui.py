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


def login_user(username, password):
    """
    function that checks whether a user exist and then login the user in.
    """

    check_user = Attributes.authenticate_user(username, password)
    return check_user


def create_new_attribute(account, username, password):
    """
    Function that creates new credentials for a given user account
    """
    new_attribute = Attributes(account, username, password)
    return new_attribute


def save_attributes(attributes):
    """
    Function to save Credentials to the credentials list
    """
    attributes.save_specifics()


def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Attributes.exhibit_attributes()


def delete_attribute(attributes):
    """
    Function to delete a Credentials from credentials list

    """
    attributes.terminate_attributes()


def locate_attribute(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Attributes.locate_attribute(account)