import getpass
 
#try:
#    p = getpass.getpass('Contraseña: ')
    
#except Exception as error:
#    print('ERROR', error)
#else:
#    print('Contraseña ingresada: ', p)

#val = input("Ingresa una expresión: ")
#print(type(val))

#val = int(input("Ingresa un número: "))
#print(val)

 
user = getpass.getuser()
 
while True:
    pwd = getpass.getpass("User Name : %s " % user)
 
    if pwd == 'abcd':
        print("Welcome!!!")
        break
    else:
        print("The password you entered is incorrect.")