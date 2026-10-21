class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)      

    def desencolar(self):
        return self.items.pop(0)         

    def esta_vacia(self):
        return len(self.items) == 0



servicios = {
    1: "Siniestros",
    2: "Pólizas nuevas",
    3: "Pagos y renovaciones",
}


colas = {num: Cola() for num in servicios}
contadores = {num: 0 for num in servicios}

print("Servicios:")
for num, nombre in servicios.items():
    print(f"  {num} - {nombre}")
print("Comandos: C <servicio> = llega cliente | A <servicio> = atender | S = salir\n")

while True:
    comando = input("> ").strip().upper().split()

    if not comando:
        continue
    if comando[0] == "S":
        print("Sistema cerrado.")
        break

   
    if len(comando) != 2 or not comando[1].isdigit() or int(comando[1]) not in servicios:
        print("Comando inválido. Ejemplo: C 1  o  A 2")
        continue

    letra = comando[0]
    servicio = int(comando[1])

    if letra == "C":                         
        contadores[servicio] += 1
        turno = contadores[servicio]
        colas[servicio].encolar(turno)
        print(f"Tu turno es el {turno} en {servicios[servicio]}")

    elif letra == "A":                       
        if colas[servicio].esta_vacia():
            print(f"No hay clientes esperando en {servicios[servicio]}")
        else:
            turno = colas[servicio].desencolar()
            print(f"Llamando al turno {turno} de {servicios[servicio]}")

    else:
        print("Comando inválido. Usa C, A o S")