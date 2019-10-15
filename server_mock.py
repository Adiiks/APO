from account import *

class ServerMock:
    accounts = [
        Account("abc", 1234, 1000, 1),
        Account("def", 1234, 2000, 2)
    ]

    def __init__(self):
        pass
    
    def validate(self, auth_data):
        return not not self.get_account_by_auth_data(auth_data)

    def deposit(self, value, auth_data):
        account = self.get_account_by_auth_data(auth_data)
        if account:
            account.money += value
            return True
        return False
    
    def withdraw(self, value, auth_data):
        account = self.get_account_by_auth_data(auth_data)
        if account:
            if account.money >= value:
                account.money -= value
                return True
        return False
    
    def get_money_amount(self, auth_data):
        account = self.get_account_by_auth_data(auth_data)
        if account:
            return account.money
        return False
    
    def transfer(self, value, auth_data, receiver):
        account = self.get_account_by_auth_data(auth_data)
        receiverAccount = self.get_account_by_number(receiver)
        if account and receiverAccount and account.money >= value:
            account.money -= value
            receiverAccount.money += value
            return True
        return False

    #private
    def get_account_by_auth_data(self, auth_data):
        for a in self.accounts:
            if a.card_data == auth_data.card_data and a.pin == auth_data.pin:
                return a
        return None
    
    def get_account_by_number(self, number):
        for a in self.accounts:
            if a.number == number:
                return a
        return None

server = ServerMock()
                