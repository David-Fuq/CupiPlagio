
# Función 1: 
def cargar_datos(ruta: str) -> dict:
    archivo = open(ruta, "r", encoding="utf-8")
    linea = archivo.readline()  
    linea = archivo.readline().strip()

    datos_por_pais = {}

    while linea != "":
        valores = linea.split(",")

        info = {}
        info["rank"] = int(valores[0])
        info["cupituber"] = valores[1]
        info["subscribers"] = int(valores[2])
        info["video_views"] = int(valores[3])
        info["video_count"] = int(valores[4])
        info["category"] = valores[5]
        info["started"] = valores[6]
        info["country"] = valores[7]
        info["monetization_type"] = valores[8]
        info["description"] = valores[9]

        llave = valores[7]  

        if llave not in datos_por_pais:
            lista = []
        else:
            lista = datos_por_pais[llave]

        lista.append(info)
        datos_por_pais[llave] = lista

        linea = archivo.readline().strip()

    archivo.close()
    return datos_por_pais

cupitube = cargar_datos("/Users/macuser/Documents/Violeta. IP/v.hurtadog/cupitubers.csv")



# Función 2:
def buscar_por_categoria_y_rango_suscriptores(cupitube: dict, suscriptores_min: int, suscriptores_max: int, categoria_buscada: str) -> list:
    resultado = []

    for lista_cupi in cupitube.values():
        for creador in lista_cupi:
            if creador["category"] == categoria_buscada and suscriptores_min <= creador["subscribers"] <= suscriptores_max:
                resultado.append(creador)

    return resultado
  


# Función 3:
def buscar_cupitubers_por_pais_categoria_monetizacion(cupitube: dict, pais_buscado: str, categoria_buscada: str, monetizacion_buscada: str) -> list:
   
    resultado = []

    if pais_buscado in cupitube:
        for cupituber in cupitube[pais_buscado]:
            if (cupituber["category"] == categoria_buscada and 
                cupituber["monetization_type"] == monetizacion_buscada):
                resultado.append(cupituber)

    return resultado



# Función 4:
def buscar_cupituber_mas_antiguo(cupitube: dict) -> dict:

    cupituber_mas_antiguo = None
    fecha_mas_antigua = "9545-12-31"  

    for lista_cupi in cupitube.values():
        for cupituber in lista_cupi:
            if cupituber["started"] < fecha_mas_antigua:
                fecha_mas_antigua = cupituber["started"]
                cupituber_mas_antiguo = cupituber

    return cupituber_mas_antiguo

            

# Función 5:
def obtener_visitas_por_categoria(cupitube: dict, categoria_buscada: str) -> int:
  
    total_visitas = 0
    
    
    for youtuber, data in cupitube.items():
        
        if categoria_buscada in data["category"]:
            total_visitas += data["video_views"]
    
    return total_visitas



# Función 6:
def obtener_categoria_con_mas_visitas(cupitube: dict) -> dict:
    visitas_por_categoria = {}
    
    
    for youtuber in list(cupitube.keys()):
        data = cupitube[youtuber]
        for categoria in data["category"]:
            if categoria not in visitas_por_categoria:
                visitas_por_categoria[categoria] = data["video_views"]
            else:
                visitas_por_categoria[categoria] += data["video_views"]
    
    
    categoria_mas_visitas = None
    max_visitas = 0
    
    for categoria, visitas in visitas_por_categoria.items():
        if visitas > max_visitas:
            categoria_mas_visitas = categoria
            max_visitas = visitas
    
    return {"categoria": categoria_mas_visitas, "visitas": max_visitas}



# Funcion 7:
def crear_correo_para_cupitubers(cupitube: dict) -> None:
    for data in cupitube.values():
        nombre = data["name"].lower()

        
        nombre_limpio = ""
        for letra in nombre:
            if letra >= 'a' and letra <= 'z':
                nombre_limpio += letra
            elif letra >= '0' and letra <= '9':
                nombre_limpio += letra

        nombre_limpio = nombre_limpio[:15]

        fecha = data["start_date"]
        anio = fecha[0:4]
        mes = fecha[5:7]

        correo = nombre_limpio + "." + anio[2:] + mes + "@cupitube.com"
        data["correo"] = correo


# Función 8:
def recomendar_cupituber(cupitube: dict, suscriptores_min: int, suscriptores_max: int, fecha_minima: str, fecha_maxima: str, videos_minimos: int, palabra_clave: str) -> dict:
  
    categoria_mas_visitas = ""
    max_visitas = 0
    for youtuber in cupitube.keys():
        
        data = cupitube[youtuber]
    
    for categoria in data["category"].keys():
        visitas = data["category"][categoria]
        

        if visitas > max_visitas:
            max_visitas = visitas
            categoria_mas_visitas = categoria


    for youtuber, data in cupitube.items():
   
        if categoria_mas_visitas == data["category"]:
          
            if suscriptores_min <= data["subscribers"] <= suscriptores_max:
               
                if data['videos'] >= videos_minimos:
                    
                    if fecha_minima <= data["start_date"] <= fecha_maxima:
                       
                        if palabra_clave.lower() in data["description"].lower():
                            
                            return data
    

    return {}



# Función 9:
def paises_por_categoria(cupitube: dict) -> dict:
    
    resultado = {}

    for youtuber in cupitube.keys():
        data = cupitube[youtuber]
        pais = data["country"]
        categorias = data["category"]

        for categoria in categorias:
            if categoria not in resultado:
                resultado[categoria] = []

            if pais not in resultado[categoria]:
                resultado[categoria].append(pais)

    return resultado


