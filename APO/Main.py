from Account import *

def main():
	accounts = []
	for i in range(1000, 9999):
		account = Account(i,0)
		accounts.append(account)

	while True:

		id = int(input("\nEnter pin: "))

		while id < 1000 or id > 9999:
			id = int(input("\nInvalid Id: "))

		while True:
			print("\n1:Balance \n2:Withdraw\n3:Deposit\n4:exit")

			selection = int(input("Enter a number: "))

			for acc in accounts:
				if acc.getId() == id:
					accountObj = acc
					break

			if selection == 1:
				print(accountObj.getBalance())
				input("Press enter to back to menu")
			elif selection == 2:
				amount = float(input("\nEnter amount to withdraw: "))

				if amount < accountObj.getBalance():
					accountObj.withdraw(amount)
					print("\n Balance: " + str(accountObj.getBalance()))
					input("Press enter to back to menu")
				else:
					print("\nYour balance is less than withdraw")
					input("Press enter to back to menu")

			elif selection == 3:
				amount = float(input("\nEnter amount to deposit: "))
				accountObj.deposit(amount)
				print("\nBalance: " + str(accountObj.getBalance()))
				input("Press enter to back to menu")

			elif selection == 4:
				print("Thanks")
				exit()

			else:
				print("\nInvalid choice")
main()