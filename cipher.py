import string
import random
import pyperclip


class User:
    """
    Creates a User class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, username, password):
        """
        A method that accentuates the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instance into the user list
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def terminate_user(self):
        """
        This method deletes a saved account from the list
        """
        User.user_list.remove(self)


class Attributes:
    """
    This creates an attributes class to help create new objects of attributes
    """
    attributes_list = []

    @classmethod
    def authenticate_user(cls, username, password):
        """
        This method verifies whether a user is created in the user_list or not
        """
        our_user = ""
        for user in User.user_list:
            if user.username == username and user.password == password:
                our_user == user.username
        return our_user