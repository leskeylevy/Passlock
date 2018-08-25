class User:
    '''
    Class that generates instaces of Users
    '''

    user_list = [] #Empty user list

    def __init__(self,first_name,last_name,email,location):
        '''
        defining the properties for object user

        Args:
        :param first_name: New user first name
        :param last_name: New user last name
        :param email: New user email
        :param location: New user location
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location