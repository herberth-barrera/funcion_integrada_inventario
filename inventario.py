def calcularTotal(precio, cantidad):
    return precio * cantidad


def validarStock(cantidad, existente=5):
    return cantidad < existente


def registrarProducto(nombre, precio, cantidad, inventario):
    total_inversion = calcularTotal(precio, cantidad)
    alerta_stock = validarStock(cantidad, existente=5)
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": total_inversion,
        "stock_bajo": alerta_stock
    }
    
    inventario.append(producto)
    return inventario


def buscarProducto(nombre_buscar, inventario):
    for p in inventario:
        if p["nombre"].lower() == nombre_buscar.lower():
            return p
    return None