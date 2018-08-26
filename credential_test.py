import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    """
    test class defining test cases for credentials behaviour
    """

    def setUp(self):
        '''
        setup method to run b4 each test
        '''
        self.new_credential = Credential('Facebook', 'leskeylevy', 'mysecretpassword', 'leskeylevy@gmail.com')

    def test_init(self):
        '''
        test to see if the class was initiated properly
        '''
        self.assertEqual(self.new_credential.site_name, "Facebook")
        self.assertEqual(self.new_credential.userName, "leskeylevy")
        self.assertEqual(self.new_credential.password, "mysecretpassword")
        self.assertEqual(self.new_credential.emailUsed, "leskeylevy@gmail.com")

    def tearDown(self):
        '''
        method to clean up after each test case
        '''
        Credential.credential_list = []

    def test_save_credential(self):
        '''
        test tosee if credentials are being saved
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        '''
        test to see if multiple credentials can be saved
        '''
        self.new_credential.save_credential()
        test_credential = Credential('test.com', 'testuser', 'testpassword', 'testemail')
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        '''
        test to see if delete works
        '''
        self.new_credential.save_credential()
        test_credential = Credential('test.com', 'testuser', 'testpassword', 'testemail')
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_site_name(self):
        '''
        test to see if the user is able to search for credentials for a given site using the sites name
        '''
        self.new_credential.save_credential()
        test_credential = Credential('test.com', 'testuser', 'testpassword', 'testemail')
        test_credential.save_credential()
        found_credential = Credential.find_by_name('test.com')
        self.assertEqual(found_credential.site_name, test_credential.site_name)

    def test_credential_exists(self):
        '''
        test to see if we can return a boolean when credential not found
        :return: False credential does not exist
        '''
        self.new_credential.save_credential()
        test_credential = Credential('test.com', 'testuser', 'testpassword', 'testemail')
        test_credential.save_credential()

        credential_exists = Credential.credential_exist('test.com')

        self.assertTrue(credential_exists)



if __name__ == '__main__':
    unittest.main()
