print("Escriba 1 si es cliente o escriba 2 si es empleado")
rol=int(input())
if rol==1:
    print("Proceda a registrarse")
    print("Ingrese su correo electrónico: ")
    correo=input()
    print("Ingrese su nombre completo: ")
    nombre=input()
    print("Ingrese su fecha de nacimiento (formato: dd/mm/aaaa): ")
    fechanacimiento=input()
    print("Ingrese el número de su tarjeta de crédito: ")
    numerotarjeta=input()
    print("Ingrese la fecha de vencimiento de su tarjeta (formato: mm/aaaa): ")
    fechavencimiento=input()
    print("Ingrese el código de seguridad de su tarjeta: ")
    codigoseguridad=input()

    print("Los datos ingresados son:")
    print("Nombre", nombre)
    print("Email", correo)
    print("fecha de nacimiento", fechanacimiento)
    print("Número de tarjeta", numerotarjeta)
    print("fecha de vencimiento", fechavencimiento)
    print("Código de seguridad", codigoseguridad)

    print("Escriba 1 si los datos está correctos, de lo contrario escriba 2 para volverlos a escribir")
    continuar=True
    while continuar:
        respuesta=int(input())
        if respuesta==2:
            print("Proceda a registrarse")
            print("Ingrese su correo electrónico: ")
            correo=input()
            print("Ingrese su nombre completo: ")
            nombre=input()
            print("Ingrese su fecha de nacimiento (formato: dd/mm/aaaa): ")
            fechanacimiento=input()
            print("Ingrese el número de su tarjeta de crédito: ")
            numerotarjeta=input()
            print("Ingrese la fecha de vencimiento de su tarjeta (formato: mm/aaaa): ")
            fechavencimiento=input()
            print("Ingrese el código de seguridad de su tarjeta: ")
            codigoseguridad=input()

            print("Los datos ingresados son:")
            print("Nombre", nombre)
            print("Email", correo)
            print("fecha de nacimiento", fechanacimiento)
            print("Número de tarjeta", numerotarjeta)
            print("fecha de vencimiento", fechavencimiento)
            print("Código de seguridad", codigoseguridad)

            print("Escriba 1 si los datos está correctos, de lo contrario escriba 2 para volverlos a escribir")
        else:
            continuar=False
            print("Se ha registrado correctamente")
            def realizar_pedidos():
                print("Escriba su pedido")
                pedido=input()
                continuar=True
                while continuar:
                    respuesta=input("¿Desea realizar otro pedido?")
                    if respuesta=="si":
                        print("Escriba su pedido")
                        pedido+=input()
                    else:
                        continuar=False
                        print("Su pedido registrado es:",pedido) #No pude separar cada pedido por (,)

                import datetime
                hora_actual = datetime.datetime.now()
                hora = hora_actual.strftime('%H:%M')
                print("Hora en la que se hizo el pedido=", hora)
                with open("pedidos.txt", "w") as f:
                    f.write(pedido)
                pedidosregistrados=pedido
                with open("horas.txt", "w") as f:
                    f.write(hora)
                tiempo_de_espera=hora

            def consultar_pedidos_ya_ingresados():
                try:
                    with open("pedidos.txt", "r") as f:
                        pedidos = f.read()
                        print("Pedidos registrados:")
                        print(pedidos)
                except FileNotFoundError:
                    print("No se han registrado pedidos todavía.")

            def Consultar_tiempo_de_orden_lista():
                try:
                    with open("horas.txt", "r") as f:
                        horas = f.read()
                        print("Hora de orden lista")
                        print("Su pedido estará listo en 15 minutos") 

                except FileNotFoundError:
                    print("No se han registrado pedidos todavía.")
            #Acá se debe colocar lo de generar facturas

            ''''def generar_factura(platillos_seleccionados, fecha_nacimiento):
                # Calcular subtotal
                subtotal = sum(platillo.precio_sin_iva for platillo in platillos_seleccionados)
                # Calcular descuentos
                descuento = 0
                if fecha_nacimiento is not None:
                    if fecha_nacimiento.day == datetime.date.today().day and fecha_nacimiento.month == datetime.date.today().month:
                        descuento = subtotal * 0.12
                # Calcular IVA
                iva = subtotal * 0.13
                # Calcular total
                total = subtotal + iva - descuento
                # Mostrar factura
                print("Factura:")
                for platillo in platillos_seleccionados:
                    print("Cantidad:", 1)
                    print("Descripción:", platillo.descripcion)
                    print("Precio:", platillo.precio_sin_iva)
                print("Subtotal:", subtotal)
                print("Descuentos:", descuento)
                print("IVA (13%):", iva)
                print("Total:", total)'''
         #Termina lo de facturas

            while True:
                print("1. Realizar pedidos")
                print("2. Consultar pedidos ya ingresados")
                print("3. Consultar tiempo de orden lista")
                print("4. Generar factura")
                
                opcion=print("Ingrese una opción")
                a=int(input())
                if a==1:
                    realizar_pedidos()
                elif a==2:
                    consultar_pedidos_ya_ingresados()
                elif a==3:
                    Consultar_tiempo_de_orden_lista()
                elif a==4:
                    generar_factura
                else:
                    print("Ha ingresado una opción inválida")

elif rol==2:
    #Definir una clase para los platillos
    class Platillo:
        def __init__(self, tipo, descripcion, precio_sin_iva):
            self.tipo = tipo
            self.descripcion = descripcion
            self.precio_sin_iva = precio_sin_iva

    #Definir una lista para almacenar los platillos
    platillos = []

    #Función para registrar un nuevo platillo
    def registrar_platillo():
        tipo = input("Ingrese el tipo del platillo: ")
        descripcion = input("Ingrese la descripción del platillo: ")
        precio_sin_iva = float(input("Ingrese el precio sin IVA del platillo: "))
        platillo = Platillo(tipo, descripcion, precio_sin_iva)
        platillos.append(platillo)

    #Función para mostrar la lista de órdenes
    def mostrar_ordenes():
        print("Lista de órdenes:")
        for orden in ordenes:
            print("Número de orden:", orden["numero"])
            print("Usuario:", orden["usuario"])
            print("Platillos:")
            for platillo in orden["platillos"]:
                print("- Tipo:", platillo.tipo)
                print("- Descripción:", platillo.descripcion)
                print("- Precio sin IVA:", platillo.precio_sin_iva)
            print()
            
    #Definir una lista para almacenar las órdenes
    ordenes = []

    #Uso del menú
    while True:
        opcion = input("Seleccione una opción:\n1. Registrar platillo\n2. Mostrar órdenes\n3. Salir\n")
        if opcion == "1":
            registrar_platillo()
        elif opcion == "2":
            mostrar_ordenes()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")



    


