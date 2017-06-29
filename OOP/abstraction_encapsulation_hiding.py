"""

Data Abstraction : Data Encapsulation + Information Hiding

Encapsulation : Veriler üzerindeki işlemlerin methodlar üzerinden yapılması
Information Hiding : Verinin direkt değiştirilememesi.

ORNEK :
Encapsulation, işlemini yapmak için 2 temel method yeterlidir.
Getter ve setter metodlarını implemente ettiğimiz zaman bu yeterlidir.

"""
class Robot:
	def __init__(self, name=None):
		self.name = name
	
	def say_hi(self):
		if self.name:
			print("Hi, I am " + self.name + "!")
		else:
			print("Hi, I am a Robot without a name")

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name


x = Robot()
x.set_name("Apo")
print(x.get_name())




