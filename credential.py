class Credential:
    '''
    class to generate instances of different credentials
    '''

    credential_list = []

    def __init__(self,site_name,userName,password,emailUsed):
        self.site_name = site_name
        self.userName = userName
        self.password = password
        self.emailUsed = emailUsed
