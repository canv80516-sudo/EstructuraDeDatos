class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None


class ListaSimple:
    def __init__(self):
        self.p = None

    def crea_inicio(self):
        self.p = Nodo(input("Ingrese el dato: "))
        res = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))
        while res == 1:
            q = Nodo(input("Ingrese el dato: "))
            q.liga = self.p
            self.p = q
            res = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))

    def inserta_inicio(self, dato):
        q = Nodo(dato)
        q.liga = self.p
        self.p = q

    def inserta_final(self, dato):
        q = Nodo(dato)
        if self.p is None:
            self.p = q
        else:
            actual = self.p
            while actual.liga is not None:
                actual = actual.liga
            actual.liga = q

    def inserta_despues(self, ref, dato):
        q = self.p
        while q is not None and q.info != ref:
            q = q.liga
        if q is None:
            print("El dato de referencia no se encontró")
        else:
            nuevo = Nodo(dato)
            nuevo.liga = q.liga
            q.liga = nuevo

    def inserta_antes(self, ref, dato):
        if self.p is None:
            print("La lista está vacía")
        elif self.p.info == ref:
            self.inserta_inicio(dato)
        else:
            ant, q = self.p, self.p.liga
            while q is not None and q.info != ref:
                ant, q = q, q.liga
            if q is None:
                print("El dato de referencia no se encontró")
            else:
                nuevo = Nodo(dato)
                nuevo.liga = q
                ant.liga = nuevo

    def elimina_inicio(self):
        if self.p is None:
            print("La lista está vacía")
        else:
            self.p = self.p.liga

    def elimina_final(self):
        if self.p is None:
            print("La lista está vacía")
        elif self.p.liga is None:
            self.p = None
        else:
            ant, q = self.p, self.p.liga
            while q.liga is not None:
                ant, q = q, q.liga
            ant.liga = None

    def elimina_dato(self, dato):
        if self.p is None:
            print("La lista está vacía")
        elif self.p.info == dato:
            self.p = self.p.liga
        else:
            ant, q = self.p, self.p.liga
            while q is not None and q.info != dato:
                ant, q = q, q.liga
            if q is None:
                print("El dato no se encontró")
            else:
                ant.liga = q.liga

    def elimina_anterior(self, x):
        if self.p is None:
            print("La lista está vacía")
        elif self.p.info == x:
            print("El dato es el primero, no tiene nodo anterior")
        else:
            ant2, ant, q = None, self.p, self.p.liga   
            while q is not None and q.info != x:
                ant2, ant, q = ant, q, q.liga
            if q is None:
                print("El dato no se encontró")
            elif ant2 is None:                        
                self.p = q
            else:
                ant2.liga = q

    def elimina_posterior(self, x):
        q = self.p
        while q is not None and q.info != x:
            q = q.liga
        if q is None:
            print("El dato no se encontró")
        elif q.liga is None:
            print("El dato es el último, no tiene nodo posterior")
        else:
            q.liga = q.liga.liga

    def elimina_todos(self):
        self.p = None

    def busca_desordenada(self, x):
        q = self.p                                    
        while q is not None and q.info != x:         
            q = q.liga                               
        return q is not None                          
    def busca_ordenada(self, x):
        q = self.p                                  
        while q is not None and q.info < x:        
            q = q.liga
        return q is not None and q.info == x         

    def busca_recursiva(self, x):
        return self._busca_rec(self.p, x)

    def _busca_rec(self, p, x):
        if p is not None:                            
            if p.info == x:                           
                return True
            return self._busca_rec(p.liga, x)         
        return False                                  

   
    def mostrar(self):
        actual = self.p
        while actual is not None:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("NIL")


lista = ListaSimple()
lista.crea_inicio()
lista.mostrar()

opcion = -1
while opcion != 0:
    print("\n1. Insertar  2. Eliminar  3. Mostrar  4. Buscar  0. Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        print("Insertar en: 1. Inicio  2. Final  3. Antes de un dato  4. Después de un dato")
        donde = int(input("Opción: "))
        dato = input("Dato nuevo: ")
        if donde == 1:
            lista.inserta_inicio(dato)
        elif donde == 2:
            lista.inserta_final(dato)
        elif donde == 3:
            lista.inserta_antes(input("¿Antes de cuál dato?: "), dato)
        elif donde == 4:
            lista.inserta_despues(input("¿Después de cuál dato?: "), dato)
        lista.mostrar()

    elif opcion == 2:
        print("Eliminar: 1. Primero  2. Último  3. Un dato X  4. Anterior a X  5. Posterior a X  6. Todos")
        que = int(input("Opción: "))
        if que == 1:
            lista.elimina_inicio()
        elif que == 2:
            lista.elimina_final()
        elif que == 3:
            lista.elimina_dato(input("¿Cuál dato?: "))
        elif que == 4:
            lista.elimina_anterior(input("¿Anterior a cuál dato?: "))
        elif que == 5:
            lista.elimina_posterior(input("¿Posterior a cuál dato?: "))
        elif que == 6:
            lista.elimina_todos()
        lista.mostrar()

    elif opcion == 3:
        lista.mostrar()

    elif opcion == 4:
        print("Buscar: 1. Desordenada  2. Ordenada  3. Recursiva")
        tipo = int(input("Opción: "))
        dato = input("¿Qué dato buscas?: ")
        if tipo == 1:
            hallado = lista.busca_desordenada(dato)
        elif tipo == 2:
            hallado = lista.busca_ordenada(dato)
        elif tipo == 3:
            hallado = lista.busca_recursiva(dato)
        print("El elemento sí se encuentra en la lista" if hallado
              else "El elemento no se encuentra en la lista")