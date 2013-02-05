class DocType(object):

	def __init__(self, name, strings_to_match):
		self.name = name
		self.strings_to_match = strings_to_match
		self.matching_files = []

	def identify_file_match(self, filename, filetext, percent_match):
		matches = 0
		for string in self.strings_to_match:
			if string in filetext:
				matches += 1
		if matches > (percent_match * len(self.strings_to_match)):
			if filename not in self.matching_files:
				self.matching_files.append(filename)
		