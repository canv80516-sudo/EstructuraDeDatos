import tkinter as tk

class Pila:
  def __init__(self, capacidad=None):
    self._datos = []
    self._capacidad = capacidad

  def push(self, valor):
    if self._capacidad is not None and len(self._datos) >= self._capacidad:
      raise OverflowError("Pila llena")
    self._datos.append(valor)

  def pop(self):
    if not self._datos:
      raise IndexError("Pila vacia")
    return self._datos.pop()

  def peek(self):
    if not self._datos:
      raise IndexError("Pila vacia")
    return self._datos[-1]

  def esta_vacia(self):
    return len(self._datos) == 0

 
  def esta_llena(self):
    return self._capacidad is not None and len(self._datos) >= self._capacidad

  def tamano(self):
    return len(self._datos)

  def vaciar(self):
    self._datos.clear()

  def elementos(self):
    return list(self._datos) 

# INTERFAZ GRÁFICA
class VisorPila:
  ANCHO, ALTO = 180, 44        
  X0, Y_BASE = 60, 430           
  COLORES = ["#4ea8de", "#80ed99", "#ffd166", "#ef8354",
             "#c77dff", "#06d6a0", "#f78fb3", "#9bc4e2"]

  def __init__(self, root, capacidad=8):
    self.root = root
    root.title("Pila (LIFO) - Visualizador")
    self.pila = Pila(capacidad)
    self.ocupado = False                     

    self.canvas = tk.Canvas(root, width=320, height=470, bg="white")
    self.canvas.grid(row=0, column=0, padx=10, pady=10)

    panel = tk.Frame(root)
    panel.grid(row=0, column=1, sticky="n", padx=10, pady=10)

    tk.Label(panel, text="Valor:").pack(anchor="w")
    self.entrada = tk.Entry(panel, width=18, font=("Arial", 12))
    self.entrada.pack(anchor="w", pady=4)
    self.entrada.bind("<Return>", lambda e: self.push())
    self.entrada.focus()

    fila = tk.Frame(panel)
    fila.pack(anchor="w")
    for texto, cmd in [("Push", self.push), ("Pop", self.pop),
                       ("Peek", self.peek), ("Vaciar", self.vaciar)]:
      tk.Button(fila, text=texto, width=8, command=cmd).pack(side="left", padx=2)

    self.info = tk.Label(panel, font=("Consolas", 10), justify="left")
    self.info.pack(anchor="w", pady=8)

    tk.Label(panel, text="Registro:").pack(anchor="w")
    self.registro = tk.Text(panel, width=46, height=15, font=("Consolas", 9),
                            state="disabled", bg="#f4f4f4")
    self.registro.pack()
    self.registro.tag_config("ok", foreground="#0b6e4f")
    self.registro.tag_config("error", foreground="#c1121f")

    self.log("Escribe un valor y pulsa Push.")
    self.dibujar()

  #botones
  def push(self):
    if self.ocupado:
      return
    valor = self.entrada.get().strip()[:12]
    if not valor:
      return self.log("Escribe un valor primero.", "error")

    i = self.pila.tamano()                    

    def terminar():
      try:
        self.pila.push(valor)                  
      except OverflowError as e:
        self.log(f"push({valor}) -> OverflowError: {e}", "error")
      else:
        self.log(f"push({valor})  -> tamaño {self.pila.tamano()}", "ok")
      self.entrada.delete(0, "end")
      self.dibujar()
      self.ocupado = False

    if self.pila.esta_llena():                
      terminar()
      return
    self.ocupado = True
    self.animar(valor, i, 5, self.y_slot(i), terminar)

  def pop(self):
    if self.ocupado:
      return
    i = self.pila.tamano() - 1
    try:
      valor = self.pila.pop()
    except IndexError as e:
      return self.log(f"pop() -> IndexError: {e}", "error")

    def terminar():
      self.log(f"pop()  -> {valor}  (tamaño {self.pila.tamano()})", "ok")
      self.ocupado = False

    self.dibujar()                             
    self.ocupado = True
    self.animar(valor, i, self.y_slot(i), -self.ALTO, terminar)

  def peek(self):
    if self.ocupado:
      return
    try:
      valor = self.pila.peek()
    except IndexError as e:
      return self.log(f"peek() -> IndexError: {e}", "error")
    self.log(f"peek() -> {valor}  (no se elimina)", "ok")
    self.dibujar(resaltar=True)
    self.root.after(900, self.dibujar)

  def vaciar(self):
    if not self.ocupado:
      self.pila.vaciar()
      self.log("vaciar()", "ok")
      self.dibujar()

  # dibujo
  def y_slot(self, i):
    return self.Y_BASE - (i + 1) * self.ALTO   

  def bloque(self, valor, i, y, borde=2, color_borde="black"):
    x0, x1 = self.X0, self.X0 + self.ANCHO
    r = self.canvas.create_rectangle(x0, y, x1, y + self.ALTO - 4,
                                     fill=self.COLORES[i % len(self.COLORES)],
                                     outline=color_borde, width=borde)
    t = self.canvas.create_text((x0 + x1) // 2, y + self.ALTO // 2 - 2,
                                text=valor, font=("Arial", 14, "bold"))
    return r, t

  def animar(self, valor, i, y, y_fin, al_terminar):
    r, t = self.bloque(valor, i, y)
    paso = 14 if y_fin > y else -14

    def mover(y_act):
      nuevo = y_act + paso
      if (paso > 0 and nuevo >= y_fin) or (paso < 0 and nuevo <= y_fin):
        self.canvas.delete(r, t)
        return al_terminar()
      self.canvas.move(r, 0, paso)
      self.canvas.move(t, 0, paso)
      self.root.after(15, lambda: mover(nuevo))

    mover(y)

  def dibujar(self, resaltar=False):
    c = self.canvas
    c.delete("all")
    elementos = self.pila.elementos()
    der = self.X0 + self.ANCHO + 6
    izq = self.X0 - 6
    alto_total = self.pila._capacidad * self.ALTO
    c.create_line(izq, self.Y_BASE - alto_total - 8, izq, self.Y_BASE + 4,
                  der, self.Y_BASE + 4, der, self.Y_BASE - alto_total - 8,
                  width=4)                     # contenedor en "U"

    for i, valor in enumerate(elementos):
      es_tope = i == len(elementos) - 1
      y = self.y_slot(i)
      if es_tope:
        self.bloque(valor, i, y, 4, "#c1121f" if resaltar else "black")
        c.create_text(der + 8, y + self.ALTO // 2 - 2, text="← TOPE", anchor="w",
                      fill="#c1121f", font=("Arial", 10, "bold"))
      else:
        self.bloque(valor, i, y)

    if not elementos:
      c.create_text((izq + der) // 2, self.Y_BASE - 30, text="(pila vacía)",
                    fill="gray", font=("Arial", 12, "italic"))

    tope = elementos[-1] if elementos else "—"
    self.info.config(text=f"tamano()      = {len(elementos)}\n"
                          f"esta_vacia()  = {self.pila.esta_vacia()}\n"
                          f"tope          = {tope}")

  def log(self, msg, etiqueta=None):
    self.registro.config(state="normal")
    self.registro.insert("end", msg + "\n", etiqueta)
    self.registro.see("end")
    self.registro.config(state="disabled")


if __name__ == "__main__":
  ventana = tk.Tk()
  VisorPila(ventana)
  ventana.mainloop()
