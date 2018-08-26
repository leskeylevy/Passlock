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
        self.new_credential = Credential('Facebook','leskeylevy','mysecretpassword','leskeylevy@gmail.com')

    def test_init(self):
        '''
        test to see if the class was initiated properly
        '''
        self.assertEqual(self.new_credential.site_name,"Facebook")
        self.assertEqual(self.new_credential.userName, "leskeylevy")
        self.assertEqual(self.new_credential.password, "mysecretpassword")
        self.assertEqual(self.new_credential.emailUsed, "leskeylevy@gmail.com")

    def test_save_credential(self):
        '''
        test tosee if credentials are being saved
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)


if __name__ =='__main__':
    unittest.main()
