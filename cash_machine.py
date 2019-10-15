from server_mock import *
from account import *

class CashMachine:
    def __init__(self):
        while(True):
            auth_data = None
            print("Wsuń kartę płatnicza")
            card = input(">")
            print("Podaj pin")
            pin = input(">")
            if not pin.isdigit():
                print("Nieprawidłowy pin")
                print("[ Karta się wysuwa ]")
                continue
            pin = int(pin)
            auth_data = AuthData(card, pin)
            if not server.validate(auth_data):
                print("Nieprawidłowy pin lub karta płatnicza")
                print("[ Karta się wysuwa ]")
                continue
            while(True):
                print("Podaj numer opcji")
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
                    result = server.deposit(amount, auth_data)
                    if result:
                        print("Pieniądze wpłacone")
                    else:
                        print("Wystąpił nieoczekiwany błąd.")
                        print("[ Banknot się wysuwa ]")
                elif number == "2":
                    print("Podaj kwotę")
                    amount = input(">")
                    if not amount.isdigit():
                        print("Nieprawidłowa kwota")
                        continue
                    amount = int(amount)
                    result = server.withdraw(amount, auth_data)
                    if result:
                        print("[ Pieniądze się wysuwają ]")
                        print("Pieniądze wypłacone")
                    else:
                        print("Wystąpił nieoczekiwany błąd.")
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
                    result = server.transfer(amount, auth_data, accountNumber)
                    if result:
                        print("Przelew zrobiony")
                    else:
                        print("Wystąpił nieoczekiwany błąd.")
                elif number == "4":
                    result = server.get_money_amount(auth_data)
                    if result != False:
                        print("Obecnie posiadasz")
                        print(result)
                    else:
                        print("Wystąpił nieoczekiwany błąd.")
                elif number == "5":
                    print("[ Karta się wysuwa ]")
                    break
                else:
                    print("Nieprawidłowy numer")

m = CashMachine()

                

    
