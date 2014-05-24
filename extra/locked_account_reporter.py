import codecs
def test_encoding(file):
	# For the files we are examining, two encodings
	# are available: UTF-8, UTF-16LE.
	# We want to determine which for a file:
	try:
		filehandle = codecs.open(file,'r','utf-8')
		filehandle = readlines()
	except UnicodeDecodeError:
		print('Not UTF-8, likely UTF-16LE encoded')
	else:
		print('File is UTF-8')
