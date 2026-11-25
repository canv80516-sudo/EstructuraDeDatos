
# BUSQUEDA HASH: INVENTARIO

productos = {
    "A101": {
        "nombre": "Laptop",
        "precio": 12500,
        "stock": 5
    },
    "A102": {
        "nombre": "Mouse",
        "precio": 250,
        "stock": 15
    },
    "A103": {
        "nombre": "Teclado",
        "precio": 450,
        "stock": 10
    },
    "A104": {
        "nombre": "Monitor",
        "precio": 3200,
        "stock": 8
    },
    "A105": {
        "nombre": "Audifonos",
        "precio": 600,
        "stock": 12
    },
    "A106": {
        "nombre": "USB",
        "precio": 150,
        "stock": 20
    }
}

print("=== BUSQUEDA HASH ===")

print("\nCodigos de productos disponibles:")

for codigo in productos:
    print("-", codigo)

codigo = input("\nIngrese el codigo del producto: ").upper()

resultado = productos.get(codigo)

if resultado is not None:

    print("\nPRODUCTO ENCONTRADO")
    print("Codigo:", codigo)
    print("Nombre:", resultado["nombre"])
    print("Precio: $", resultado["precio"])
    print("Stock:", resultado["stock"])

else:

    print("\nEl producto no se encuentra registrado.")
