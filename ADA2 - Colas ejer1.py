class Cola:

  def __init__(self):
    self.elementos = []

  def esta_vacia(self):
    return len(self.elementos) == 0

  def encolar(self, item):
    self.elementos.append(item)

  def desencolar(self):
    if not self.esta_vacia():
      return self.elementos.pop(0)
    return None

  def __str__(self):
    return str(self.elementos)


def sumar_colas(cola_a, cola_b):
  cola_resultado = Cola()

  while not cola_a.esta_vacia() and not cola_b.esta_vacia():
    valor_a = cola_a.desencolar()
    valor_b = cola_b.desencolar()

    suma = valor_a + valor_b
    cola_resultado.encolar(suma)

  return cola_resultado


if __name__ == "__main__":
  print("=SUMADOR DE COLAS INTERACTIVO=")

  cola_a = Cola()
  cola_b = Cola()


  print("\n--- Llenando la Cola A ---")
  n_a = int(
      input("¿Cuántos números deseas ingresar en la Cola A? (Ej: 5): ")
  )
  for i in range(n_a):
    num = int(input(f"Ingresa el elemento {i + 1} de la Cola A: "))
    cola_a.encolar(num)

 
  print("\n--- Llenando la Cola B ---")
  n_b = int(
      input(
          f"¿Cuántos números deseas ingresar en la Cola B? (Debe ser {n_a} para"
          " que coincidan): "
      )
  )

  
  while n_b != n_a:
    print(
        "Para sumar uno a uno, ambas colas deben tener la misma cantidad de"
        " elementos."
    )
    n_b = int(input(f"Por favor, ingresa nuevamente la cantidad para la Cola B: "))

  for i in range(n_b):
    num = int(input(f"Ingresa el elemento {i + 1} de la Cola B: "))
    cola_b.encolar(num)

 
  print("\n----------------------------------")
  print(f"Cola A ingresada:   {cola_a}")
  print(f"Cola B ingresada:   {cola_b}")

  
  cola_res = sumar_colas(cola_a, cola_b)
  print(f"Cola Resultado:     {cola_res}")
  print("----------------------------------")