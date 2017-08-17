def email_sender(email_address, message):
    # mock email sender
    print("sending email to {}, content:\n{}".format(email_address, message))


class UserManager:

    users = [
        {'name': 'admin', 'balance': 1000, 'email': 'admin@planixs.com'}
    ]

    def add_user(self, user):
        self.users.append(user)

    def user_credit(self, user_name, amount):
        try:
            user = [user for user in self.users if user['name'] == user_name][0]
            user['balance'] = user['balance'] + amount
            self.send_email(user_name, 'processed credit transaction')
        except:
            print("user not found")

    def user_debit(self, user_name, amount):
        try:
            user = [user for user in self.users if user['name'] == user_name][0]
            user['balance'] = user['balance'] - amount
            self.send_email(user_name, 'processed debit transaction')
        except:
            print("user not found")

    def send_email(self, user_name, message):
        try:
            user = [user for user in self.users if user['name'] == user_name][0]
            email_address = user['email']
            balance = user['balance']
            message = message + "\nyour current balance is {}".format(balance)
            email_sender(email_address, message)
        except:
            print("user not found")
