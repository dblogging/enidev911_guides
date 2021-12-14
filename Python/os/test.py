from organizar_ficheros import organizer
import os



user_path = os.getenv('userprofile')
path = os.path.join(user_path, 'Downloads')
organizer(path)

# import os 

current_path = os.getcwd()
user_path = os.getenv('userprofile')

folders = {'Desktop': 'Escritorio', 
		   'Documents': 'Mis documentos', 
		   'Pictures' : 'Imágines'}

dir_folder = list(folders.keys())


print('Te encuentras actualmente en: \n'+current_path)
print()
print('Selecciona la carpeta a organizar:\n')
i = 1
for key, value in folders.items():
	print(' '*5 + '+------------------+')
	print(' '*5 + '|{}. {:<14} {}'.format(i, value, '|'))
	print(' '*5 + '+------------------+')
	i += 1

opt =int(input('\nIngrese el número de la opción:\n'))

if opt == 1:
	new_path = os.path.join(user_path, dir_folder[0])
	os.chdir(new_path)
	#print("Has cambiado de carpeta ahora estás en '{}'".format(folders['Desktop']))

elif opt == 2:
	new_path = os.path.join(user_path, dir_folder[1])
	os.chdir(new_path)
	print(os.getcwd())
	print("Has cambiado de carpeta ahora estás en '{}'".format(folders['Documents']))



	os.chdir('')

print(os.path.basename(path))
print('Cambiar a :')

print(os.listdir(user_path))

for i in os.listdir(user_path):
	print(i)
	if i ==
path = os.system('dir /b')
