class School:
	def __init__(self, name):
		self.name = name
		self.roster = {}

	def add_student(self, name, grade):
		self.roster[str(grade)] = self.roster.get(str(grade), [])
		self.roster[str(grade)].append(name)

	def grade(self, grade):
		return self.roster[str(grade)]

	def sort_roster(self):
		sorted_roster = {}
		for key in self.roster.keys():
			sorted_roster[key] = sorted(self.roster[key])
		return sorted_roster