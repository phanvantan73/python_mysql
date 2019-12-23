class Student():

	def __init__(self, code, name, className):
		self.code = code
		self.name = name
		self.className = className

	def getCode(self):
		return self.code

	def getName(self):
		return self.name

	def getClassName(self):
		return self.className

	def getStudentInfor(self):
		print('Code: ' + self.code)
		print('Name: ' + self.name)
		print('Class: ' + self.className)
		print('-------------')
