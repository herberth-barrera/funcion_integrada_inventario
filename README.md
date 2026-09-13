# funcion_integrada_inventario
Programa interactivo en consola desarrollado en Python. Aplica programación modular mediante funciones interconectadas con parámetros y valores de retorno para el registro de productos, cálculo automático de totales monetarios, control de alertas por stock bajo y búsqueda de artículos.

# 🛒 Sistema de Gestión de Inventario para Tienda

Un sistema modular desarrollado en **Python 3** orientado al control y gestión operativa del inventario de una tienda. El proyecto implementa los principios fundamentales de la **programación modular**, separando las reglas de negocio en funciones especializadas y reutilizables que procesan datos de entrada y retornan información estructurada para el sistema.

---

## 🎯 Características Principales

* **Cálculo Automático de Totales:** Determina el valor monetario acumulado por producto a partir de su precio unitario y cantidad en existencia.
* **Control de Stock Mínimo:** Evalúa automáticamente las existencias de cada artículo y genera alertas de **¡STOCK BAJO!** si la cantidad es menor al umbral de seguridad.
* **Registro de Productos:** Estructura y almacena la información de cada producto en un formato organizado (diccionarios dentro de listas).
* **Búsqueda Inteligente:** Permite localizar cualquier producto por su nombre dentro del inventario de forma insensible a mayúsculas/minúsculas.
* **Interfaz de Consola Interactiva:** Menú guiado por terminal mediante bucles de control (`while`) con manejo de excepciones (`try/except`) para evitar fallos por datos inválidos.
* **Casos de Prueba Iniciales:** Carga automática de 3 productos de prueba al iniciar el programa para verificar de inmediato el funcionamiento correcto de todos los cálculos y alertas.

---

## 🛠️ Estructura del Proyecto

```text
.
├── inventario.py    # Módulo lógico con las funciones propias del sistema
├── main.py          # Programa principal e interfaz de usuario en consola
└── README.md        # Documentación general y guía de ejecución

## Cómo ejecutarlo
python main.py

##Funciones de inventario.py
calcularTotal(precio, cantidad) → retorna el total (float)
validarStock(cantidad, umbral=5) → retorna True/False
registrarProducto(nombre, precio, cantidad, inventario) → retorna el inventario actualizado
buscarProducto(nombre_buscar, inventario) → retorna el producto con nombre coincidente/None
editarProducto(nombre, inventario) → busca el producto con el nombre ingresado con la función buscarProducto() y le pregunta al usuario que cambios desea hacer y retorna el producto actualizado; sino lo encuentra, retorna Nulo

## Equipo – parte de código desarrollada por cada integrante
- Herberth Otoniel Barrera Bonilla – implementó buscarProducto() en inventario.py, redactó la primera parte de README y creó el directorio de github
- Camila Alejandra Herrera Pleitez – implementó calcularTotal(), validarStock() y registrar Producto() en inventario.py
- Andrés Romero Weil – implementó main.py y las pruebas con distintos casos de datos
- Héctor Antonio Calderón Meléndez – implementó editarProducto en inventario.py y redactó la segunda parte de README desde el apartado "Cómo ejecutarlo"