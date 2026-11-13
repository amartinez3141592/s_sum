import math
import random

def numero_a_lista_fija(numero, bits_usados):
    l = [int(bit) for bit in f"{numero:b}"]
    l.reverse()
    return l

def obtener_suma_con_letras(tabla, letras):
    suma = 0
    i = 0
    while i < len(tabla):
        for l in letras:
            if tabla[i][0] == l:
                suma += tabla[i][1]
        i = i + 1
    return suma

def obtener_suma(tabla, pertenece):
    suma = 0
    for i in range(len(pertenece)):
        if pertenece[i] == 1:
            suma += tabla[len(tabla)-i-1][1]
    return suma

def obtener_suma_de_particiones(particiones, indices):
    suma = 0
    for particion_idx in range(len(particiones)):
        if indices[particion_idx][0] == 1:
            suma = suma + particiones[particion_idx][0][1] 
        if indices[particion_idx][1] == 1:
            suma = suma + particiones[particion_idx][1][1] 
    return suma

def obtener_letras_de_particiones(particiones, indices):
    letras = []
    for particion_idx in range(len(particiones)):
        if indices[particion_idx][0] == 1:
            letras.append(particiones[particion_idx][0][0]) 
        if indices[particion_idx][1] == 1:
            letras.append(particiones[particion_idx][1][0]) 
    return letras

def obtener_letras(tabla, pertenece):
    L = []
    for i in range(len(pertenece)):
        if pertenece[i] == 1:
            L.append(tabla[len(tabla)-i-1][0])
    return L


def obtener_suma_de_valores_en_el_indice(tabla, indice):
    # indice = int(random.uniform(0, 2**len(tabla)))
    pertenece = numero_a_lista_fija(indice, int(math.floor(2**len(tabla))))
    print("#SECRETO: variable local")
    print("indice", indice)
    pertenece.reverse()
    print("pertenece", pertenece)
    L = obtener_letras(tabla, pertenece)
    suma = obtener_suma(tabla, pertenece)
    print(L)
    print(suma)
    print("#SECRETO")
    return suma

def restar_binario(binario):
    if binario[0] == 0 and binario[1] == 0:
        return [1,1]
    if binario[0] == 0 and binario[1] == 1:
        return [0,0]
    if binario[0] == 1 and binario[1] == 0:
        return [0,1]
    if binario[0] == 1 and binario[1] == 1:
        return [1,0]
    
def sumar_binario(binario):
    if binario[0] == 0 and binario[1] == 0:
        return [0,1]
    if binario[0] == 0 and binario[1] == 1:
        return [1,0]
    if binario[0] == 1 and binario[1] == 0:
        return [1,1]
    if binario[0] == 1 and binario[1] == 1:
        return [0,0]

# funcion recursiva que recorre la tabla segun quiera
def proxima_direccion(particiones, indices, objetivo):

    suma_en_direccion = obtener_suma_de_particiones(particiones, indices)
    print("indices: ",indices,"suma: ", suma_en_direccion, "punto actual: ", obtener_letras_de_particiones(particiones, indices))
    
    if suma_en_direccion == objetivo:
        return indices
    elif suma_en_direccion > objetivo:
        # print("buscando")
        opciones = []
        for i in range(len(indices)):
            if restar_binario(indices[i]) != [1,1]:
                indice_en_direccion = restar_binario(indices[i])
                
                indice_auxiliar = [indices[idx_sin_actual] for idx_sin_actual in range(len(indices)) if idx_sin_actual != i]
                indice_auxiliar.insert(i, indice_en_direccion)

                suma_en_direccion = obtener_suma_de_particiones(particiones, indice_auxiliar)
                if suma_en_direccion >= objetivo:
                    opciones.append((i, suma_en_direccion))
        #region anterior
        # if restar_biario(indices[0]) != [1,1]:
        #     indice_arriba = restar_biario(indices[0])
        #     suma_arriba = obtener_suma_de_particiones(particiones, [indice_arriba, indices[1]])
        #     # print("arriba:", suma_arriba)
        #     if suma_arriba >= objetivo:
        #         opciones.append((0, suma_arriba))

        # if restar_biario(indices[1]) != [1,1]:
        #     indice_izq = restar_biario(indices[1])
        #     suma_izq = obtener_suma_de_particiones(particiones, [indices[0], indice_izq])
        #     # print("izq:", suma_izq)
        #     if suma_izq >= objetivo:
        #         opciones.append((1, suma_izq))
        
        if len(opciones) > 0:
            suma_menor_posible = min(opciones, key=lambda x: x[1])
            index = suma_menor_posible[0]

            indices[index] = restar_binario(indices[index])
        else:
            # como no hay opcion valida giro el cubo

            if indices != list(reversed(indices)):
                # si hace algo girarlo, lo hago. Si giro un cubo y estoy en [01,01,01] da lo mismo
                print("000")
                
                ultimo_eje = indices[len(indices)-1]
                for eje in range(0, len(indices)-1):
                    indices[eje + 1] = indices[eje]
                indices[0] = ultimo_eje
                
                # indices = list(reversed(indices))
            else:
                # sino salgo del subcubo inferior por cualquier eje de mayor valor y resto en todos los demas
                # esto es para que despues al girar siemrpe sea menor la nueva configuracion y no entre en bucle
                print("111")
                indices[len(indices)-1] = sumar_binario(indices[len(indices)-1])
                for eje in range(0, len(indices)-1):
                    if restar_binario(indices[eje]) != [1, 1]:
                        indices[eje] = restar_binario(indices[eje])
                
        return indices
    elif suma_en_direccion < objetivo:
        # sino salgo del subcubo inferior por cualquier eje de mayor valor y resto en todos los demas
        # esto es para que despues al girar siemrpe sea menor la nueva configuracion y no entre en bucle
        print("222")
        if sumar_binario(indices[len(indices)-1]) != [0,0]:
            indices[len(indices)-1] = sumar_binario(indices[len(indices)-1])
        else:
            ultimo_eje = indices[len(indices)-1]
            for eje in range(0, len(indices)-1):
                indices[eje + 1] = indices[eje]
            indices[0] = ultimo_eje
        # for eje in range(0, len(indices)-1):
        #     if restar_binario(indices[eje]) != [1, 1]:
        #         indices[eje] = restar_binario(indices[eje])
    
    return indices

lista_objetos = [
    # ("L", 35),
    # ("B", 20),  
    ("A", 3),  
    ("B", 7),  
    ("C", 32),  
    ("D", 33), 
    # ("E", 8),  
    # ("F", 34),

  
]
lista_objetos = sorted(
    lista_objetos,
    key=lambda x: x[1],
    reverse=False
)
mitad = len(lista_objetos) // 2

primera_parte = lista_objetos[:mitad]
segunda_parte = lista_objetos[mitad:]

print("primera_parte: ", primera_parte)
print("segunda_parte: ", segunda_parte)

particiones = []
for i in range(len(primera_parte)):
    particiones.append([segunda_parte[i], primera_parte[i]])

print("particiones:", particiones)
suma_objetivo = obtener_suma_de_valores_en_el_indice(lista_objetos, random.randint(1, 2**len(lista_objetos)))

# comentar esto si no es una prueba, va por todas las combinaciones
# obtiene su suma e intenta llegar al valor por el cubo

for eleccion_de_muestra in range(2**(len(lista_objetos))):
    punto_de_partida = [[1,1] for i in particiones]
    suma_objetivo = obtener_suma_de_valores_en_el_indice(lista_objetos, eleccion_de_muestra)
    print("particiones: ", particiones)
    i = 1
    while i < 24 and obtener_suma_de_particiones(particiones, punto_de_partida) != suma_objetivo:
        punto_de_partida = proxima_direccion(particiones, punto_de_partida, suma_objetivo)
        i = i + 1
    print("solucion: ", obtener_letras_de_particiones(particiones, punto_de_partida), obtener_suma_de_particiones(particiones, punto_de_partida))

    if (suma_objetivo != obtener_suma_de_particiones(particiones, punto_de_partida)):
        print("Error: no se llego a la solucion:")
        break
# si llega a la opcion donde estan todos los elementos y no dice Error
# significa que soluciona el problema dada la entrada

# print(lista_objetos)
if suma_objetivo == obtener_suma(lista_objetos, [1 for l in lista_objetos]):
    print("solucion:", lista_objetos)

