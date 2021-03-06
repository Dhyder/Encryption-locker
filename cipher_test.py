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

    def test_stockpile_attribute(self):
        """
        Test case to test if attribute is saved into the attributes list.
        """
        self.contemporary_attribute.save_specifics()
        self.assertEqual(len(Attributes.attributes_list), 1)

    def tearDown(self):
        """
        This method cleans up after each test case has run.
        """
        Attributes.attributes_list = []

    def test_multiple_accounts_save(self):
        """
        Tests if we can save multiple Attributes objects to our attributes list
        """
        self.contemporary_attribute.save_specifics()
        test_attribute = Attributes("Free_City", "Jodie_Comer", "Villanelle@*Oxana!")
        test_attribute.save_specifics()
        self.assertEqual(len(Attributes.attributes_list), 2)

    def test_terminate_attribute(self):
        """
        Tests if we can remove an account's attributes from our Attributes list
        """
        self.contemporary_attribute.save_specifics()
        test_attribute = Attributes("Free_City", "Jodie_Comer", "Villanelle@*Oxana!")
        test_attribute.save_specifics()

        self.contemporary_attribute.terminate_attributes()
        self.assertEqual(len(Attributes.attributes_list), 1)

    def test_locate_attribute(self):
        """
        Tests if location of a certain attribute entry by account name and display the details of the attribute is
        plausible
        """
        self.contemporary_attribute.save_specifics()
        test_attribute = Attributes("Free_City", "Jodie_Comer", "Villanelle@*Oxana!")
        test_attribute.save_specifics()

        this_attribute = Attributes.locate_attribute("Free_City")

        self.assertEqual(this_attribute.account, test_attribute.account)

    def test_attribute_exists(self):
        """
        Tests if we can return a boolean value based on whether we can or can't locate the attribute.
        """
        self.contemporary_attribute.save_specifics()
        this_attribute = Attributes("Free_City", "Jodie_Comer", "Villanelle@*Oxana!")
        this_attribute.save_specifics()
        attribute_located = Attributes.if_attribute("Free_City")
        self.assertTrue(attribute_located)

    def test_exhibit_saved_attributes(self):
        """
        Exhibits all attributes saved by the user
        """
        self.assertEqual(Attributes.exhibit_attributes(), Attributes.attributes_list)


if __name__ == '__main__':
    unittest.main()
