def email_sender(email_address, message):
    # mock email sender
    print("sending email to {}, content:\n{}".format(email_address, message))


def user_credit(user, amount):
    user['balance'] = user['balance'] + amount
    send_email(user, 'debit processed')


def user_debit(user, amount):
    user['balance'] = user['balance'] + amount
    send_email(user, 'debit processed')


def send_email(user, message):
    email_sender(user['email'], message)
