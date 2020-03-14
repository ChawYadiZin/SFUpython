def say_hello():
	print('Hello World')




say_hello()


#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b, 'is maximum')