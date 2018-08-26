#!/usr/bin/env python3.6
from user import User


def create_user(fname, lname, email, location):
    '''
    function to create a new user
    '''
    new_user = User(fname, lname, email, location)
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
def main():
    print("Hello Welcome to  Passlock.What is your name?")
    user_name = input()

    print(f"Hello {user_name}.to sign up to Passlock create an account.")
    print('\n')

    while True:
            print("Use these short codes to navigate the app :\n cu -> Sign up.\n da -> Display your account.\n ln -> Login.\n ex ->exit Passlock.")

            short_code = input().lower()

            if short_code == 'cu':
                print("New Passlock Account")
                print("-"*100)

                print("First name ....")
                f_name = input()

                print("Last name....")
                l_name = input()

                print("Email address ...")
                e_address = input()

                print("Your location .....")
                y_location = input()

                save_users(create_user(f_name,l_name,e_address,y_location))
                print('\n')
                print(f"New User  {f_name} {l_name} created")
                print('\n')

            elif short_code == 'fu':

                if find_user():
                        print("Enter the last name of the user you want to search for")

                        search_lname = input()
                        if check_existing_user(search_lname):
                            search_user = find_user(search_lname)
                            print(f"{search_user.first_name}  {search_user.last_name}")
                            print('-' * 20)
                            print(f"Email address.......{search_user.email}")
                            print(f"Location......{search_user.location}")

                        else:
                            print("That user does not exist")

                elif short_code == "ex":
                        print("BYE!......")
                        break
                else:
                        print("I really didn't get that.Please use the short codes")


if __name__ =='__main__':
    main()