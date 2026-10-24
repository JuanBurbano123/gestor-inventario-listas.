
productos = []
cantidades = []


def buscar_producto(nombre):
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            return i
    return -1


def registrar_producto():
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    if buscar_producto(nombre) != -1:
        print("Este producto ya esta registrado.")
        return

    try:
        cantidad = int(input("Cantidad disponible: "))

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return

        productos.append(nombre)
        cantidades.append(cantidad)

        print("Producto registrado correctamente.")

    except ValueError:
        print("Error: debe ingresar un numero entero.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        print("\n--- INVENTARIO ---")

        for i in range(len(productos)):
            print(
                i + 1, ".",
                productos[i],
                "- Cantidad:", cantidades[i]
            )


def consultar_producto():
    nombre = input("Nombre del producto que desea buscar: ").strip()
    posicion = buscar_producto(nombre)

    if posicion != -1:
        print("Producto:", productos[posicion])
        print("Cantidad disponible:", cantidades[posicion])
    else:
        print("El producto no existe en el inventario.")


def modificar_cantidad():
    nombre = input("Nombre del producto que desea modificar: ").strip()
    posicion = buscar_producto(nombre)

    if posicion != -1:
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return

            cantidades[posicion] = nueva_cantidad
            print("Cantidad modificada correctamente.")

        except ValueError:
            print("Error: debe ingresar un numero entero.")
    else:
        print("El producto no existe en el inventario.")


def eliminar_producto():
    nombre = input("Nombre del producto que desea eliminar: ").strip()
    posicion = buscar_producto(nombre)

    if posicion != -1:
        eliminado = productos.pop(posicion)
        cantidades.pop(posicion)

        print("Producto eliminado:", eliminado)
    else:
        print("El producto no existe en el inventario.")


def mostrar_resumen():
    print("\n--- RESUMEN DEL INVENTARIO ---")
    print("Productos diferentes registrados:", len(productos))

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    mayor = max(cantidades)
    posicion = cantidades.index(mayor)

    print("Producto con mayor cantidad:", productos[posicion])
    print("Cantidad disponible:", mayor)

    print("Unidades totales:", sum(cantidades))


def menu():
    while True:
        print("\n===== GESTOR DE INVENTARIO =====")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar cantidad")
        print("5. Eliminar producto")
        print("6. Mostrar resumen")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            consultar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            print("Gracias por utilizar el gestor de inventario.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


menu()

