from server_mock import *

class CashMachine:
    def __init__(self):
        while(True):
            accountData = None
            print("Wsuń kartę płatnicza")
            card = input(">")
            print("Podaj pin")
            pin = input(">")
            if not pin.isdigit():
                print("Nieprawidłowy pin")
                print("[ Karta się wysuwa ]")
                continue
            pin = int(pin)
            accountData = {"cardData": card, "pin": pin}
            if not server.validate(accountData):
                print("Nieprawidłowy pin lub karta płatnicza")
                print("[ Karta się wysuwa ]")
                continue
            while(True):
                print("Podan numer opcji")
                print("1. Wpłać pieniądze")
                print("2. Wypłać pieniądze")
                print("3. Zrób przelew")
                print("4. Sprawdź stan konta")
                print("5. Wyjmij kartę")
                number = input(">")
                if number == "1":
                    print("Wpłać kwote")
                    amount = input(">")
                    if not amount.isdigit():
                        print("Nieprawidłowy banknot")
                        print("[ Banknot się wysuwa ]")
                        continue
                    amount = int(amount)
                    server.deposit(amount, accountData)
                    print("Pieniądze wpłacone")
                elif number == "2":
                    print("Podaj kwotę")
                    amount = input(">")
                    if not amount.isdigit():
                        print("Nieprawidłowa kwota")
                        continue
                    amount = int(amount)
                    server.withdraw(amount, accountData)
                    print("[ Pieniądze się wysuwają ]")
                    print("Pieniądze wypłacone")
                elif number == "3":
                    print("Podaj kwotę")
                    amount = input(">")
                    if not amount.isdigit():
                        print("Nieprawidłowa kwota")
                        continue
                    amount = int(amount)
                    print("Podaj number konta")
                    accountNumber = input(">")
                    if not accountNumber.isdigit():
                        print("Nieprawidłowy number konta")
                        continue
                    accountNumber = int(accountNumber)
                    server.transfer(amount, accountData, accountNumber)
                    print("Przelew zrobiony")
                elif number == "4":
                    amount = server.get_money_amount(accountData)
                    print("Obecnie posiadasz")
                    print(amount)
                elif number == "5":
                    print("[ Karta się wysuwa ]")
                    break
                else:
                    print("Nieprawidłowy numer")

m = CashMachine()

                

    
