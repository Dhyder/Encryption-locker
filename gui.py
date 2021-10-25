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


def check_attributes(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Attributes.if_attribute(account)


def engender_password():
    """
    generates a random password for the user.
    """
    auto_password = Attributes.engender_password()
    return auto_password


def copy_password(account):
    """
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Attributes.duplicate_password(account)


def cipher():
    print(
        "Hi There, I'm Cipher, your Encryption Locker...\n Please enter one of the following to proceed.\n CA "
        "--- "
        "(To Create Account)  \n LA ---  (Login To An Existing Account)  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('~' * 50)
        username = input("User_name: ")
        while True:
            print(" CP - (To create your own password)\n GP - (let cipher generate a random password for you)")
            password_choice = input().lower().strip()
            if password_choice == 'cp':
                password = input("Enter Password\n")
                break
            elif password_choice == 'gp':
                password = engender_password()
                break
            else:
                print("Invalid password, please try again")
        save_user(create_new_user(username, password))
        print("~" * 85)
        print(f"Hello {username}, Your account has been created successfully! Your password is: {password}")
        print("~" * 85)
    elif short_code == "la":

        print("Enter your Username and Password to log in:")
        print("~" * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Cipher")
            print('\n')
    while True:
        print(
            "Use The Following Short Codes:\n CC - (Create a new credential) \n DC - (Display Credentials) \n LC - ("
            "Locate a "
            "credential) \n GP - (let cipher generate a random password for you) \n Del - (Delete credential) \n Ex - ("
            "Exit the "
            "application) \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("." * 20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print(
                    "CP - (To create your own password)\n GP - (Let cipher generate a random password for you)")
                password_choice = input().lower().strip()
                if password_choice == 'cp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_choice == 'gp':
                    password = engender_password()
                    break
                else:
                    print("Invalid password please try again")
            save_attributes(create_new_attribute(account, username, password))
            print('\n')
            print(
                f"Account Attributes for: Account - {account} - UserName: {username} - Password:{password} created "
                f"successfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print(f"Here's your list of accounts : ")

                print('|*' * 15)
                print('_' * 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_' * 30)
                print('*|' * 15)
            else:
                print("Sorry, you have no credentials saved yet..........")
        elif short_code == "lc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if locate_attribute(search_name):
                search_attribute = locate_attribute(search_name)
                print(f"Account Name : {search_attribute.account}")
                print('-' * 50)
                print(f"User Name: {search_attribute.username} Password :{search_attribute.password}")
                print('-' * 50)
            else:
                print("Sorry, the credential declared does not exist")
                print('\n')
        elif short_code == "del":
            print("Enter the account name of the Attributes you want to delete")
            search_name = input().lower()
            if locate_attribute(search_name):
                search_attribute = locate_attribute(search_name)
                print("_" * 50)
                search_attribute.terminate_attributes()
                print('\n')
                print(f"Your stored credentials for : {search_attribute.account} have been successfully deleted!!!")
                print('\n')
            else:
                print("Sorry, the declared credential for deletion does not exist in your store yet")

        elif short_code == 'gp':

            password = engender_password()
            print(f" {password} Your cipher has been generated successfully. You can proceed to use it in your account")
        elif short_code == 'ex':
            print("Thanks for using Cipher.. See you soon!")
            break
        else:
            print("Incorrect... Your entries should correspond with the Menu above")


if __name__ == '__main__':
    cipher()
