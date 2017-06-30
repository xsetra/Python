# -*- coding: utf-8 -*-
class Person:
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age

	def get_names(self, age=None):
		if age:
			return self.firstname + " " + self.lastname + " , " + str(self.age)
		else:
			return self.firstname + " " + self.lastname


if __name__ == "__main__":
	x = Person("Abdullah", "Caliskan", 20)
	print(x.get_names())
	print(x.get_names(1))

""" 
#  overloading işlemini zaten yapıyor diyebiliriz. Function family olusturuyor
# Yani int, double, float halleri için zaten metodlar var.
#1 argümanlı bir metod ve argümansız çalışacak metotlar yapacaksanız;
#argümanı isteğe bağlı hale getirmelisiniz. yada *args kullanın.
"""
