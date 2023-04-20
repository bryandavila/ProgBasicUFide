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
            
            import datetime
            def realizar_pedidos():
                nombre=input("Ingrese su nombre:")
                platillos=[]
                continuar=True
                while continuar:
                    platillo=input("Ingrese el nombre del platillo que desea pedir: ")
                    platillos.append(platillo)
                    respuesta=input("¿Desea agregar otro platillo? (si o no): ")
                    if respuesta=="no":
                        continuar=False
                print("Sus platillos registrados son:", platillos)
                with open("ordenes.txt", "a") as f:
                    f.write(nombre + ":" + ",".join(platillos) + "\n")
                hora_actual = datetime.datetime.now()
                hora = hora_actual.strftime('%H:%M')
                print("Hora en la que se hizo el pedido=", hora)
                with open("horas.txt", "w") as f:
                    f.write(hora)
                with open("pedidos.txt", "a") as f:
                    f.write(nombre + ",".join(platillos) + "\n")
                print("Pedido registrado exitosamente.")


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

            def imprimir_factura():
                print("Ingrese la cantidad de platillos que desea comprar: ")
                cantidad = int(input())
                print("Ingrese la descripción de los platillos: ")
                descripcion = input()
                print("Ingrese el precio unitario de los platillos: ")
                precio = float(input())
                subtotal = cantidad * precio
                cumpleanos = input("¿Es tu cumpleaños hoy? (si o no) ")
                if cumpleanos == "si":
                    descuento = subtotal * 0.12
                else:
                    descuento = 0
                impuesto_venta = subtotal * 0.13
                total = subtotal + impuesto_venta - descuento
                print("Factura:")
                print("Cantidad de platillos:", cantidad)
                print("Descripción:", descripcion)
                print("Precio sin IVA: $", precio)
                print("Subtotal: $", subtotal)
                print("Impuesto de venta (13%): $", impuesto_venta)
                if cumpleanos == "si":
                    print("Descuento (12%): $", descuento)
                print("Total: $", total)

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
                    imprimir_factura()
                else:
                    print("Ha ingresado una opción inválida")

elif rol==2:
    class Platillo:
        def __init__(self, tipo, descripcion, precio_sin_iva):
            self.tipo = tipo
            self.descripcion = descripcion
            self.precio_sin_iva = precio_sin_iva
    platillos = []
    ordenes=[]
    def registrar_platillo():
        tipo = input("Ingrese el tipo del platillo: ")
        descripcion = input("Ingrese la descripción del platillo: ")
        precio_sin_iva = float(input("Ingrese el precio sin IVA del platillo: "))
        platillo = Platillo(tipo, descripcion, precio_sin_iva)
        platillos.append(platillo)
    def mostrar_ordenes():
        try:
            with open("pedidos.txt", "r") as f:
                pedidos = f.read()
                print("Pedidos registrados:")
                print(pedidos)
        except FileNotFoundError:
            print("No se han registrado pedidos todavía.")
            print()
    def mostrar_platillos():
        print("Lista de platillos:")
        for platillo in platillos:
            print("- Tipo:", platillo.tipo)
            print("- Descripción:", platillo.descripcion)
            print("- Precio sin IVA:", platillo.precio_sin_iva)
        print()

    def mostrar_pedidos_registrados():
        nombre = input("Ingrese su nombre registrado en el código A: ")
        with open("pedidos.txt", "r") as f:
            pedidos = f.read().strip()
        print(f"Nombre: {nombre}")
        print(f"Pedidos registrados: {pedidos}")


while True:
    opcion = input("Seleccione una opción:\n1. Registrar platillo\n2. Mostrar órdenes\n3. Salir\n4. Mostrar platillos\n")
    if opcion == "1":
        registrar_platillo()
    elif opcion == "2":
        mostrar_ordenes()
    elif opcion == "3":
        break
    elif opcion == "4":
        mostrar_platillos()
    elif opcion =="5":
        mostrar_pedidos_registrados()
    else:
        print("Opción inválida.")





    

