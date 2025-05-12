#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CupiTube
"""

#funcion de crear dic de cupituber
# def crear_dict_cupituber (datos:list)-> dict:
#     ct = { "rank" : int(datos[0]),
#           "cupituber": datos[1],
#           "subscribers":int(datos[2]),
#           "video_views":int(datos[3]),
#           "video_count":int(datos[4]),
#           "category": datos[5],
#           "started": datos[6],
#           "monetization_type": datos[8],
#           "description": datos[9] }
#     linea = "1,T-Series,222000000, 198459090822, 17317, Music, 2006-11-15, AdSense, bEST UnBOxInG ViDEos!"
#     datos = linea.split(",")
    
#     return (ct)

# Función 1: 
def cargar_cupitube(archivo: str) -> dict:
    
    #TODO 1: Implemente la función tal y como se describe en la documentación.
    paises = {}
    
    arch = open(archivo, "r", encoding = "utf-8")
    arch.readline()
    
    line = arch.readline().strip()
    while line != "":
        
        datos = line.split(",")
        dicti = { "rank" : int(datos[0]),
              "cupituber": datos[1],
              "subscribers": int(datos[2]),
              "video_views": int(datos[3]),
              "video_count": int(datos[4]),
              "category": datos[5],
              "started": datos[6],
              "monetization_type": datos[8],
              "description": datos[9] }
        
        pais = datos[7]
        
        if pais not in paises:
            paises[pais] = []
            
        paises[pais].append(dicti)
        line = arch.readline().strip()
    
    
    arch.close()
  
    return (paises)



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
    total = []
    
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            categoria = dicti_pais["category"]
            subs = dicti_pais ["subscribers"]
            if categoria.lower() == categoria_buscada.lower():
                if suscriptores_min < subs and subs < suscriptores_max:
                    total.append(dicti_pais)
                    
            
    return (total)

        


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
    total = []
    
    for pais in cupitube:
        if pais.lower() == pais_buscado.lower():
            lista_pais = cupitube[pais]
            for x in range(len(lista_pais)):
                dicti_pais = lista_pais[x]
                categoria = dicti_pais["category"].lower()
                mon = dicti_pais ["monetization_type"].lower()
                if categoria == categoria_buscada:
                    if mon == monetizacion_buscada:
                        total.append(dicti_pais)

    return (total)

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
    mas_antiguo_fecha = "2025-12-30"
    antiguo = ""
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            fecha = dicti_pais["started"]
            if fecha < mas_antiguo_fecha:
                antiguo = dicti_pais
                mas_antiguo_fecha = fecha
                
        return (antiguo)

            
            

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
    vistas_total = 0
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            if dicti_pais["category"].lower() == categoria_buscada:
                vistas_total += dicti_pais["video_views"]
                
    return (vistas_total)




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
    cat_mayor_view = {}
    view_cat = {}
    view_mayor = 0
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            categoria = dicti_pais["category"].lower()
            if categoria not in view_cat:
                view_cat[categoria] = obtener_visitas_por_categoria(cupitube, categoria)
        for c in view_cat:
            view_actual = view_cat[c]
            if view_actual > view_mayor:
                view_mayor = view_actual
                cat_mayor_view["categoria"] = c
                cat_mayor_view["visitas"] = view_mayor
                
        
            
    return (cat_mayor_view)


         
def quitar_caracteres_especiales (nombre:str) -> str:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","k","r","s","t","u","v","w","x","y","z"]
    num = ["0","1","2","3","4","5","6","7","8","9"]
    nom = list(nombre.lower())
    final = ""
    for x in nom:
        if x in letras or x in num:
            final += x
    final = final[:16]    
    return (final)
    
        
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
    correo = ""
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            nombre = dicti_pais["cupituber"].lower()
            año = dicti_pais["started"][2:4]
            mes = dicti_pais["started"][5:7]
            if not str.isalnum(nombre):
                nombre = quitar_caracteres_especiales(nombre)
            correo = nombre + "." + año + mes + "@cupitube.com"
            dicti_pais["correo"] = correo
            


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
    cat = obtener_categoria_con_mas_visitas(cupitube)["categoria"]
    
    
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            if dicti_pais["category"] == cat:
                if dicti_pais["subscribers"]<= suscriptores_max and dicti_pais["subscribers"]>= suscriptores_min:
                    if dicti_pais["video_count"] >= videos_minimos:
                        if dicti_pais["started"]>= fecha_minima and dicti_pais["started"]<= fecha_maxima:
                            if palabra_clave.lower() in dicti_pais["description"].lower():
                                return dicti_pais
   




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
    final = {}
    for pais in cupitube:
        lista_pais = cupitube[pais]
        for x in range(len(lista_pais)):
            dicti_pais = lista_pais[x]
            categoria = dicti_pais["category"].lower()
            if categoria not in final:
                final[categoria] = []
            if pais not in final[categoria]:
                final[categoria].append (pais)
                
    return final

