#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CupiTube
"""

# Función 1: 
def cargar_cupitube(ruta: str) -> dict:
    """
    Carga un archivo en formato CSV (Comma-Separated Values) con la información de los CupiTubers y 
    los organiza en un diccionario donde la llave es el país de origen.
    
    Parámetros:
        archivo (str): Ruta del archivo CSV con la información de los CupiTubers, incluyendo la extensión.
                       Ejemplo: "./cupitube.csv" (si el archivo CSV está en el mismo directorio que este archivo).
    
    Retorno:
        dict: Diccionario estructurado de la siguiente manera:
            
            - Las llaves representan los países de donde provienen los CupiTubers.
              - El país de origen de un CupiTuber se encuentra en la columna "country" del archivo CSV.
              - El país es un string no vacío, sin espacios al inicio o al final.
                Ejemplo: "India"
            
            - Los valores son listas de diccionarios, donde cada diccionario representa un CupiTuber. 
              - Cada diccionario contiene los siguientes campos basados en las columnas del archivo CSV:
    
                "rank" (int): Ranking del CupiTuber en el mundo. Es un valor entero mayor a cero.
                              Ejemplo: 1
    
                "cupituber" (str): Nombre del CupiTuber. Es un string no vacío, sin espacios al inicio o al final.
                                   Ejemplo: "T-Series"
    
                "subscribers" (int): Cantidad de suscriptores del CupiTuber. Es un valor entero mayor a cero.
                                     Ejemplo: 222000000
    
                "video_views" (int): Cantidad de visitas de todos los videos del CupiTuber. Es un valor entero mayor o igual a cero.
                                     Ejemplo: 198459090822
    
                "video_count" (int): Cantidad de videos publicados por el CupiTuber. Es un valor entero mayor o igual a cero.
                                     Ejemplo: 17317
    
                "category" (str): Categoría principal de los videos del CupiTuber. Es un string no vacío, sin espacios al inicio o al final.
                                  Ejemplo: "Music"
    
                "started" (str): Fecha en la que el CupiTuber empezó a publicar videos en formato YYYY-MM-DD.
                                Es un string no vacío, sin espacios al inicio o al final.
                                Ejemplo: "2006-11-15"
    
                "monetization_type" (str): Tipo de monetización de los videos del CupiTuber. Es un string no vacío, sin espacios al inicio o al final.
                                           Ejemplo: "AdSense"
    
                "description" (str): Descripción del tipo de videos que publica el CupiTuber. Es un string no vacío, sin espacios al inicio o al final.
                                     Ejemplo: "Amazing travel vlogs worldwide!"
    
    Notas importantes:
        1. Al usar readline(), agregue strip() de esta forma: readline().strip() para garantizar que se eliminen los saltos de línea.
            Documentación de str.strip(): https://docs.python.org/es/3/library/stdtypes.html#str.strip
            Documentación de readline(): https://docs.python.org/es/3/tutorial/inputoutput.html#methods-of-file-objects
            
        2. Al usar open(), agregue la codificación "utf-8" de esta forma: open(archivo, "r", encoding="utf-8") para garantizar la lectura de caracteres especiales del archivo CSV.
    """
    #TODO 1: Implemente la función tal y como se describe en la documentación.

    archivo = open(ruta, "r",  encoding = "utf-8")
    linea = archivo.readline()
    linea = archivo.readline().strip()
    paises = {}
    
    while linea != "":
    
        listas = linea.split(",")
        info = {}
        info["rank"] = int(listas[0])
        info["cupituber"] = listas[1]
        info["subscribers"] = int(listas[2])
        info["video_views"] = int(listas[3])
        info["video_count"] = int(listas[4])
        info["category"] = listas[5]
        info["started"] = listas[6]
        info["monetization_type"] = listas[8]
        info["description"] = listas[9]
    
        llave = listas[7]
    
        if llave not in paises:
            
            l = []
            
        else:
            
            l = paises[llave]
        l.append(info)
    
        paises[llave] = l
        linea = archivo.readline().strip()
        
    archivo.close()
    return paises

ruta = "C:/Users/maira/Downloads/cupitube.csv"
cupitube = cargar_cupitube(ruta)

#print(cupitube)
    

# Función 2:
def buscar_por_categoria_y_rango_suscriptores(cupitube: dict, suscriptores_min: int, suscriptores_max: int, categoria_buscada: str) -> list:
    """
    Busca los CupiTubers que pertenecen a la categoría dada y cuyo número de suscriptores esté dentro del rango especificado.
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        suscriptores_min (int): Cantidad mínima de suscriptores requerida (inclusiva).
        suscriptores_max (int): Cantidad máxima de suscriptores permitida (inclusiva).
        categoria_buscada (str): Categoría de los videos del CupiTuber que se busca.
        
    Retorno:
        list: Lista con el o los diccionarios de los CupiTubers que cumplen con todos los criterios de búsqueda.
              Si no se encuentra ningún CupiTuber, retorna una lista vacía.
    
    Ejemplo:
        Para los siguientes valores:
        - suscriptores_min = 1000000
        - suscriptores_max = 111000000
        - categoria_buscada = "Gaming"
        
        Hay exactamente 102 cupitubers que cumplen con los criterios de búsqueda y que deben ser reportados en la lista retornada.
        ATENCIÓN: Este solo es un ejemplo de consulta exitosa en el dataset. Su función debe ser implementada para cualquier valor dado de: suscriptores_min, suscriptores_max y categoria_buscada.
    """
    #TODO 2: Implemente la función tal y como se describe en la documentación.
    
    rta = []
    
    for pais in cupitube:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            suscriptores = cupituber["subscribers"]
            categoria = cupituber["category"]
            
            if categoria == categoria_buscada and suscriptores_min <= suscriptores <= suscriptores_max:
                rta.append(cupituber)
                    
    return rta 

#print(buscar_por_categoria_y_rango_suscriptores(cupitube, 1000000, 111000000, "Gaming"))

# Función 3:
def buscar_cupitubers_por_pais_categoria_monetizacion(cupitube: dict, pais_buscado: str, categoria_buscada: str, monetizacion_buscada: str) -> list:
    """
    Busca los CupiTubers de un país, categoría y tipo de monetización buscados.
    
    Parámetros:
        cupitube (dict): Diccionario de países con la información de los CupiTubers.
        pais_buscado (str): País de origen buscado.
        categoria_buscada (str): Categoría buscada.
        monetizacion_buscada (str): Tipo de monetización buscada (monetization_type).
        
    Ejemplo:    
       Dado el país "UK", la categoría "Gaming" y el tipo de monetización "Crowdfunding",  hay un CupiTuber que cumpliría con estos criterios de búsqueda:
           [{'rank': 842, 'cupituber': 'TommyInnit', 'subscribers': 11800000, 'video_views': 1590238217, 'video_count': 289, 'category': 'Gaming', 'started': '2015-03-07', 'monetization_type': 'Crowdfunding', 'description': 'wEird fActs aND ExPERiments!'}]
       ATENCIÓN: Este solo es un ejemplo de consulta existosa en el dataset. Su función debe ser implementada para cualquier valor dado de: pais_buscado, categoria_buscada y monetizacion_buscada
        
    Retorno:
        list: Lista con el o los diccionarios de los CupiTubers que tienen como origen el país buscado, su categoría coincide con la categoría buscada y su tipo de monetización coincide con la monetización buscada.
                Si no se encuentra ningún CupiTuber o el país buscado no existe, se retorna una lista vacía.
    """
    #TODO 3: Implemente la función tal y como se describe en la documentación.
    
    rta = []
    
    for pais in cupitube:
        
        if pais == pais_buscado:
            
            lista = cupitube[pais]
        
            for cupituber in lista:
            
                categoria = cupituber["category"]
                monetizacion = cupituber ["monetization_type"]
            
                if categoria == categoria_buscada and monetizacion == monetizacion_buscada:
                    rta.append(cupituber)
                    
    return rta
        
print(buscar_cupitubers_por_pais_categoria_monetizacion(cupitube, "UK", "Gaming", "Crowdfunding"))

# Función 4:
def buscar_cupituber_mas_antiguo(cupitube: dict) -> dict:
    """
    Busca al CupiTuber más antiguo con base en la fecha de inicio (started).
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
    
    Retorno:
        dict: Diccionario con la información del CupiTuber más antiguo.
              En caso de empate (misma fecha de inicio o started), se retorna el primer CupiTuber encontrado.
    
    Nota:
        Las fechas de inicio de los CupiTubers ("started") en el dataset están en el formato "YYYY-MM-DD" (Año-Mes-Día).
        En Python, este formato permite que las fechas puedan compararse directamente como strings, ya que el orden lexicográfico coincide con el orden cronológico.
        
        Ejemplos de comparaciones:
            "2005-02-15" < "2006-06-10"  # → True (Porque 2005 es anterior a 2006)
            "2010-08-23" > "2009-12-31"  # → True (Porque 2010 es posterior a 2009)
            "2015-03-10" < "2015-03-20"  # → True (Mismo año y mes, pero el día 10 es anterior al día 20)
    """
    #TODO 4: Implemente la función tal y como se describe en la documentación.
    
    rta = None
    fecha = 8888-12-31
    
    for pais in cupitube:
        
        lista = cupitube[pais]

        for cupituber in lista:

            fecha_inicio = cupituber["started"]
            
            if fecha_inicio < fecha:
                
                fecha = fecha_inicio
                rta = cupituber
                
    return rta

#print(buscar_cupituber_mas_antiguo(cupitube))

# Función 5:
def obtener_visitas_por_categoria(cupitube: dict, categoria_buscada: str) -> int:
    """
    Obtiene el número total de visitas (video_views) acumuladas para una categoría dada de CupiTubers.
    
    Parámetros:
       cupitube (dict): Diccionario con la información de los CupiTubers.
       categoria_buscada (str): Nombre de la categoría de interés.
    
    Retorno:
       int: Número total de visitas para la categoría especificada.
           - Si la categoría aparece en múltiples CupiTubers, sus visitas se suman.
           - Si la categoría no está presente en los datos, el resultado a retornar será 0.
    
    Ejemplo:
       Dada la categoría "Music", hay un total de 2906210355935 vistas.
       ATENCIÓN: Este solo es un ejemplo de consulta existosa en el dataset. Su función debe ser implementada para cualquier valor dado de: categoria_busqueda.
    """
    #TODO 5: Implemente la función tal y como se describe en la documentación.
    
    vistas = 0
    
    for pais in cupitube:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            categoria = cupituber["category"]
            
            if categoria == categoria_buscada:
                
                vistas += cupituber["video_views"]
                
    return vistas

#print(obtener_visitas_por_categoria(cupitube, "Music"))

# Función 6:
def obtener_categoria_con_mas_visitas(cupitube: dict) -> dict:
    """
    Identifica la categoría con el mayor número de visitas (video_views) acumuladas.
    
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
        
    Retorno:
        dict: Diccionario con las siguientes llaves:
            - "categoria": Cuyo valor asociado es el nombre de la categoría con más visitas.
            - "visitas": cuyo valor asociado es la cantidad total de visitas de la categoría con más visitas.
        Si hay varias categorías con la misma cantidad máxima de visitas, se retorna la primera encontrada en el recorrido total del diccionario.
    """
    #TODO 6: Implemente la función tal y como se describe en la documentación.
    
    categorias = {}
    
    for pais in cupitube:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            categoria = cupituber["category"]
            vistas = cupituber["video_views"]
            
            if categoria in categorias:
                
                categorias[categoria] += vistas
                
            else:
                
                categorias[categoria] = vistas
                
    max_vistas = 0
    categoria_mas_vista = ""
    
    for categoria in categorias:
        
        if categorias[categoria] > max_vistas:
            
            max_vistas = categorias[categoria]
            categoria_mas_vista = categoria
            
    rta = {}
    
    rta["categoria"] = categoria_mas_vista
    rta["vistas"] = max_vistas
    
    return rta

#print(obtener_categoria_con_mas_visitas(cupitube))

# Funcion 7:
def crear_correo_para_cupitubers(cupitube: dict) -> None:
    """
    Crea una dirección de correo electrónico para cada CupiTuber siguiendo un formato específico y la añade al diccionario.
    Esta función modifica de forma permanente el diccionario recibido como parámetro, añadiendo una nueva llave "correo" con el valor asociado: [X].[Y][Z]@cupitube.com
    Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
    
    Donde:
        - [X]: Nombre del CupiTuber sin espacios y sin caracteres especiales.
        - [Y]: Últimos dos dígitos del año de inicio del CupiTuber.
        - [Z]: Los dos dígitos del mes de inicio del CupiTuber.
    
    Reglas de formato:
        - El nombre del CupiTuber debe estar libre de espacios y caracteres especiales.
              - Un carácter es especial si no es alfanumérico.
        - La longitud máxima del nombre debe ser de 15 caracteres. Si se excede este límite, se toman solo los primeros 15 caracteres.
        - Se debe añadir un punto (.) inmediatamente después del nombre.
        - A continuación, se agregan los últimos dos dígitos del año de inicio.
        - Luego, se añaden los dos dígitos del mes de inicio (sin guión o separador entre año y mes).
        - El correo generado debe estar siempre en minúsculas.
        
    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.
    
    Ejemplo:
        Para un CupiTuber con nombre "@PewDiePie" y fecha de inicio "2010-06-15",
        el correo generado sería: "pewdiepie.1006@cupitube.com"
    
    Nota:
        La función str.isalnum() permite verificar si una cadena es alfanumérica:
        https://docs.python.org/es/3/library/stdtypes.html#str.isalnum
    """
    #TODO 7: Implemente la función tal y como se describe en la documentación.
    
    for pais in cupitube:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            x = cupituber["cupituber"]
            fecha = cupituber["started"]
            
            x = ""
            
            for letra in x:
                
                if letra.isalnum():
                    
                    x += letra
                
            x = x [:15]
            y = fecha [2:4]
            z = fecha [5:7]
            
            correo = x.lower() + "." + y + z + "@cupitube.com"
            
            cupituber["correo"] = correo
            
            
# Función 8:
def recomendar_cupituber(cupitube: dict, suscriptores_min: int, suscriptores_max: int, fecha_minima: str, fecha_maxima: str, videos_minimos:int, palabra_clave: str) -> dict:
    """
    Recomienda al primer (uno solo) CupiTuber que cumpla con todos los criterios de búsqueda especificados.
    
    La función busca un CupiTuber que:
       - Pertenece a la categoría con más visitas totales.
       - Tiene un número de suscriptores dentro del rango especificado.
       - Ha publicado al menos la cantidad mínima de videos indicada.
       - Ha comenzado a publicar dentro del rango de fechas especificado.
       - Contiene la palabra clave dada como parte de su descripción (sin distinguir entre mayúsculas/minúsculas).
    
    Parámetros:
       cupitube (dict): Diccionario con la información de los CupiTubers.
       suscriptores_min (int): Cantidad mínima de suscriptores requerida (inclusiva).
       suscriptores_max (int): Cantidad máxima de suscriptores permitida (inclusiva).
       fecha_minima (str): Fecha mínima en formato YYYY-MM-DD (inclusiva).
       fecha_maxima (str): Fecha máxima en formato YYYY-MM-DD (inclusiva).
       videos_minimos (int): Cantidad mínima de videos requerida.
       palabra_clave (str): Palabra clave que debe estar presente como parte de la descripción.
           
    Retorno:
       dict: Información del primer CupiTuber que cumpla con todos los criterios.
             Si no se encuentra ningún CupiTuber que cumpla, retorna un diccionario vacío.
    
    Notas:
       - La búsqueda de la palabra clave no distingue entre mayúsculas y minúsculas.
         Por ejemplo, si la palabra clave es "gAMer" y la descripción contiene "Gamer ingenioso", el criterio de palabra clave se cumple para ese CupiTuber.
       - Por simplicidad, la búsqueda de la palabra clave se realiza también en subcadenas. 
         Por ejemplo, si la palabra clave es "car", el criterio de palabra clave se cumpliría para descripciones que contengan palabras como: "car", "card", "scarce", o "carpet", etc.
    """
    #TODO 8: Implemente la función tal y como se describe en la documentación.
    
    vistas_categoria = {}
    
    for pais in cupitube:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            categoria = cupituber["category"]
            vistas = cupituber["video_views"]
            
            if categoria in vistas_categoria :
                
                vistas_categoria += vistas
                
            else:
                
                vistas_categoria = vistas
                
    categoria_vistas = ""
    mayor_vistas = 0
    
    for categoria in categoria_vistas:
        
        if vistas_categoria[categoria] > mayor_vistas:
            
            mayor_vistas = vistas_categoria[categoria]
            categoria_vistas = categoria
            
    palabra_clave = palabra_clave.lower()
    
    for pais in lista:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            categoria = cupituber["category"]
            suscriptores = cupituber["subscribers"]
            fecha_inicio = cupituber["started"]
            videos = cupituber["video_count"]
            descripcion = cupituber["description"].lower()
            
            if categoria == categoria_vistas:
                if suscriptores_min <= suscriptores <= suscriptores_max:
                    if fecha_minima <= fecha_inicio <= fecha_maxima:
                        if videos >= videos_minimos:
                            if palabra_clave in descripcion:
                                return cupituber
                
    return {}

#print(recomendar_cupituber(cupitube, suscriptores_min, suscriptores_max, fecha_minima, fecha_maxima, videos_minimos, palabra_clave))

# Función 9:
def paises_por_categoria(cupitube: dict) -> dict:
    """
    Crea un diccionario que relaciona cada categoría de CupiTubers con una lista de países (sin duplicados) de origen de los CupiTubers en esa categoría.

    Parámetros:
        cupitube (dict): Diccionario con la información de los CupiTubers.

    Retorno:
        dict: Diccionario en el que las llaves son los nombres de las categorías y 
              los valores son listas de los nombres de los países (sin duplicados) que tienen al menos un CupiTuber en dicha categoría.

    Nota:
        - No se permiten países repetidos en la misma categoría.
        - Un país puede aparecer en varias categorías.
        - Cada categoría debe tener al menos un país asociado.
        - Por favor recuerde que el nombre un país en el dataset inicia con letra mayúscula, por ejemplo: "India"
    
    Ejemplo:    
       Al considerar la categoría (llave) "Music", la lista de países únicos asociados a esta sería:
           ['India', 'USA', 'Sweden', 'Russia', 'South Korea', 'Canada', 'Brazil', 'UK', 'Argentina', 'Poland', 'Saudi Arabia', 'Australia', 'Thailand', 'Spain', 'Indonesia', 'Mexico', 'France', 'Netherlands', 'Italy', 'Japan', 'Germany', 'South Africa', 'UAE', 'Turkey', 'China']
       ATENCIÓN: Este solo es un ejemplo de una de las categorías que se reportaría como llave en el diccionario resultado. 
       Su función debe reportar todas las categorías con su respectiva lista de países sin duplicados.
    """
    #TODO 9: Implemente la función tal y como se describe en la documentación.
    
    rta = {}
    
    for pais in cupitube:
        
        lista = cupitube[pais]
        
        for cupituber in lista:
            
            categoria = cupituber["category"]
            
            if categoria not in rta:
                
                rta[categoria] = []
                
            if pais not in rta[categoria]:
                
                rta[categoria].append(pais)

    return rta

#print(paises_por_categoria(cupitube))
            
