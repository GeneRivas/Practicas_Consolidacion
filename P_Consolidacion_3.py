Nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
Magos = ['Harry Houdini', 'David Blaine', 'Teller']
Cientificos = ['Newton', 'Hawking', 'Einstein']
Otros = [ otros for otros in Nombres 
		if otros not in Magos and otros not in Cientificos]

def Hacer_Grandioso():
   for grandiosos in Magos:
    print(f'El gran {grandiosos}')

def Imprimir_Nombres():
   for todos in Nombres:
    print(todos)
    
print('\n***********TODOS LOS NOMBRES***********\n')
Imprimir_Nombres()       
print('\n***********MAGOS GRANDIOSOS***********\n')
Hacer_Grandioso() 
print('\n***********CIENTIFICOS***********\n')
for names in Cientificos:
  print(names)    
print('\n***********LOS RESTANTES***********\n')
for names in Otros:
  print(names) 















