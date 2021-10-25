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

    def __init__(self, account, username, password):
        """
        Defines attributes to be stored
        """
        self.account = account
        self.username = username
        self.password = password

    def save_specifics(self):
        """
        Stores a new attribute to the attributes list
        """
        Attributes.attributes_list.append(self)

    def terminate_attributes(self):
        """
        This method deletes an account's Attributes from them attributes_list
        """
        Attributes.attributes_list.remove(self)

    @classmethod
    def locate_attribute(cls, account):
        """
        This method takes in an account's name and returns a attribute that matches that account's name
        """
        for attribute in cls.attributes_list:
            if attribute.account == account:
                return attribute

    @classmethod
    def duplicate_password(cls, account):
        located_attributes = Attributes.locate_attribute(account)
        pyperclip.copy(located_attributes.password)

    @classmethod
    def if_attribute(cls, account):
        """
        This checks an attributes existence from the attributes list and returns true or false.
        :return: True or False
        """
        for attribute in cls.attributes_list:
            if attribute.account == account:
                return True
        return False

    @classmethod
    def exhibit_attributes(cls):
        """
        This method returns all items in the attributes list
        """
        return cls.attributes_list

    def engender_password(self=9):
        """
        This produces a random password string of letters and digits and special characters
        :return: Random password
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "=_!@#$^&*~%?"
        return "".join(random.choice(password) for _ in range(self))