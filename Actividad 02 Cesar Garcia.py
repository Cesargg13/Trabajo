username = input('Por favor introduce tu nombre: ')
print( f'Hola, {username}')
s_age = input('Age:')
age = int(s_age)
s_height  = input('Height:')
height = float(s_height)
print(f'Tienes {age} años y mides {height} M.')
gender=None
email=None


print("Ahora te hare algunas preguntas.")
You_gender=input('¿cual es tu genero? (m or f)?')
if(You_gender!= ''):
	if You_gender== 'm':
		gender='Masculino'
		Number=Number+1
	elif You_gender=='f':
		gender='Femenino'
		Number=Number+1
	else:
		print(f'({You_gender}) tu genero no existe en mi base ')

You_email=input('¿cual es tu email?')
if You_email != '':
	Number=Number+1
	email=You_email
