from inventario import registrarProducto, buscarProducto

def ejecutar_pruebas_iniciales(inventario):
    print("--- EJECUTANDO CASOS DE PRUEBA DE INICIALIZACIÓN ---")
    inventario = registrarProducto("Soda Pepsi 600ml", 1.25, 12, inventario)
    inventario = registrarProducto("Aceite Motor 20W50", 6.50, 2, inventario)
    inventario = registrarProducto("Agua Embotellada 1L", 0.75, 25, inventario)
    print("Casos de prueba registrados exitosamente.\n")
    return inventario


def mostrar_menu():
    print("   SISTEMA DE INVENTARIO - TIENDA   ")
    print(" ")
    print("1. Registrar nuevo producto")
    print("2. Ver todos los productos")
    print("3. Buscar un producto por nombre")
    print("4. Salir")
    print(" ")


def main():
    inventario = []
    inventario = ejecutar_pruebas_iniciales(inventario)
    
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")
            nombre = input("Ingrese el nombre del producto: ")
            
            try:
                precio = float(input("Ingrese el precio unitario ($): "))
                cantidad = int(input("Ingrese la cantidad en existencia: "))
                
                inventario = registrarProducto(nombre, precio, cantidad, inventario)
                print(f"¡Producto '{nombre}' registrado con éxito!\n")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para precio y cantidad.\n")
                
        elif opcion == "2":
            print("\n--- LISTA DE PRODUCTOS REGISTRADOS ---")
            if len(inventario) == 0:
                print("El inventario está vacío.")
            else:
                for p in inventario:
                    estado = "¡STOCK BAJO!" if p["stock_bajo"] else "Normal"
                    print(f"• Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']} | Total: ${p['total']:.2f} | Estado: {estado}")
            print()
            
        elif opcion == "3":
            print("\n--- BUSCAR PRODUCTO ---")
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            resultado = buscarProducto(nombre_buscar, inventario)
            
            if resultado != None:
                estado = "¡STOCK BAJO!" if resultado["stock_bajo"] else "Normal"
                print(f"\nProducto encontrado:")
                print(f"Nombre: {resultado['nombre']}")
                print(f"Precio: ${resultado['precio']:.2f}")
                print(f"Cantidad: {resultado['cantidad']}")
                print(f"Total en inventario: ${resultado['total']:.2f}")
                print(f"Estado de Stock: {estado}\n")
            else:
                print(f"\nEl producto '{nombre_buscar}' no se encuentra en el inventario.\n")
                
        elif opcion == "4":
            print("\nGracias por utilizar el Sistema de Inventario. ¡Hasta luego!")
        else:
            print("\nOpción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()