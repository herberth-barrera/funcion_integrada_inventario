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


---

Integrantes del grupo y responsabilidad:
Herberth Barrera: Codigo main.py
Hector Calderon: inventario.py
Camila Herrera: inventario.py
Andres Romero: Readme.md
