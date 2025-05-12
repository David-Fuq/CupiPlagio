# d = {
#      "India":[
#          {
#              "category":"Music","view_counts":2000000
#              },
#          {
#              "category":"Gaming","view_counts":4000000
#              }
#          ]
#      }

# for pais in d:
#      print(pais) # India
#      print(d[pais]) # [{'category': 'Music', 'view_counts': 2000000}, {'category': 'Gaming', 'view_counts': 4000000}]
#      i = 0
#      print(d[pais][i]) # {'category': 'Music', 'view_counts': 2000000}
# #     print(d[pais][i]["category"]) # Music
# #     print(d[pais][i]["view_counts"]) # 2000000
    


# d1 = {
#      "India":[
#          {
#              "category":"Music","view_counts":2000000
#              },
#          {
#              "category":"Gaming","view_counts":4000000
#              }
#          ],
#      "USA":[
#          {
#              "category":"Gaming","view_counts":20000000
#              },
#          {
#              "category":"Music","view_counts": 50000000
#              }
#          ]
#      }

# for pais in d1:
#     print(pais)
#     # India
#     # USA
#     print(d1[pais])
#     # [{'category': 'Music', 'view_counts': 2000000}, {'category': 'Gaming', 'view_counts': 4000000}]
#     # [{'category': 'Gaming', 'view_counts': 20000000}, {'category': 'Music', 'view_counts': 50000000}]
    
# mi_string = "¡Python es genial! 3.14"
# string = ""
# for cadacaracter in mi_string:
#     if cadacaracter.isalnum():
#         string += cadacaracter
# print(string)  # Salida: Pythonesgenial314
# print(string.isalnum()) # Salida: True
    
lista = [{
            "Nombre" : "Mr.Beast",
            "edad":32
            },
        {"Nombre":"@Pewdiepie",
         "edad":35
            }]

# print(lista)

diccionario = 0
nombre = ""
nuevo_nombre = {"Correo":""}

while diccionario < len(lista):
    cada_diccionario = lista[diccionario]
    
    llavenombre = cada_diccionario["Nombre"].isalnum()
    N = cada_diccionario["Nombre"]
    
    
    
    for cadacaracter in N:
        
        if cadacaracter.isalnum():
            nombre += cadacaracter
    
    nuevo_nombre("Correo") == nombre
    
    lista.append(nuevo_nombre)  
    
    diccionario += 1


  

# print(nombre)    
    


print(lista)
    
    