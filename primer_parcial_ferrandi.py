# Franco Ferrandi 
# Comision 115 turno mañana
# Primer parcial


MENU = """Menu de Gestion de Clinica
Seleccione el N° de la opcion deseada:
1. Cargar pacientes.
2. Mostrar todos los pacientes.
3. Buscar pacientes por numero de Historia Clinica.
4. Ordenar pacientes por numero de Historia Clinica.
5. Mostrar pacientes con mas dias de internacion.
6. Mostrar pacientes con menos dias de internacion.
7. Cantidad de pacientes con mas de 5 dias de internacion.
8. Promedio de dias de internacion de todos los pacientes.
9. Salir del programa.
"""

pacientes = []


def mostrar_menu(menu: str) -> None:
    """
    Recibe un string con la varible menu y la imprime.
    Parametros: menu (str)
    Devuelve: None
    """
    print(menu)

def cargar_paciente(pacientes: list) -> list:
    """
    Recibe parametro una lista("pacientes"), genera una lista nueva con numero de HC, nombre del paciente, edad, diagnostico y dias de internacion, y luego anida lista nueva en la lista recibida como parametro.
    Parametros: pacientes (list)
    Salida: pacientes (list)
    """
    cantidad_pacientes_ingresar = int(input("Cuantos pacientes desea ingresar: "))
    while cantidad_pacientes_ingresar <= 0:
        cantidad_pacientes_ingresar = int(input("Numero no valido (debe ser mayor a 0). Ingrese nuevamente cantidad de pacientes que quiere ingresar: "))

    if cantidad_pacientes_ingresar > 0:
        for n in range(cantidad_pacientes_ingresar):
            paciente_nuevo = []

            paciente_numero_hc = int(input(f"Ingrese el numero de historia clinica del paciente {n+1}: "))
            while paciente_numero_hc <= 0:
                paciente_numero_hc = int(input("Numero no valido (debe ser mayor o igual a 0). Ingrese nuevamente numero de historia clinica: "))

            paciente_nombre = input(f"Ingrese el nombre del paciente {n+1}: ").lower()
            while paciente_nombre == "":
                paciente_nombre = input("Nombre no valido. Ingrese el nombre del paciente: ").lower()

            paciente_edad = int(input(f"Ingrese la la edad del paciente {n+1}: "))
            while paciente_edad <= 0:
                paciente_edad = int(input("Edad no valida. Ingrese la la edad del paciente: "))

            paciente_diagnostico = input(f"Ingrese el diagnostico del paciente {n+1}: ").lower()
            while paciente_diagnostico == "":
                paciente_diagnostico = input("Nombre no valido. Ingrese el diagnostico del paciente: ").lower()

            paciente_dias_internacion = int(input(f"Ingrese la cantidad dias de internacion del paciente {n+1}: "))
            while paciente_dias_internacion < 0:
                paciente_dias_internacion = int(input("Cantidad no valida. Ingrese la cantidad dias de internacion del paciente: "))

            paciente_nuevo = [paciente_numero_hc, paciente_nombre, paciente_edad, paciente_diagnostico, paciente_dias_internacion]
            pacientes.append(paciente_nuevo)

    return pacientes

def mostrar_lista_pacientes(pacientes:list) -> None:
    """
    Recibe parametro una lista("pacientes") busca dentro de ella: nombre del producto buscado e imprime nombre, precio unitario y cantidad de stock del producto.
    Parametros: pacientes (list)
    Salida: None
    """

    for n in range(len(pacientes)):
        print(f"Paciente n°{n+1}:\nHC paciente: {pacientes[n][0]}, nombre: {pacientes[n][1]}, edad: {pacientes[n][2]}, diagnostico: {pacientes[n][3]}, dias de internacion: {pacientes[n][4]}.")

def busqueda_paciente_hc(pacientes:list) -> None:
    """
    Recibe parametro una lista("pacientes") busca dentro de ella el numero de HC del paciente e imprime numero de HC, nombre del paciente, edad, diagnostico y dias de internacion.
    Parametros: pacientes (list)
    Salida: None
    """
    paciente_numero_hc = int(input("Ingrese el numero de historia clinica del paciente: "))
    while paciente_numero_hc <= 0:
        paciente_numero_hc = int(input("Numero no valido (debe ser mayor o igual a 0). Ingrese nuevamente numero de historia clinica: "))

    for n in range(len(pacientes)):
        if pacientes[n][0] == paciente_numero_hc:

            mensaje = f"HC paciente: {pacientes[n][0]}, nombre: {pacientes[n][1]}, edad: {pacientes[n][2]}, diagnostico: {pacientes[n][3]}, dias de internacion: {pacientes[n][4]}."
            print(mensaje)
            break

    else:
        mensaje = "El numero de HC no fue encontrado en la base de datos."
        print(mensaje)

def ordenar_pacientes(pacientes: list) -> None:
    """
    Recibe parametro pacientes (list) y ordena los pacientes en función de su numero de HC de manera ascendente usando el método de burbuja.
    Parametros: pacientes (list)
    Return: None
    """
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j][0] > pacientes[j+1][0]:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]

    print("Lista de pacientes ordenada por HC de manera ascendente:")
    for paciente in pacientes:
        print(f"HC: {paciente[0]}, nombre del paciente: {paciente[1]}, edad: {paciente[2]}, diagnostico: {paciente[3]}, dias de internacion: {paciente[4]}")

def mostrar_paciente_mas_dias_internacion(pacientes:list) -> None:
    """
    Recibe parametro pacientes (list) e imprime los datos del paciente con mas dias de internacion.
    Parametros: pacientes (list)
    Return: None
    """
    paciente_mas_dias = float('-inf')
    paciente_mas_dias_nombre = ""
    paciente_mas_dias_hc = 0
    paciente_mas_dias_diagnostico = ""
    paciente_mas_dias_edad = 0

    for i in range(len(pacientes)):
        if pacientes[i][4] > paciente_mas_dias:
            paciente_mas_dias = pacientes[i][4]
            paciente_mas_dias_nombre = pacientes[i][1]
            paciente_mas_dias_hc = pacientes[i][0]
            paciente_mas_dias_diagnostico = pacientes[i][3]
            paciente_mas_dias_edad = pacientes[i][2]

    print(f"""Paciente con MAS dias de internacion:
Nombre paciente: '{paciente_mas_dias_nombre}', dias de internacion: {paciente_mas_dias}, n° HC: {paciente_mas_dias_hc}, edad: {paciente_mas_dias_edad}, diagnostico: {paciente_mas_dias_diagnostico}.""")

def mostrar_paciente_menos_dias_internacion(pacientes:list) -> None:
    """
    Recibe parametro pacientes (list) e imprime los datos del paciente con menos dias de internacion.
    Parametros: pacientes (list)
    Return: None
    """
    paciente_menos_dias = float('inf')
    paciente_menos_dias_nombre = ""
    paciente_menos_dias_hc = 0
    paciente_menos_dias_diagnostico = ""
    paciente_menos_dias_edad = 0

    for i in range(len(pacientes)):
        if pacientes[i][4] < paciente_menos_dias:
            paciente_menos_dias = pacientes[i][4]
            paciente_menos_dias_nombre = pacientes[i][1]
            paciente_menos_dias_hc = pacientes[i][0]
            paciente_menos_dias_diagnostico = pacientes[i][3]
            paciente_menos_dias_edad = pacientes[i][2]

    print(f"""Paciente con MENOS dias de internacion:
Nombre paciente: '{paciente_menos_dias_nombre}', dias de internacion: {paciente_menos_dias}, n° HC: {paciente_menos_dias_hc}, edad: {paciente_menos_dias_edad}, diagnostico: {paciente_menos_dias_diagnostico}.""")

def busqueda_paciente_mas_cinco_dias(pacientes:list) -> None:
    """
    Recibe parametro una lista("pacientes") busca dentro de ella el numero pacientes con mas de 5 dias de internacion e imprime la cantidad de pacientes que cumplan con la condicion.
    Parametros: pacientes (list)
    Salida: None
    """
    cantidad_pacientes_mas_cinco_dias = 0
    limite_dias = 5

    for n in range(len(pacientes)):
        if pacientes[n][4] > limite_dias:
            cantidad_pacientes_mas_cinco_dias += 1

    mensaje = f"Cantidad de pacientes que tienen mas de 5 dias de internacion: {cantidad_pacientes_mas_cinco_dias}."
    print(mensaje)

def promediar_dias_internacion(pacientes:list) -> None:

    acumulador_dias_internacion = 0
    contador_pacientes = 0

    for n in range(len(pacientes)):
        acumulador_dias_internacion += pacientes[n][4]
        contador_pacientes += 1

    promedio_dias_internacion = (acumulador_dias_internacion/contador_pacientes)
    promedio_dias_internacion_redondeado = round(promedio_dias_internacion, 2)

    mensaje = f"Promedio de dias de internacion de todos los pacientes: {promedio_dias_internacion_redondeado}."
    print(mensaje)

def ejecutar_opcion(seguir:str) -> str:
    """
    Recibe parametro "seguir" (str), se le pregunta un numero de opcion y ejecuta esa opcion(funcion) o finaliza el programa.
    Parametros: seguir (str)
    Salida: seguir (str)
    """
    opcion = int(input("Elige una opcion: "))
    while opcion < 1 or opcion > 9: 
        print("Opcion no valida")
        opcion = int(input("Elige una opcion(1-9): "))
        seguir = ""
    if opcion == 1:
        print("Haz elegido la opcion 1")
        cargar_paciente(pacientes)
        seguir = ""
    elif opcion == 9:
        print("Haz elegido la opcion 9. Haz salido del sistema.")
        seguir = "salir"
    else:
        if len(pacientes) == 0:
            print("No hay pacientes registrados para la operación solicitada.")
            seguir = ""
        else:
            if opcion == 2:
                print("Haz elegido la opcion 2")
                mostrar_lista_pacientes(pacientes)
                seguir = ""
            elif opcion == 3:
                print("Haz elegido la opcion 3")
                busqueda_paciente_hc(pacientes)
                seguir = ""
            elif opcion == 4:
                print("Haz elegido la opcion 4")
                ordenar_pacientes(pacientes)
                seguir = ""
            elif opcion == 5:
                print("Haz elegido la opcion 5")
                mostrar_paciente_mas_dias_internacion(pacientes)
                seguir = ""
            elif opcion == 6:
                print("Haz elegido la opcion 6")
                mostrar_paciente_menos_dias_internacion(pacientes)
                seguir = ""
            elif opcion == 7:
                print("Haz elegido la opcion 7")
                busqueda_paciente_mas_cinco_dias(pacientes)
                seguir = ""
            elif opcion == 8:
                print("Haz elegido la opcion 8")
                promediar_dias_internacion(pacientes)
                seguir = ""

    return seguir

seguir = ""
while seguir != "salir":
    mostrar_menu(MENU)
    seguir = ejecutar_opcion(seguir)