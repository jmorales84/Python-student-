import datetime

def xTabla():
    x= int(input("Ingresa el numero de la tabla que deseas"))
    a=10
    while a>=1: #----While----
        print (f"{x} * {a} = {x*a}")
        a-=1

def numeros():
    n1=int(input("Ingresa el primer numero"))
    if n1 % 2 == 0:
        print ("El numero es par")
    else: 
        print("El numero es Impar")

def IfAnidado():
    n3=int(input("Ingresa tu Calificacion ---->"))
    if (n3==100) :
        print("Excelente, Felicidades")
    elif (n3 <= 99 and n3 >= 90):
        print("Muy bien")
    elif (n3<=89 and n3>=80):
        print("Bien")
    elif (n3<= 79 and n3>=70):
        print("Alumno Regular")
    else: 
        print("Puedes mejorar")

def Formula():
    n1 = int(input("Dame un numero"))
    a=1
    acu=0
    while a<=n1:
         p=a+1
         r=pow (a,p)
         acu=acu+r
         res=acu/n1
         a+=1
         print ("El resultado final es ---->", res)

def matricula():
    import datetime
    fecha = datetime.datetime.now()
    print (fecha)
    año= datetime.datetime.strftime(fecha, "%Y")
    periodo= int(input("ingresa el periodo en que entraste 1= julio o 2 = septiembre"))
    if (periodo==1 or periodo==2):
        print (periodo)
        carrera=int(input("ingresa el numero de la carrera elegida \n"
            "1.- ING. INDUSTRIAL \n"
            "2.- ING TIC'S \n"
            "3.- ING SISTEMAS \n"
            "4.- ING.MECATRONICA \n"
            "5.- ING CIVIL \n"
            "6.- ING. QUIMICA \n"
            "7.- LIC. ADMINISTRACION \n"
            "8.- ING.LOGISTICA \n"))
    if (carrera==1 or carrera==2 or carrera==3 or carrera==4 or carrera==5 or carrera==6 or carrera==7 or carrera==8):
        print (carrera)

        numeroIns =int (input("ingresa que numero de alumno eres segun tu inscripcion"))
        if (numeroIns<10):
           concat= str (año) + str (periodo) + str (carrera) + str("00") + str(numeroIns)
           print(concat)
        if (numeroIns>10 and numeroIns<100):
            concat = str(año) + str(periodo) + str(carrera) + str("0") + str (numeroIns)
            print (concat)
        if (numeroIns>=100 and numeroIns<1000):
            concat= str(año) + str(periodo) + str(carrera) + str(numeroIns)
            print(concat)
        else:
            print ("ingresa nuevamente el numero de carrera")
    else:
         print ("No son correctos tus datos")
         print ("ingresa nuevamente el numero del periodo")




while True:
    print("Ingresa el numero de lo que quieres reaizar")
    print("{1} X tabla")
    print("{2} Numero Par o Numero Impar")
    print("{3} If Anidado")
    print("{4} Formula")
    print("{5} Numero de Control (MATRICULA)")
    print("{x} Pulsa para salir")
    num=(input("Ingresa el numero del codigo que deseas"))
    if (num == "x"):
        break
    else:
        match num:
            case "1":
                xTabla()
            case "2":
                numeros()
            case"3":
                IfAnidado()
            case"4":
                Formula()
            case"5":
                matricula()
            case _:
                break
            