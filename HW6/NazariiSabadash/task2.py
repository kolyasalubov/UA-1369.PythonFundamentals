is_login_valid = False
attempts = 0

while not is_login_valid:
    login = input('enter your login: ')

    if login == 'First':
        print('welcomeee You have successfully logged in.')
        is_login_valid = True
    else:
        attempts += 1
        print(
            f'error => wrong login details.that"s attempt No{attempts}. try again.')
