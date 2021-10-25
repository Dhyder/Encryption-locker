import unittest
from cipher import User
from cipher import Attributes


class TestClass(unittest.TestCase):
    """
    Defines test cases for the User class
    """

    def setUp(self):
        """
        Runs before solitary test methods run
        """
        self.rookie_user = User("Vickie_Shiraa", "Jessica*@hyde7502!")

    def test_inst(self):
        """
        Test case to check if the object has been instantiated correctly
        """
        self.assertEqual(self.rookie_user.username, "Vickie_Shiraa")
        self.assertEqual(self.rookie_user.password, "Jessica*@hyde7502!")

    def test_stockpile_user(self):
        """
        test case to test if a user instance was saved into the User list
        """
        self.rookie_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestAttributes(unittest.TestCase):
    """
    Test class that defines test cases for attributes class
    """

    def setUp(self):
        """
        Runs before solitary attribute test methods run
        """
        self.contemporary_attribute = Attributes("Amino", "Vickie_Shiraa", "Jessica*@hyde7502!")

    def test_inst(self):
        """
        Test class that checks if a new attributes instance has been instantiated veraciously
        """
        self.assertEqual(self.contemporary_attribute.account, "Amino")
        self.assertEqual(self.contemporary_attribute.username, "Vickie_Shiraa")
        self.assertEqual(self.contemporary_attribute.password, "Jessica*@hyde7502!")


if __name__ == '__main__':
    unittest.main()
