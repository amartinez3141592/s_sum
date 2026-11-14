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
def proximos_minimos_y_maximos(particiones, maximos, minimos, objetivo):
    puntos_ref = []
    for i in range(len(particiones)):
        muestra = [mins for mins in minimos]
        muestra.pop(i)
        muestra.insert(i, maximos[i])
        print("muestra:", i, muestra, obtener_suma_de_particiones(particiones, muestra))
        puntos_ref.append((i, muestra, obtener_suma_de_particiones(particiones, muestra)))

    idx_max_eje = max(puntos_ref, key=lambda x: x[2])[0]
    idx_min_eje = min(puntos_ref, key=lambda x : x[2])[0]
    print("min:", idx_min_eje)
    print("max:", idx_max_eje)
    print("minimos:", minimos)
    print("maximos:", maximos)
    for i, muestra, suma in puntos_ref:
        if suma == objetivo:
            minimos = muestra
            maximos = muestra
            break
        elif objetivo < suma:
            if minimos[i] != maximos[i]:
                maximos[i] = restar_binario(maximos[i])
        elif suma < objetivo:
            muestra_ = [mins for mins in minimos]
            muestra_.pop(i)
            muestra_.insert(i, sumar_binario(minimos[i]))
            if minimos[i] != maximos[i] and obtener_suma_de_particiones(particiones, muestra_) <= objetivo:
                minimos[i] = sumar_binario(minimos[i])

    return maximos, minimos
lista_objetos = [
    # ("L", 35),
    # ("B", 20),
    ("A", 3),
    ("B", 7),
    ("C", 32),
    ("D", 33),
    ("E", 8),
    ("F", 34),


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
    maximos = [[1,1] for i in particiones]
    minimos = [[0,0] for i in particiones]

    suma_objetivo = obtener_suma_de_valores_en_el_indice(lista_objetos, eleccion_de_muestra)
    print("particiones: ", particiones)
    idx = 0
    while obtener_suma_de_particiones(particiones, minimos) != suma_objetivo and idx < 5:
        maximos, minimos = proximos_minimos_y_maximos(particiones, maximos, minimos, suma_objetivo)
        print(minimos, maximos)
        print("solucion: ", obtener_letras_de_particiones(particiones, minimos), obtener_suma_de_particiones(particiones, minimos))
        idx = idx + 1

    if (suma_objetivo != obtener_suma_de_particiones(particiones, minimos)):
        print("Error: no se llego a la solucion:")
        break
    # si llega a la opcion donde estan todos los elementos y no dice Error
    # significa que soluciona el problema dada la entrada

# # print(lista_objetos)
# if suma_objetivo == obtener_suma(lista_objetos, [1 for l in lista_objetos]):
#     print("solucion:", lista_objetos)

