# Classes are most useful for holding and accessing abstract collections of data
'''
One useful class method to override is the built-in __repr__() method,
 which is short for representation; by providing a return value in this method, 
 we can tell Python how to represent an object of our class (for instance, when using a print statement).

class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1, 2, 3)
print(my_point)
'''

'''
The bank account class you’ll create should have methods for each of the following:

    Accepting deposits
    Allowing withdrawals
    Showing the balance
    Showing the details of the account
'''
class BankAccount():
	balance = 0
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "%s's account. Balance: $%.2f" % (self.name, self.balance)

	def __show_balance__(self):
		return "$%.2f" % (self.balance)

	def deposit(self, amount):
		if amount <= 0:
			raise TypeError("Invalid amount")
			return
		else:
			print( "$%.2f" % (amount) )
			self.balance += amount
			print( self.__show_balance__() )

	def withdraw(self, amount):
		if amount > self.balance:
			raise "Not enough funds in your account"
			return
		else:
			print( "$%.2f" % (amount) )
			self.balance -= amount
			print( self.__show_balance__() )


# Instance
cuentaDeYanis = BankAccount("Yanny Granados")
print(cuentaDeYanis)

cuentaDeYanis.deposit(200000)
print(cuentaDeYanis)
cuentaDeYanis.withdraw(800)