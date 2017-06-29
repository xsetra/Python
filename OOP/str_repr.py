class Robot:
	def __init__(self, name=None, build_year=None):
		self.name = name
		self.build_year = build_year

	def get_name(self):
		return self.name
	
	def get_build_year(self):
		return self.build_year

	def __repr__(self):
		return "Robot('" + self.get_name() + "', " + str(self.get_build_year()) + ")"

	def __str__(self):
		return "Robot ::: \n\tName:" + self.get_name() + "\n\tBuilded:" + str(self.get_build_year())


if __name__ == "__main__":
	x = Robot(name="Abdullah", build_year=1996)
	str_x = str(x)
	print(str_x)
	print("Type of str_x : ", type(str_x))
	
	repr_x = repr(x)
	print(repr_x)
	print("Type of repr_x : ", type(repr_x))
	
