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
    print(f'No existe un producto con ese nombre')
    return None

def editarProducto(nombre, inventario):
    #Aprovechamos la funcion "buscarProducto" para
    #encontrar al producto que queremos editar
    producto =  buscarProducto(nombre, inventario)
    if producto != None:
        print(f'Si no quiere cambiar cierta caracteristica, presione solamente enter')

        nuevoNombre= input(f"Ingrese nuevo nombre (actual: {producto.get('nombre',0)}):")
        nuevoPrecio= input(f"Ingrese nuevo precio (actual: {producto.get('precio',0)}):")
        nuevaCantidad= input(f"Ingrese nueva cantidad (actual: {producto.get('cantidad',0)}):")

        #Con el primer mensaje dejamos claro que si
        #el usuario no quiere cambiar un parametro que
        #enviara un mensaje vacio.
        #Evaluamos si la variable no esta vacia para
        #hacer el cambio debido.
        if nuevoNombre != "":
            producto["nombre"] = str(nuevoNombre)
        if nuevoPrecio != "":
            producto["precio"] = float(nuevoPrecio)
        if nuevaCantidad != "":
            producto["cantidad"] = int(nuevaCantidad)

        #Actualizamos el total y el stock bajo del producto
        producto["total"] = calcularTotal(producto["precio"], producto["cantidad"])
        producto["stock_bajo"] = validarStock(producto["cantidad"])

        #Comunicamos que se termino el cambio
        print("se actualizo el producto")
        #No tenemos que avisar en caso que no exista
        #el producto, en tal caso la funcion buscarProducto
        #avisa antes y no se ejecutaria el primer
        #if de esta funcion.
