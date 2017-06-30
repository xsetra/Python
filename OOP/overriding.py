class Person:
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age
	
	def __str__(self):
		return self.firstname + " " + self.lastname + " , " + str(self.age)
	
	
class Employee(Person):
	def __init__(self, first, last, age, staffnum):
		super().__init__(first, last, age)
		self.staffnumber = staffnum

	def __str__(self):
		return super().__str__() + " , " + str(self.staffnumber)


if __name__ == "__main__":
	x = Person("Abdullah", "Caliskan", 20)
	y = Employee("Guido", "Van Rossum", 50, 1)
	print(x)
	print(y)
