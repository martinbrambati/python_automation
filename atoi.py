references 			= 	{'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
operations 			= 	{'-':-1,'+':1}
decimal_separator	=	'.'
k_separator			=	','

def atoi (n):
	"""Returns n as number"""
	
	#n = validate(n)

	number = 0
	i = 0
	for letter in reversed(n):
		number = operations.get(letter,1) * (number + references.get(letter,0) * 10**i) 

		if k_separator != letter:
			i += 1
		
		if decimal_separator == letter:
			 number, i = 0, 0 
		

	return number 

def validate(n):
	i 			= 0
	count_op 	= 0
	count_sep 	= 0

	for letter in n:
		is_number 			= references.get(letter,False)
		is_operation 		= operations.get(letter,False)
		is_decimal_or_k_set = letter == decimal_separator or letter == k_separator

		if (is_operation && i != 0) or (is_operation and count_op > 0) or (is_decimal_or_k_set and count_sep > 0) :
			return 0
		
		count_op += 1
		count_sep += 1
		i += 1

	return n 	

def test():
	print ( atoi('-.5') == 0 )
	print ( atoi('-0.5') == 0 )
	print ( atoi('1-') == 0 )
	print ( atoi('1-22') == 0 )
	print ( atoi('1') == 1 )
	print ( atoi('12') == 12 )
	print ( atoi('-1') == -1 )
	print ( atoi('--1') == 0 )
	print ( atoi('2.0') == 2 )
	print ( atoi('2.2') == 2 )
	print ( atoi('.5') == 0)
	print ( atoi('2,600') == 2600)
	print ( atoi('a') == 0)
	print ( atoi('+1') == 1)
	print ( atoi('+1.5') == 1)
	print ( atoi('+16,0000,00') == 0)
	print ( atoi('-16,000') == -16000)
	print ( atoi('-16,000.9900') == -16000)
	print ( atoi('--16,000.9900') == 0)
	print ( atoi('1.-') == 0)
	print ( atoi('') == 0)
	print ( atoi(',') == 0)
	print ( atoi('.') == 0)
	print ( atoi('1a2') == 0)
	
test()