#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(fname, lname, email, Password):
    '''
    function to create a new user
    '''
    new_user = User(fname, lname, email, Password)
    return new_user


def save_users(user):
    '''
    function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()


def find_user(lname):
    '''
    function to find user
    '''
    return User.find_by_last_name()


def check_existing_user(lname):
    '''
    checking if user exists
    '''
    return User.user_exists()


def display_user():
    '''
    function to return the saved user
    :return:
    '''
    return User.display_user()

    # ________________________________CREDENTIALS_______________________________________


def create_credential(site_name, userName, password, emailUsed):
    '''
    function to create new credential
    :param site_name:
    :param userName:
    :param password:
    :param emailUsed:
    :return:
    '''
    new_credential = Credential(site_name, userName, password, emailUsed)
    return new_credential


def save_credential(credential):
    '''
    function to save credential created
    '''
    credential.save_credential()


def del_credential(credential):
    '''
    function to delete credential
    '''
    credential.delete_credential()


def find_credential(name):
    '''
   function that finds credentials by site name and returns the credential
    '''
    return Credential.find_by_name(name)


def check_credential_exists(name):
    '''
    function that checks if the credential exists with that site name
    :return: boolean
    '''
    return Credential.credential_exist(name)


def display_credential():
    '''
    function to display all credentials
    '''
    return Credential.display_credential()


def main():
    print("Hello Welcome to  Passlock.What is your name?")
    user_name = input()

    print(f"Hello {user_name}.to sign up to Passlock create an account.")
    print('\n')

    while True:
        print("Use these short codes to navigate the app :\n cu -> Sign up.\n da -> Display your account.\n ln -> "
              "Login.\n ex ->exit Passlock.")

        short_code = input().lower()

        if short_code == 'cu':
            print("New Passlock Account")
            print("-" * 100)

            print("First name ....")
            f_name = input()

            print("Last name....")
            l_name = input()

            print("Email address ...")
            e_address = input()

            print("Your Password .....")
            print("*" * 40)
            pwd = input()

            save_users(create_user(f_name, l_name, e_address, pwd))
            print('\n')
            print(f" A New account for {f_name} {l_name} created")
            print(f"You can now login to your account {l_name} using your Password.")
            print('\n')

        elif short_code == 'da':

            if display_user():
                print("Here is your account Details ")
                print('\n')
                for user in display_user():
                    print(f"Full name:{user.first_name} {user.last_name} user name:{user.last_name} Email {user.email}")
                    print('\n')
                else:
                    print('\n')
                    print("That user does not exist. Sign up to create user account")
                    print('\n')

            elif short_code == "ln":
                print("please Enter your last name.")
                account_name = input()
                print("please enter your password")
                password = input()
                if password == pwd:
                    print("you are now logged in")
                    print('-' * 20)


            else:
                print("Wrong password try again!")
        elif short_code == "ex":
            print(f"Thanks {user_name} and feel free to recomend  our services to your friends ")
            break
        else:
            print("I really didnt get that.Please use the short codes")


if __name__ == '__main__':
    main()
