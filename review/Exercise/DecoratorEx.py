# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}
user2 = {
    'name': 'Lucy',
    'valid': False
}


def authenticated(fn):
    def wraper(*args):
        if args[0]['valid'] == True:
            fn(*args)
        else:
            print('Invalid User')

    return wraper


@authenticated
def message_friends(*user):
    print(f'message has been sent to {user[0]["name"]}')


message_friends(user1)
message_friends(user2)

print(user1['valid'])
