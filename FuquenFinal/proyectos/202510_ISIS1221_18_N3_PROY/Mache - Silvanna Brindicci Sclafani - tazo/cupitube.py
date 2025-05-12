#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

CupiTube
"""

# Función 1: 
def cargar_cupitube(ruta:str) -> dict:
    
    archivo=open(ruta,"r", encoding="utf-8")
    linea=archivo.readline()
    dict_grande={}
    linea=archivo.readline().strip()
    
    
    while linea !="":
    

        lista=linea.split(",")
        
        dict_pequeno={}
        dict_pequeno["cupituber"]=lista[0]
        dict_pequeno["susbcriber"]=int(lista[2])
        dict_pequeno["video_views"]=int(lista[3])
        dict_pequeno["videocount"]=int(lista[4])
        dict_pequeno["category"]=(lista[5])
        dict_pequeno["started"]=(lista[6])
        dict_pequeno["monetization_type"]=(lista[8])
        dict_pequeno["description"]=lista[9]
        
        llave=lista[7]
        
        if llave not in dict_grande:
            lista_1=[]
    
        else: 
            lista_1 = dict_grande[llave]
        lista_1.append(dict_pequeno)
        
        dict_grande[llave]=lista_1  
        linea=archivo.readline()
        
    return dict_grande
    
         
ruta ="/Users/silvannabrindiccisclafani/Downloads/n3-esqueleto/cupitube.csv"

cupitube=(cargar_cupitube(ruta))




# Función 2:
def buscar_por_categoria_y_rango_suscriptores(cupitube: dict, suscriptores_min: int, suscriptores_max: int, categoria_buscada: str) -> list:
    cumple=[]
    rango=range(suscriptores_min,suscriptores_max+1)
    
    for llave in cupitube:
        lista=cupitube[llave]
        for cupituber in lista :
            suscriptores=cupituber["susbcriber"]
            categoria=cupituber["category"]
            
            if categoria==categoria_buscada and suscriptores in rango:
                cumple.append(cupituber)
                
                
                
            elif categoria!=categoria_buscada and suscriptores not in rango:
                cumple=cumple
                
    return cumple  



# Función 3:
def buscar_cupitubers_por_pais_categoria_monetizacion(cupitube: dict, pais_buscado: str, categoria_buscada: str, monetizacion_buscada: str) -> list:
    cumple=[]

    for llave in cupitube:
        lista=cupitube[llave]
        for cupituber in lista :
            categoria=cupituber["category"]
            monetizacion=cupituber["monetization_type"]
            
            if llave==pais_buscado and categoria==categoria_buscada and monetizacion==monetizacion_buscada:
                cumple.append(cupituber)
            elif llave!=pais_buscado and categoria!=categoria_buscada and monetizacion!=monetizacion_buscada:
                cumple=cumple
                
    return cumple
            

def buscar_cupituber_mas_antiguo(cupitube: dict) -> dict:
    mayor="9999-12-31"
    cupi_antiguo={}
    for llave in cupitube:
        lista=cupitube[llave]
        for cupituber in lista:
            fecha=cupituber["started"]
            
            if fecha<mayor:
                mayor=fecha
                cupi_antiguo=cupituber
    return cupi_antiguo



    
def obtener_visitas_por_categoria(cupitube: dict, categoria_buscada: str) -> int:
    vistas=0
    
    for llave in cupitube:
        lista=cupitube[llave]
        for cupituber in lista :
            vistas_t=cupituber["video_views"]
            categoria=cupituber["category"]
            
            if categoria==categoria_buscada:
                vistas+=vistas_t
                
    return vistas


# Función 6:
def obtener_categoria_con_mas_visitas(cupitube: dict) -> dict:

    categoria_mayor_vistas=""
    dict_categoria_mayor_vistas={}
    mayor_visitas=-1
    
    
    
    for llave in cupitube:
        lista=cupitube[llave]
        
        for cupituber in lista :
            categoria=cupituber["category"]
            visitas=cupituber["video_views"]
 
            
            if categoria not in  dict_categoria_mayor_vistas:
                dict_categoria_mayor_vistas[categoria]=0
       
            dict_categoria_mayor_vistas[categoria]+=visitas
                
    for categoria in dict_categoria_mayor_vistas:
        if dict_categoria_mayor_vistas[categoria]>mayor_visitas:
                categoria_mayor_vistas=categoria
                resp={"categoria":categoria_mayor_vistas,
                "visitas":dict_categoria_mayor_vistas[categoria]}
                
                
    return resp 



# Funcion 7:
def crear_correo_para_cupitubers(cupitube: dict) -> None:


    for llave in cupitube:
        lista=cupitube[llave]
        for cupituber in lista :
            nombre=cupituber["cupituber"]
            fecha=cupituber["started"]
            
            
            nombre_final=""
            for i in nombre:
                if str.isalnum(i)==True:
                    nombre_final+=i
            if len(nombre_final)>15:
                nombre_final=nombre_final[0:16]
                
            final=nombre_final+"."
            fecha_mod=fecha[2:4]+fecha[5:7]
            final=nombre_final+"."+fecha_mod
            final=final.lower()
            
            cupituber["correo"]=final+"@cupitube.com"
            


# Función 8:
def recomendar_cupituber(cupitube: dict, suscriptores_min: int, suscriptores_max: int, fecha_minima: str, fecha_maxima: str, videos_minimos:int, palabra_clave: str) -> dict:
    
    resp={}
    
   
    
        
    for llave in cupitube:
        lista=cupitube[llave]
        
        for cupituber in lista :
            categoria=cupituber["category"]
            suscriptores=cupituber["susbcriber"]
            cantidad_videos=cupituber["videocount"]
            fecha=cupituber["started"]
            descripcion=cupituber["description"]
            
            if categoria==obtener_categoria_con_mas_visitas(cupitube):
               if suscriptores_min<suscriptores and suscriptores>suscriptores_max:
                   if cantidad_videos>videos_minimos :
                       if fecha_minima<fecha and fecha<fecha_maxima:
                           if palabra_clave.lower() in descripcion.lower():
                
                               resp=cupituber 
                
        
                
    return resp


# Función 9:
def paises_por_categoria(cupitube: dict) -> dict:
    
    diccionario_nuevo={}

    for llave in cupitube:
        lista=cupitube[llave]
        for cupituber in lista :
            categoria=cupituber["category"]
            
            if categoria not in diccionario_nuevo:
                diccionario_nuevo[categoria]=[]
            
            if llave not in diccionario_nuevo[categoria] :
                diccionario_nuevo[categoria].append(llave)
                
    return diccionario_nuevo


            

  
