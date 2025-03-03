def calcular_suma(N):
    suma = 0 
    resultado_individual = ""
    for i in range(1,N + 1):
        resultado_individual += str(i ** (i+1))
        if i < N:
            resultado_individual += "+"
        suma += i ** (i+1)
    return suma, resultado_individual

def main():
    N= int(input("Ingrese el numero total de terminos de la serie a calcular: "))
    resultado, resultado_individual = calcular_suma(N)
    resultado_final = resultado /N
    print("la suma de la serie es: ", resultado_individual)
    print("El resultado de la suma es: ", resultado)
    print("El resultado final es: ", resultado_final) 
    
if __name__ == "__main__":
    main()           