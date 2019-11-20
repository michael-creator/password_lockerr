import unittest
from user import User

class testUser(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_user = User('mickey', 'password')
    
    def test_save_user(self):
        '''
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def tearDown(self):
        '''
         tearDown does a clear up after evry test has run
        '''
        User.user_list =[]
    
  
if __name__== "__main__":
    unittest.main()