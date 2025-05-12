#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CupiTube
"""

import cupitube as ct


###### Funciones auxiliares (NO MODIFICAR):
    
# Función auxiliar que muestra la información de un CupiTuber
def mostrar_cupituber(cupituber: dict) -> None:
    """
    Muestra la información de un CupiTuber.
    
    Parámetros:
        cupituber (dict): Diccionario con la información del CupiTuber.
    """
    print("\n")
    print("#" * 50)
    
    print((
        "\nNombre: {}\n"
        "Ranking: {}\n"
        "Suscriptores: {}\n"
        "Visitas de videos: {}\n"
        "Cantidad de videos: {}\n"
        "Categoría: {}\n"
        "Año de inicio: {}\n"
        "Tipo de monetización: {}\n"
        "Descripción: {}\n"
    ).format(
        cupituber["cupituber"], cupituber["rank"], cupituber["subscribers"],
        cupituber["video_views"], cupituber["video_count"], cupituber["category"],
        cupituber["started"], cupituber["monetization_type"], cupituber["description"]
    ))
    
    print("#" * 50)

# Función auxiliar que muestra la información de múltiples CupiTubers
def mostrar_cupitubers(cupitubers: list) -> None:
    """
    Muestra la información de una lista de CupiTubers.
    
    Parámetros:
        cupitubers (list): Lista de diccionarios con la información de los CupiTubers.
    """
    print("\nCupiTubers encontrados:")
    print("-" * 50)
    
    for cupituber in cupitubers:
        mostrar_cupituber(cupituber)

    print("-" * 50)
    
# Función auxiliar que muestra los países de CupiTubers en una categoría específica.
def mostrar_paises(paises: list) -> None:
    """ 
    Muestra los países que tienen CupiTubers en una categoría específica.
    
    Parámetros:
        paises (list): Lista de nombres de países.
    """
    print("-" * 50)
    
    for pais in paises:
        print(pais)
    
    print("-" * 50)
###### Fin de las funciones auxiliares



# Funciones a implementar (solo aquellas con TODOs):

def ejecutar_buscar_por_categoria_y_rango_suscriptores(cupitube: dict) -> None:
    

    categoria = input("Ingrese la categoría: ")
    minimo = int(input("Ingrese el mínimo de suscriptores: "))
    maximo = int(input("Ingrese el máximo de suscriptores: "))
    
    cupitubers = ct.buscar_por_categoria_y_rango_suscriptores(cupitube, minimo, maximo, categoria)
    
    if cupitubers != []:
        mostrar_cupitubers(cupitubers)
    else:
        print("No se encontraron CupiTubers que cumplan con los criterios.")
        


def ejecutar_buscar_cupitubers_por_pais_categoria_monetizacion(cupitube: dict) -> None:
    pais_buscado=input("Ingrese un pais:").capitalize()
    categoria_buscada=input("Ingrese una categoria:")
    monetizacion_buscada=input("Ingrese tipo de monetizacion")
    funcion=ct.buscar_cupitubers_por_pais_categoria_monetizacion(cupitube, pais_buscado, categoria_buscada, monetizacion_buscada)
    
    if funcion==[]:
        resp="No se encontraron CupiTubers que cumplan con los criterios."
        
    else: 
        resp="Los CupiTubers de " + str(pais_buscado) + " que pertenecen a la categoría " + str(categoria_buscada)+ " y tienen monetización " + str(monetizacion_buscada)+" son:"
        mostrar_cupitubers(funcion)
        
    print(resp)


        
def ejecutar_buscar_cupituber_mas_antiguo(cupitube: dict) -> None:
    
    funcion=ct.buscar_cupituber_mas_antiguo(cupitube)
    nombre=funcion["cupituber"]
    fecha=funcion["started"]
    
    resp="El CupiTuber más antiguo es " + str(nombre)+ " y empezó en " + str(fecha)
    print(resp)
    
   
   


def ejecutar_obtener_visitas_por_categoria(cupitube: dict) -> None:
    categoria_buscada=input("Ingrese una categoria:")
    funcion=ct.obtener_visitas_por_categoria(cupitube, categoria_buscada)
    vistas=funcion
    resp="El total de visitas para la categoría " + str(categoria_buscada) + " es: " + str(vistas)
    
    print(resp)


def ejecutar_obtener_categoria_con_mas_visitas(cupitube: dict) -> None:
    
    funcion=ct.obtener_categoria_con_mas_visitas(cupitube)
    categoria=funcion["category"]
    vistas=funcion["video_views"]
    resp="La categoría con más visitas es " +str(categoria)+ " con" +str(vistas) +"visitas."
    print(resp)


    
def ejecutar_crear_correo_para_cupitubers(cupitube: dict) -> None:

    if "USA" in cupitube and cupitube["USA"] != [] and cupitube["USA"][0] is not None:
        ct.crear_correo_para_cupitubers(cupitube)
        cupituber = cupitube["USA"][0]
        print("El correo para el primer Cupituber de 'USA' con nombre '" + cupituber["cupituber"] + "' es: " + cupituber["correo"] + ".")
        

def ejecutar_recomendar_cupituber(cupitube: dict) -> None:
    suscriptores_min = int(input("Ingrese límite inferior del rango de suscriptores: "))
    suscriptores_max = int(input("Ingrese límite superior del rango de suscriptores: "))
    
    fecha_minima = input("Ingrese el límite inferior del rango de fechas: (El formato de ingreso debe ser: YYYY-MM-DD) ")
    fecha_maxima = input("Ingrese el límite superior del rango de fechas: (El formato de ingreso debe ser: YYYY-MM-DD) ")
    videos_minimos = int(input("Ingrese la cantidad mínima de videos requerida: "))
    palabra_clave = input("Ingrese la palabra clave que debe estar en la descripción: (no se aceptan cadenas vacias) ").strip()
    
    funcion=ct.recomendar_cupituber(cupitube, suscriptores_min, suscriptores_max, fecha_minima, fecha_maxima, videos_minimos, palabra_clave)
    
    if  funcion == []:
        print("No se encontró un CupiTuber que cumpla con los criterios.")
    else: 
        print( "El Cupituber recomendado tiene la siguiente información:")
        mostrar_cupituber(funcion)
 
    
    
def ejecutar_paises_por_categoria(cupitube: dict) -> None:
  
    estructura = ct.paises_por_categoria(cupitube)
    
    categoria = input("Ingrese la categoría: ")
    
    if categoria != "" and categoria in estructura:
        paises = estructura[categoria]
        if paises != {} and paises is not None:
            print("\nLos países con CupiTubers en la categoría " + categoria + " son:")
            mostrar_paises(paises)
    else:
        print("La categoría ingresada no existe en los datos.")


###### Funciones del ménu (NO MODIFICAR):
def iniciar_aplicacion() -> None:
    """
    Función principal de la aplicación.
    """
    ejecutando = False
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si su archivo se llama cupitube.csv: ")
    
    if archivo == "":
        archivo = "cupitube.csv"
        
    estados = ct.cargar_cupitube(archivo)
    if estados != {} and estados is not None:
        ejecutando = True
        print("#" * 50)
        print("¡Bienvenido a la aplicación de CupiTube!")
        print("#" * 50)
    
        while ejecutando:
            ejecutando = mostrar_menu_aplicacion(estados)
            if ejecutando:
                input("Presione Enter para continuar...")
    else:
        print("\nError: No se ha podido cargar el archivo. \nRevise su implementación de la función: cargar_cupitube() en cupitube.py")
      
            
# Función para mostrar el menú de la aplicación:
def mostrar_menu_aplicacion(cupitube: dict) -> bool:
    """ 
    Muestra el menú de la aplicación y ejecuta la opción seleccionada por el usuario.
    """
    print("\nMenú de opciones:")
    print("1. Buscar CupiTubers por categoría y rango de suscriptores.")
    print("2. Buscar CupiTubers por país, categoría y monetización.")
    print("3. Buscar CupiTuber más antiguo.")
    print("4. Obtener visitas para una categoría.")
    print("5. Obtener categoría con más visitas.")
    print("6. Crear correo para CupiTubers.")
    print("7. Recomendar un CupiTuber.")
    print("8. Obtener países por categoría.")
    print("9. Salir.")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_por_categoria_y_rango_suscriptores(cupitube)
    elif opcion_elegida == "2":
        ejecutar_buscar_cupitubers_por_pais_categoria_monetizacion(cupitube)
    elif opcion_elegida == "3":
        ejecutar_buscar_cupituber_mas_antiguo(cupitube)
    elif opcion_elegida == "4":
        ejecutar_obtener_visitas_por_categoria(cupitube)
    elif opcion_elegida == "5":
        ejecutar_obtener_categoria_con_mas_visitas(cupitube)
    elif opcion_elegida == "6":
        ejecutar_crear_correo_para_cupitubers(cupitube)
    elif opcion_elegida == "7":
        ejecutar_recomendar_cupituber(cupitube)
    elif opcion_elegida == "8":
        ejecutar_paises_por_categoria(cupitube)
    elif opcion_elegida == "9":
        print("\n¡Gracias por usar la aplicación de CupiTube!")
        continuar_ejecutando = False
    else:
        print("Opción inválida. Por favor inténtelo de nuevo.")

    return continuar_ejecutando
###### Fin de las funciones del menú


# Punto de entrada de la aplicación
if __name__ == "__main__":
    iniciar_aplicacion()