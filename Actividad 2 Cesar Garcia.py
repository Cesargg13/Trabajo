AI_NAME = 'Alexa'
username = input('Please enter your name: ')
print( f'Hello, {username}, mi name is {AI_NAME}' )

answer = input(f'Would you like to change my name({AI_NAME})?(y/n)')
if answer == 'y':
	AI_NAME = input(f'({AI_NAME})New Name:')
print("I will ask for some data, leave it blank if you don't want to tell me.")
str_age = input('Age:')
age = int(str_age)
str_height  = input('Height:')
height = float( str_height )
Number=0
gender=None
email=None


You_gender=input('¿What is your Gender (m or f)?')
if(You_gender!= ''):
	if You_gender== 'm':
		gender='Male'
		Number=Number+1
	elif You_gender=='f':
		gender='Female'
		Number=Number+1
	else:
		print(f'({You_gender}) does not exist in my database ')

You_email=input('¿What is your E-mail?')
if You_email != '':
	Number=Number+1
	email=You_email
if Number>=2:
	answer=input( 'Can I have your phone number? (yes/no)')
	if answer=='yes':
		Number=Number+1
		phone_number = input( 'Phone number:' )
print( f'Hey {username}, You said you are {age} years old and {height}m tall.' )

