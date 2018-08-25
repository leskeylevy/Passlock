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