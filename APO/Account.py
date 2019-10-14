class Account:
	def __init__(self, id, balance=0,):
		self.id = id
		self.balance = balance

	def getId(self):
		return self.id

	def getBalance(self):
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount
