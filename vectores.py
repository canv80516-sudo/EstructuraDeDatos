def mostrar_vectores(datos): 
    for dato in datos: 
        print(dato)

def media(datos): 
    suma = 0 
    for dato in datos: 
        suma += dato
    return suma / len(datos)

def main(): 
    pares = [2, 4, 6, 8, 10]
    impares = [1, 3, 5, 7, 9]

    mostrar_vectores(pares)
    print("Media = " + str(media(pares)))

    mostrar_vectores(impares)
    print("Media = " + str(media(impares)))

if __name__ == "__main__": 
    main() 

        
