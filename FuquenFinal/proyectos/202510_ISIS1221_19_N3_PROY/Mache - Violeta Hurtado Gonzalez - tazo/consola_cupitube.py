
import cupitube as ct

cupitube = "/Users/macuser/Documents/Violeta. IP/v.hurtadog/dataset.csv" 
datos = ct.cargar_datos(cupitube)


###### Funciones auxiliares (NO MODIFICAR):
    
# Función auxiliar que muestra la información de un CupiTuber
def mostrar_cupituber(cupituber: dict) -> None:
   
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
    """
    Muestra los CupiTubers que pertenecen a la categoría dada y cuyo número de suscriptores se encuentre dentro del rango especificado.
    Ya se provee la implementación completa de esta función y no se requiere ningún cambio.
               
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    Se debe pedir al usuario la categoría, y el mínimo y el máximo del rango de suscriptores.    
    
    Hay 2 casos posibles:
        - Si no se encuentra ningún CupiTuber que cumpla con los criterios, el mensaje es:
            - "No se encontraron CupiTubers que cumplan con los criterios."
        
        - Caso contrario, debe usar la función auxiliar: mostrar_cupitubers() para mostrar a todos los CupiTubers que cumplan con los criterios.
    """
    categoria = input("Ingrese la categoría: ")
    minimo = int(input("Ingrese el mínimo de suscriptores: "))
    maximo = int(input("Ingrese el máximo de suscriptores: "))
    
    cupitubers = ct.buscar_por_categoria_y_rango_suscriptores(cupitube, minimo, maximo, categoria)
    
    if cupitubers != []:
        mostrar_cupitubers(cupitubers)
    else:
        print("No se encontraron CupiTubers que cumplan con los criterios.")


def ejecutar_buscar_cupitubers_por_pais_categoria_monetizacion(cupitube: dict) -> None:
    pais = input("Ingrese el país: ")
    categoria = input("Ingrese la categoría: ")
    monetizacion = input("Ingrese el tipo de monetización: ")

    resultado = ct.buscar_cupitubers_por_pais_categoria_monetizacion(cupitube, pais, categoria, monetizacion)

    if resultado != []:
        print("CupiTubers encontrados:")
        mostrar_cupitubers(resultado)
    else:
        print("No hay CupiTubers con ese país, categoría y monetización.")


        
def ejecutar_buscar_cupitubers_con_muchas_vistas(cupitube: dict) -> None:
    vistas = int(input("Ingrese la cantidad mínima de vistas: "))
    cupitubers = ct.buscar_cupitubers_con_muchas_vistas(cupitube, vistas)

    if len(cupitubers) > 0:
        print("CupiTubers con más de", vistas, "vistas:")
        mostrar_cupitubers(cupitubers)
    else:
        print("No se encontraron CupiTubers con más de", vistas, "vistas.")



def ejecutar_buscar_cupituber_con_mas_vistas(cupitube: dict) -> None:
    cupituber = ct.buscar_cupituber_con_mas_vistas(cupitube)
    if cupituber is not None:
        print("CupiTuber con más vistas:")
        mostrar_cupituber(cupituber)
    else:
        print("No se encontraron CupiTubers.")



def ejecutar_obtener_categoria_con_mas_visitas(cupitube: dict) -> None:
    categoria, visitas = ct.obtener_categoria_con_mas_visitas(cupitube)
    
    if categoria:
        print("La categoría con más visitas es: {} con {} visitas.".format(categoria, visitas))
    else:
        print("No se encontraron categorías con visitas.")


    
def ejecutar_crear_correo_para_cupitubers(cupitube: dict) -> None:

    if "USA" in cupitube and cupitube["USA"] != [] and cupitube["USA"][0] is not None:
        ct.crear_correo_para_cupitubers(cupitube)
        cupituber = cupitube["USA"][0]
        print("El correo para el primer Cupituber de 'USA' con nombre '" + cupituber["cupituber"] + "' es: " + cupituber["correo"] + ".")
        

def ejecutar_recomendar_cupituber(cupitube: dict) -> None:
    
    
    
    min_suscriptores = int(input("Ingrese el límite inferior del rango de suscriptores: "))
    max_suscriptores = int(input("Ingrese el límite superior del rango de suscriptores: "))
    min_videos = int(input("Ingrese la cantidad mínima de videos requeridos: "))
    fecha_min = input("Ingrese la fecha mínima (YYYY-MM-DD): ")
    fecha_max = input("Ingrese la fecha máxima (YYYY-MM-DD): ")
    palabra_clave = input("Ingrese la palabra clave que debe aparecer en la descripción: ").lower()

   
    categoria_mas_visitas, _ = ct.obtener_categoria_con_mas_visitas(cupitube)

    
    for pais, cupitubers in cupitube.items():
        for cupituber in cupitubers:
           
            if cupituber["category"] == categoria_mas_visitas:
                
                if min_suscriptores <= cupituber["subscribers"] <= max_suscriptores:
                   
                    if cupituber["video_count"] >= min_videos:
                     
                        if fecha_min <= cupituber["started"] <= fecha_max:
                           
                            if palabra_clave in cupituber["description"].lower():
                                
                                print("El CupiTuber recomendado tiene la siguiente información:")
                                mostrar_cupituber(cupituber)
                                return

    
    print("No se encontró un CupiTuber que cumpla con los criterios.")

    
    
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



