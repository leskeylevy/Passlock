class Credential:
    '''
    class to generate instances of different credentials
    '''

    credential_list = []

    def __init__(self, site_name, userName, password, emailUsed):
        self.site_name = site_name
        self.userName = userName
        self.password = password
        self.emailUsed = emailUsed

    def save_credential(self):
        '''
        save credential method
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete method to delete saved credentials
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        method that takes site name and returns the credentials for that site
        Args:
            name: site name to search for
        :return:
            credentials for the site searched.
        '''

        for credential in cls.credential_list:
            if credential.site_name == name:
                return credential

    @classmethod
    def credential_exist(cls, name):
        '''
        method to search if the said credential exists
        Args:
            name:site name to search if exists
        returns:
            Boolean: Either true or false
        '''
        for credential in cls.credential_list:
            if credential.site_name == name:
                return True
        return False

    @classmethod
    def display_credential(cls):
        '''
        method to display all stored credentials
        '''
        return cls.credential_list
