class ServerMock:
    accounts = [
        {"cardData": "abc", "pin": 1234, "money": 1000, "accountNumber": 1},
        {"cardData": "def", "pin": 1234, "money": 2000, "accountNumber": 2}
    ]

    def __init__(self):
        pass
    
    def validate(self, accountData):
        return not not self.get_account(accountData)

    def deposit(self, value, accountData):
        account = self.get_account(accountData)
        if account:
            account["money"] += value
    
    def withdraw(self, value, accountData):
        account = self.get_account(accountData)
        if account:
            if account["money"] >= value:
                account["money"] -= value
    
    def get_money_amount(self, accountData):
        account = self.get_account(accountData)
        if account:
            return account["money"]
    
    def transfer(self, value, accountData, receiver):
        account = self.get_account(accountData)
        for a in self.account:
            if a["accountNumber"] == receiver:
                receiverAccount = a
        if account and receiverAccount and account["money"] >= value:
            account["money"] -= value
            receiverAccount["money"] += value

    
    def get_account(self, accountData, notAuth = False):
        for a in self.accounts:
            if a["cardData"] == accountData["cardData"]:
                if notAuth or a["pin"] == accountData["pin"]:
                    return a
                else:
                    return None
        return None

server = ServerMock()
                