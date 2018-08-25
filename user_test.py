import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User('leskey','levy','leskeylevy@gmail.com','Nairobi')

    def test_init(self):
        '''
        test to see if object isproperly initialised
        '''
        self.assertEqual(self.new_user.first_name,'leskey')
        self.assertEqual(self.new_user.last_name, 'levy')
        self.assertEqual(self.new_user.email, 'leskeylevy@gmail.com')
        self.assertEqual(self.new_user.location, 'Nairobi')

if __name__ == '__main__':
    unittest.main()