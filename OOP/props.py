class Robot:
	def __init__(self):
		self.__name = ""

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, x):
		self.__name = x


class Car:	
	def __init__(self, model=None):
		self.__set_model(model)

	def __set_model(self, model):
		self.__model = model
	
	def __get_model(self):
		return self.__model

	model = property(__get_model, __set_model)


x = Robot()
x.name = "apo"
print(x.name)

c = Car()
c.model = "Mercedes"
print(c.model)
