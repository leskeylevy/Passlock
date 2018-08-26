# import unittest
# from user import User
#
#
# class TestUser(unittest.TestCase):
#
#     def setUp(self):
#         self.new_user = User('leskey', 'levy', 'leskeylevy@gmail.com', 'Nairobi')
#
#     def test_init(self):
#         '''
#         test to see if object isproperly initialised
#         '''
#         self.assertEqual(self.new_user.first_name, 'leskey')
#         self.assertEqual(self.new_user.last_name, 'levy')
#         self.assertEqual(self.new_user.email, 'leskeylevy@gmail.com')
#         self.assertEqual(self.new_user.Password, 'Nairobi')
#
#     def tearDown(self):
#         User.user_list = []
#
#     def test_save_user(self):
#         '''
#         test to see if User object is saved into the user list
#         '''
#         self.new_user.save_user()
#         self.assertEqual(len(User.user_list), 1)
#
#     def test_save_multiple_user(self):
#         '''
#         test save multiple users to checkif we can save multiple users
#         '''
#         self.new_user.save_user()
#         test_user = User('leskey', 'levy', 'leskeylevy@gmail.com', 'Nairobi')
#         test_user.save_user()
#         self.assertEqual(len(User.user_list), 2)
#
#     def test_delete_user(self):
#         '''
#         test to see if the delete method works well
#         '''
#         self.new_user.save_user()
#         test_user = User('leskey', 'levy', 'leskeylevy@gmail.com', 'Nairobi')
#         test_user.save_user()
#
#         self.new_user.delete_user()
#         self.assertEqual(len(User.user_list), 1)
#
#     def test_find_user_by_last_name(self):
#         self.new_user.save_user()
#         test_user = User('leskey', 'levy', 'leskeylevy@gmail.com', 'Nairobi')
#         test_user.save_user()
#
#         found_user = User.find_by_last_name('levy')
#         self.assertEqual(found_user.last_name, test_user.last_name)
#
#     def test_user_exists(self):
#         self.new_user.save_user()
#         test_user = User('leskey', 'levy', 'leskeylevy@gmail.com', 'Nairobi')
#         test_user.save_user()
#
#         user_exists = User.user_exists('levy')
#         self.assertTrue(user_exists)
#
#
# if __name__ == '__main__':
#     unittest.main()
