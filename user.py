class User:
    user_list =[]
    '''
    this class defines blueprint of the user
    '''
    def __init__(self,username ,password):
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        function that saves new user objects
        '''
        User.user_list.append(self)