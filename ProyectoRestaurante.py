# Definimos un diccionario para almacenar los platillos
platillos = {
    'Entradas': [],
    'Platos fuertes': [],
    'Postres': [],
    'Bebidas': []
}

# Definimos una lista para almacenar las órdenes
ordenes = []

# Función para registrar un platillo
def registrar_platillo():
    tipo = input('Ingrese el tipo de platillo (Entradas/Platos fuertes/Postres/Bebidas): ')
    descripcion = input('Ingrese la descripción del platillo: ')
    precio = float(input('Ingrese el precio del platillo sin IVA: '))
    platillos[tipo].append({'descripcion': descripcion, 'precio': precio})
    print('Platillo registrado con éxito.')

# Función para listar los platillos
def listar_platillos():
    for tipo, lista_platillos in platillos.items():
        print(f'{tipo}:')
        for i, platillo in enumerate(lista_platillos):
            print(f'{i+1}. {platillo["descripcion"]} - ${platillo["precio"]:.2f} sin IVA')

# Función para registrar una orden
def registrar_orden():
    usuario = input('Ingrese el nombre del usuario que solicita la orden: ')
    platillos_seleccionados = []
    while True:
        tipo = input('Ingrese el tipo de platillo (Entradas/Platos fuertes/Postres/Bebidas) o escriba "terminar" para finalizar: ')
        if tipo == 'terminar':
            break
        lista_platillos = platillos.get(tipo, [])
        if not lista_platillos:
            print('No hay platillos registrados para ese tipo.')
            continue
        print(f'{tipo}:')
        for i, platillo in enumerate(lista_platillos):
            print(f'{i+1}. {platillo["descripcion"]} - ${platillo["precio"]:.2f} sin IVA')
        seleccion = int(input('Seleccione el número del platillo que desea ordenar: '))
        platillo_seleccionado = lista_platillos[seleccion-1]
        platillos_seleccionados.append(platillo_seleccionado)
    orden = {'usuario': usuario, 'platillos': platillos_seleccionados}
    ordenes.append(orden)
    print('Orden registrada con éxito.')

# Función para listar las órdenes
def listar_ordenes():
    for i, orden in enumerate(ordenes):
        print(f'Orden {i+1}: {orden["usuario"]}')
        for platillo in orden['platillos']:
            print(f'- {platillo["descripcion"]} - ${platillo["precio"]:.2f} sin IVA')
        print()

# Función para finalizar una orden
def finalizar_orden():
    listar_ordenes()
    orden_seleccionada = int(input('Ingrese el número de la orden que desea finalizar: '))
    orden = ordenes[orden_seleccionada-1]
    ordenes.remove(orden)
    print(f'La orden {orden_seleccionada} ha sido finalizada.')

# Menú principal
while True:
    print('Bienvenido al sistema de administración de platillos y órdenes.')
    print('1. Registrar platillo')
    print('2. Listar platillos')
    print('3. Registrar orden')
    print('4. Listar órdenes')
    print('5. Finalizar orden')
    print('6. Salir')

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_platillo()
    elif opcion == "2":
        listar_platillos()
    elif opcion == "3":
        registrar_orden()
    elif opcion == "4":
        listar_ordenes()
    elif opcion == "5":
        finalizar_orden()
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Por favor ingrese una opción del 1 al 6")
