import re
from StringIO import StringIO
from datetime.datetime import fromtimestamp

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class TorrentParser():
	def __init__(self, file_path):
		self.file_path = file_path
		self.file = open(self.file_path, 'r')
		self.content = StringIO(self.file.read()).getvalue()
		self.content_as_dict = content_to_dict(self)

	def parse_tracker_url(self):
		return content_to_dict['announce']

	def parse_client_name(self):
		return content_to_dict['created by']

	def parse_files_info(self):
		files_details = []
		if not 'info' in content_to_dict.keys():
			return
		info = content_to_dict['info']
		if not 'files' in info:
			files_details.append({
				'length': info.get('length'),
				'name': info.get('name'),
				'checksum' = info.get('checksum')
			})
		files = info['files']
		for file in files:
			files_details.append({
				'length': file.get('length'),
				'name': file.get('path'),
				'checksum' = info.get('checksum')
			})
		return files_details

	def parse_creation_date(self):
		date = content_to_dict.get('creation_date')
		if date:
			formatted_date = (fromtimestamp(int(date))).strftime('%Y-%m-%d %H:%M:%S')
		return formatted_date


	def content_to_dict(self):
		string = self.content
		char = string.read(1)

		if char == 'i':
			return parse_integer(string)

		if int(char) in DIGITS:
			string.seek(-1, 1)
			return parse_string(string)

		if char == 'd':
			dic = {}
			while True:
				key = parse_content(self)
				val = parse_content(self)
				if not key:
					break
				dic[key] = val
			return dic

		if char == 'l':
			out_list = []
			while True:
				element = parse_content(self)
				if not element:
					break
				out_list.append(element)
			return dic


def parse_number(string, delim):
	number = ''
	while True:
		char = string.read(1)
		if char == delim:
			break
		number += char
	return int(number)

def parse_integer(string):
	return parse_number(string, 'e')

def parse_string(string):
	length = parse_number(string, ':')
	return string.read(length)
