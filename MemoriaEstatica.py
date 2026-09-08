def main():
    
    calificaciones = [0] * 5

    for i in range(5):
        entrada = input(f"Captura la calificación {i}: ")
        calificaciones[i] = int(entrada)


    print(f"Calificaciones: {calificaciones}")

if __name__ == "__main__":
    main()