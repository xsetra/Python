"""

name : Attribute is public. Everyone can access.
_name : is Protected. You can access it from within class and subclass.
__name : is Private. only from class.

"""

# Data encapsulation demek, veriye erişimin sadece get ve set gibi metodlar üzerinden yapılması anlamına geliyor.
# Information Hiding demek, veriye erişimin sınırlandırılması. 

class Robot:
	def __init__(self, name=None, build_year=None):
		self.__name = name
		self.__build_year = build_year

	def say_hi(self):
		if self.__name:
			print("Hi, I am " + self.__name + "!")
		else:
			print("Hi, I am a Robot without name")

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_build_year(self, build_year):
		self.__build_year = build_year

	def get_build_year(self):
		return self.__build_year

	def __repr__(self):
		return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

	def __str__(self):
		return "About this robot\n\tName: " + self.__name + "\n\tBuilded: " + str(self.__build_year)

	
if __name__ == "__main__":
	x = Robot("First", 2000)
	y = Robot("Second", 2017)
	for robots in [x,y]:
		print(str(robots))
