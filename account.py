class AuthData:
    def __init__(self, card_data, pin):
        self.card_data = card_data
        self.pin = pin

class Account:
    def __init__(self, card_data, pin, money, number):
        self.card_data = card_data
        self.pin = pin
        self.money = money
        self.number = number