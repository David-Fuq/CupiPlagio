#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CupiTube
"""

# Función 1: 
def cargar_cupitube(archivo: str) -> dict:
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
    información_cupitube={}
    lista_cupitube= open(archivo,"r",encoding= "utf-8")
    fila = archivo.readline().strip().split(",")
    for linea in archivo:
        datos_cupituber = linea.strip().split(",")
        dic_pais ={}
        for i in range(len(fila)):
            dic_pais[fila[i]]=datos_cupituber[i]
            información_cupitube[dic_pais[fila[8]]]=dic_pais
    
    lista_cupitube.close()
    return información_cupitube
    
    
    pass


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
    por_categoria_rango=[]
    for linea in cupitube:
        if linea["category"] == categoria_buscada and suscriptores_min <= linea["subscribers"] <= suscriptores_max:
            por_categoria_rango.append(linea)
                
        return por_categoria_rango
    #TODO 2: Implemente la función tal y como se describe en la documentación.
    pass


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
    por_categoria_rango_monetizacion=[]
    
    for linea in cupitube:
        if linea["country"] == pais_buscado and linea["category"] == categoria_buscada and linea["monetization_type"] == monetizacion_buscada:
            por_categoria_rango_monetizacion.append(linea)
           
        return por_categoria_rango_monetizacion
    
    
    #TODO 3: Implemente la función tal y como se describe en la documentación.
    pass


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
    respuesta={}
    for i in cupitube:
        mas_antiguo=True
        for j in cupitube:
            if cupitube[j]["year"] < cupitube[i]["year"] or cupitube[j]["year"] == cupitube[i]["year"] and cupitube[j]["month"] < cupitube[i]["month"] or cupitube[j]["month"] == cupitube[i]["month"] and cupitube[j]["day"] < cupitube[i]["day"]:
                mas_antiguo=False
                if mas_antiguo:
                    respuesta={i:cupitube[i]}
    return respuesta
                
            
            
    #TODO 4: Implemente la función tal y como se describe en la documentación.
    pass
            

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
    visitas_categoria=0
    for i in cupitube:
        if cupitube[i]["category"] == categoria_buscada:
            visitas_categoria +=cupitube[i]["video_views"]
    return visitas_categoria
    #TODO 5: Implemente la función tal y como se describe en la documentación.
    pass



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
    visitas={}
    for i in cupitube:
        categoria=cupitube[i]["category"]
        visitas=cupitube[i]["video_views"]
        if categoria in visitas:
            visitas[categoria]+= cupitube[i]["video_views"]
        else:
            visitas[categoria]= cupitube[i]["video_views"]
        respuesta={}    
        maximas_visitas = -1
        for categoria in visitas:
            if visitas[categoria] > maximas_visitas:
                maximas_visitas=visitas[categoria]
                respuesta={"category":categoria,
                           "video_views": maximas_visitas}
    return respuesta
    #TODO 6: Implemente la función tal y como se describe en la documentación.
    pass


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
    pass


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
    categoria=obtener_categoria_con_mas_visitas(cupitube)
    letras_minusculas="abcdefghijklmnopqrstuwxyz"
    letras_mayusculas="ABCDEFGHIJKLMNOPQRSTUWXYZ"
    cambiar_letra={}
    for i in range(len(letras_mayusculas)):
        cambiar_letra=[letras_mayusculas[i]]=letras_minusculas[i]
    llave=""
    for letra in palabra_clave:
        if letra in cambiar_letra:
            llave +=cambiar_letra[letra]
        else:
             llave += letra   
    for i in cupitube:
        c=cupitube[i]
        if c["category"]== categoria:
            if c["subscribers"] >= suscriptores_min and c["subscribers"]<= suscriptores_max:
                if c["start_date"] >= fecha_minima and c["start_date"]<= fecha_maxima:
                    if c["video_count"]>=videos_minimos:
                        descripcion = c["description"]
                        descripcion_dada=""
                        for letra in descripcion:
                            if letra in cambiar_letra:
                                descripcion_dada += cambiar_letra[letra]
                            else:
                                descripcion_dada+= letra
                        if llave in descripcion_dada:
                            return c
            return {}
                        
    #TODO 8: Implemente la función tal y como se describe en la documentación.
    pass



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
    resultado={}
    for i in cupitube:
        c= cupitube[i]
        pais=c["country"]
        categoria=c["category"]
        
    if categoria in resultado:
        ya_existe= False
        for p in resultado[categoria]:
            if p == pais:
                ya_existe= True
        if ya_existe== False:
            resultado[categoria].append(pais)
            resultado[categoria] =[pais]
    return resultado
        
    #TODO 9: Implemente la función tal y como se describe en la documentación.
    pass
