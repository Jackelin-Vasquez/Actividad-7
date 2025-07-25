def menu():
    print("1.Ingresar una lista de n números reales y mostrar.\n2.Calcular el area y perimetro de un rectangulo.")
    print("3.Vereficar si un número es primo.\n4.Calcular el promedio de calificaciones")
    print("5.Ingresar una lista.\n6.Simular una calculadora de operaiones\n7.Salir del programa")

def sub_menu1():
    print("1.Suma total.\n2.Promedio.\n3.Cantidad de positivos, negativos y ceros.\n4.Cuantos son multiplos de 3.\n5.Slir del menú")

def pedir_numeros(cantidad):
    numeros=[]
    for i in range(cantidad):
        num= int(input(f"Ingrese numero{i+1}"))
        numeros.append(num)
    return numeros

def sumar_lista(lista):
    suma= 0
    for n in lista:
        suma += n
    return suma
def contar_positivos_negativos(lista):
    positivo= negativo = ceros =0
    for n in lista:
        if n < 0:
            negativo +=1
        if n >0:
            positivo +=1
        if n==0:
            ceros+=1
    return negativo,positivo,ceros

def multiplo_tres(lista):
   contador=0
   for n in lista:
       if n% 3==0:
           contador +=1
   return contador

def opcion_uno():
    cantidad= int(input("Cuantos numeros dese ingresar?"))
    numeros= pedir_numeros()
    suma= sumar_lista(numeros)
    positivos, negativos, ceros = contar_positivos_negativos(numeros)
    multiplos_tres= multiplo_tres(numeros)
    return numeros, suma, positivos,negativos,ceros,multiplos_tres

def promedio(suma, cantidad_num):
        return suma / cantidad_num

def calcular_area(base1,altura1):
    return base1*altura1

def calcular_perimetro(base2,altura2):
    return(2*base2) + (2*altura2)

def calcular_primo(num):
    if num <=1:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2,num):
            if i %2==0:
                return False
        return True

def opcion4():
     cantidad= int(input("Ingrese cantidad de calificaciones a ingresar:"))
     mayor_igual_85=0
     menor_60=0
     suma=0

     for i in range(cantidad):
         calificacion= float(input(f"Ingrese calificacion no.{i+1}"))
         if calificacion < 0 or calificacion > 100:
             print("Califacacion no valida")
         else:
             suma+=calificacion
             if calificacion >=85:
                 mayor_igual_85 += 1
             if calificacion < 60:
                menor_60+=1
     return cantidad, mayor_igual_85, menor_60, suma

def encontrar_mayor_menor():
    cantidad=int(input("Ingrese cantidad de números a agregar:"))
    numeros=[]
    repetidos=[]
    num_rep=[]

    for x in range(cantidad):
        while True:
            numero1=int(input(f"Ingrese número {x +1}"))
            numeros.append(numero1)
            break
    mayor= menor =numeros[0]

    for num in numeros[1:]:
        if num > mayor:
            mayor= num
        if num < menor:
            menor =num

    for n in numeros:
        if n not in num_rep:
            num_rep.append(n)
        else:
            repetidos.append((n))

    return mayor, menor, repetidos

def suma(num1,num2):
    return num1 + num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

def menu_calculadora():
    print("1.Suma.\n2.Resta.\n3.Multiplicación\n4.Division\n5.Salir")

while True:
    menu()
    opcion=input("Seleccione una opcion:")

    match opcion:
        case "1":
            resultado = opcion_uno()
            while True:
                print("---MENÚ---")
                sub_menu1()
                sub_opcion= input("Seleccione una opcion:")
                match sub_opcion:
                    case "1":
                         print(f"La suma de los número es:{resultado[1]}")
                    case "2":
                        print(f"El promedio es:{promedio(resultado[1],len(resultado[0]))}")
                    case "3":
                         print(f"hay {resultado[3]} negativos, {resultado[2]} positivos y {resultado[4]} numeros que son ceros.")
                    case "4":
                        print(f"hay{resultado[5]} numero/s que son multiplo/s de 3.")
                    case "5":
                        print("Saliendo del menú...")
                        break
                    case _:
                        print("Opcion no valida...")
        case "2":
            base= float(input("Ingrese longitud de base:"))
            altura= float(input("Ingrese altura:"))
            print(f"El area del rectangulo es:{calcular_area(base,altura)}")
            print(f"El perimetro del rectangulo es:{calcular_perimetro(base,altura)}")
        case"3":
            numero= int(input("Ingrese número:"))
            primo= calcular_primo(numero)
            if primo:
                print(f"{numero}  es primo")
            else:
                print(f"{numero} no es primo")
        case "4":
            resultado4= opcion4()
            print(f"El promedio de notas es: {promedio(resultado4[3],resultado4[0])}")
            print(f"Hay {resultado4[1]} nota/s que son mayor/es que 85\n Hay {resultado4[2]} nota/s que estan en zona de riesgo (menor qeu 60)")

        case "5":
            resultado= encontrar_mayor_menor()
            print(f"El número mayor es{resultado[0]}, el número menor es {resultado[1]} y se repiten {resultado[2]}")

        case "6":
            numero_1= float(input("Ingrese numero 1"))
            numero_2= float(input("Ingrese número 2:"))
            while True:
                menu_calculadora()
                opcion6= input("Ingrese una opcion:")

                match opcion6:
                    case "1":
                        print(f"La suma de los números es:\n {suma(numero_1,numero_2)}")
                    case "2":
                        print(f"La resta de los número es:{resta(numero_1,numero_2)}")
                    case "3":
                        print(f"la multiplicación de los números es: {multiplicacion(numero_1,numero_2)}")
                    case "4":
                        print(f"La división de los números es:{division(numero_1,numero_2)}")
                    case "5":
                        print("Saliendo...")
                        break
                    case _:
                        print("Opcion no valida")
        case "7":
            print("Saliendo del programa....")
            break
        case _:
            print("Opción no valida...")