class Person:
	def __init__(self, first=None, last=None):
		self.firstname = first
		self.lastname = last

	@property
	def name(self):
		return self.firstname + " " + self.lastname


class Employee(Person):
	def __init__(self, first=None, last=None, staffnum=None):
		# super().__init__(first, last)
		# Person.__init__(self, first, last)
		super(Employee, self).__init__(first, last)
		self.staff_number = staffnum
	
	@property
	def get_employee(self):
		return str(self.staff_number) + " - " + self.name


if __name__ == "__main__":
	x = Person("Apo", "Cal")
	y = Employee("Apo", "Cal", 1)
	print(y.get_employee)
	print(x.name)
