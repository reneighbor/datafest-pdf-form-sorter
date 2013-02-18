class DocType(object):

	def __init__(self, name, strings_to_match):
		self.name = name
		self.strings_to_match = strings_to_match
		self.matching_files = {}

	def collect_matches(self, all_files):
		for file_name, file_text in all_files.iteritems():
			self.identify_file_match(file_name, file_text)

	def identify_file_match(self, filename, filetext):
		matches = 0
		for string in self.strings_to_match:
			if string in filetext:
				matches += 1
		if matches > 1:
			percent_match = float(matches)/len(self.strings_to_match)
			self.matching_files[filename] = float(matches)/len(self.strings_to_match)