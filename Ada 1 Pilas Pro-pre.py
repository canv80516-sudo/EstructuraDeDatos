class Pila:
    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        return self.items.pop()


def operar(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a / b


def evaluar_posfija(expresion):
    pila = Pila()
    for token in expresion.split():
        if token in "+-*/":
            b = pila.pop()
            a = pila.pop()
            pila.push(operar(a, b, token))
        else:
            pila.push(float(token))
    return pila.pop()


def evaluar_prefija(expresion):
    pila = Pila()
    for token in reversed(expresion.split()):
        if token in "+-*/":
            a = pila.pop()
            b = pila.pop()
            pila.push(operar(a, b, token))
        else:
            pila.push(float(token))
    return pila.pop()


tipo = input("¿Posfija (1) o prefija (2)? ")
expresion = input("Escribe la expresión (con espacios): ")

try:
    if tipo == "1":
        print("Resultado:", evaluar_posfija(expresion))
    else:
        print("Resultado:", evaluar_prefija(expresion))
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
except IndexError:
    print("Error: la expresión está incompleta (faltan números)")
except ValueError:
    print("Error: hay un símbolo que no es número ni operador")