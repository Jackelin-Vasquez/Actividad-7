
def menu():
    print("1.Ingresar una lista de n números reales y mostrar.")
    print("2.Calcular el area y perimetro de un rectangulo.")
    print("3.Vereficar si un número es primo")
    print("4.Calcular el promedio de calificaciones")
    print("5.Ingresar una lista.")
    print("6.Simular una calculadora de operaiones")
    print("7.Salir del programa")

def sub_menu1():
    print("1.Suma total.\n2.Promedio.\n3.Cantidad de positivos, negativos y ceros.\n4.Cuantos son multiplos de 3.")

def opcion_uno():
    cantidad=int(input("Ingrese cantidad de números:"))

    suma=0
    lista_numeros=[]
    cantidad_num=0
    negativo=0
    positivo=0
    ceros=0
    multiplo_cuatro=1

    for i in range(cantidad):
        numero= int(input(f"Ingrese numero {i+1}"))
        suma += numero
        lista_numeros.append(numero)
        cantidad_num +=1

        if numero < 0:
            negativo +=1
        if numero >0:
            positivo +=1
        if numero ==0:
            ceros+=1
        if numero %4==0:
            multiplo_cuatro+=1
    return suma,lista_numeros,cantidad_num,negativo,positivo,ceros,multiplo_cuatro

def promedio(suma, cantidad_num):
        return suma / cantidad_num

def menu_opcion4():
    print("1.Cuantas son mayores  o iguales a 85.\n2.Cuantas estan en zona de riesgo(menor a 60.")

def menu_opcion5():
    print("1.El númeor mayor.\n2.El número menor.\n3.Cuantos se repiten")

while True:
    menu()
    opcion=input("Seleccione una opcion:")

    match opcion:
        case "1":
            resultado = opcion_uno()
            print("---MENÚ---")
            sub_menu1()
            sub_opcion=input("Seleccione una opcion:")
            while True:
                match sub_opcion:
                    case "1":
                        print(f"La suma de los número es:{resultado[0]}")
                    case "2":
                        print(f"El promedio es:{promedio(resultado[0],resultado[2])}")
