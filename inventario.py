def calcularTotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def validarStock(cantidad, unbral=5):
    return cantidad >= unbral

def registrarProducto(nombre, precio, cantidad, inventario):
    total = calcularTotal(precio, cantidad)
    stock_bajo = validarStock(cantidad)
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": total,
        "stock_bajo": stock_bajo
    }
    inventario.append(producto)
    return inventario

def buscarProducto(nombre_buscar, inventario):
    for p in inventario:
        if p["nombre"].lower() == nombre_buscar.lower():
            return p
    return None