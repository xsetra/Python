class Person:
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age

	def get_names(self):
		return self.firstname + " " + self.lastname

	def get_names(self, age=None):
		return self.firstname + " " + self.lastname + " , " + str(self.age)


""" Python overloading işlemini zaten yapıyor diyebiliriz. Function family olusturuyor
Yani int, double, float halleri için zaten metodlar var.
"""
