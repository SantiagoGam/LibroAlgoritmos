#RECORDATORIO
#Esto SOLO FUNCIONA en listas ordenadas

#Definir variables
Ingreso = 0
Buscar = 0


#Lista Vacia
Numeros=[]

#Definir funciones
def BuscarNumero(Numeros, Elemento):
    Menor = 0
    Mayor = len(Numeros)-1

    while Menor <= Mayor:
        Medio = (Menor + Mayor)//2 
        Estimado = Numeros[Medio]

        if Estimado == Elemento:
            return Medio
        if Estimado > Elemento:
            Mayor = Medio-1
        else:
            Menor = Medio+1
    return None

#Definir programa
print("BIENVENIDO A LA BUSQUEDA BINARIA")
input("Presione cualquier tecla para continuar...")

#Ingreso de datos
while Ingreso !=999 :
    print('Para salir ingrese "999"')
    Ingreso=int(input("Ingrese un numero: "))
    Numeros.append(Ingreso)
    
    
Numeros.sort()

#Consulta de datos
print("De los numeros ingresados anteriormente...")
print(Numeros)
Buscar = int(input("¿Que numero desea buscar?: "))
print(BuscarNumero(Numeros, Buscar))


