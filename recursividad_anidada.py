# Estructura de un carrito con combos anidados
carrito_de_compras = {
    "nombre": "Super Combo Gamer",
    "descuento_porcentaje": 10,  # 10% de descuento al combo completo
    "elementos": [
        {
            "nombre": "Teclado Mecánico",
            "precio_base": 80.0,
            "elementos": []  # Producto simple
        },
        {
            "nombre": "Pack Streaming",
            "descuento_porcentaje": 5,  # 5% de descuento a este sub-combo
            "elementos": [
                {
                    "nombre": "Micrófono USB",
                    "precio_base": 100.0,
                    "elementos": []
                },
                {
                    "nombre": "Cámara Web HD",
                    "precio_base": 60.0,
                    "elementos": []
                }
            ]
        }
    ]
}

def calcular_precio_total(item):
    """
    Calcula el precio final procesando de adentro hacia afuera:
    resuelve primero los sub-combos/productos internos y usa
    sus precios calculados para resolver el combo principal.
    """
   
    if not item.get("elementos"):
        precio = item["precio_base"]
        print(f"  -> Producto individual: {item['nombre']} = ${precio:.2f}")
        return precio

    print(f"Procesando Combo: '{item['nombre']}'...")


    subtotales = [
        calcular_precio_total(sub_item) 
        for sub_item in item["elementos"]
    ]
    
    
    suma_elementos = sum(subtotales)
   
    descuento = item.get("descuento_porcentaje", 0) / 100
    precio_final_combo = suma_elementos * (1 - descuento)
    
    print(f" Subtotal '{item['nombre']}': ${suma_elementos:.2f} | Con {item.get('descuento_porcentaje')}% desc = ${precio_final_combo:.2f}\n")
    return precio_final_combo



print("=== CÁLCULO DE CARRITO CON COMBOS ANIDADOS ===\n")
total_a_pagar = calcular_precio_total(carrito_de_compras)
print(f"TOTAL FINAL A PAGAR: ${total_a_pagar:.2f}")