def addup():
	l =[]
	while True:
		n = raw_input('> ')
		if n =='quit':
			break
		l.append(int(n))
	return l 

def normalize(n):
	print 'not yet implemented'

def factorial(number):
	if type(number) is str:
		number = eval(number)
	product = 1
	for i in range(number):
		product = product * (i+1)
	return product
