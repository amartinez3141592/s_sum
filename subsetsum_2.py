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

def obtener_tope(unos, variables):
    if variables == 1:
        return 1
    elif unos == 1:
        return variables-1
    elif unos == variables:
        return 1
    else:
        comb_arriba = math.comb(variables-1, unos)
        comb_abajo = math.comb(variables-1, unos-1)
        
        return comb_arriba + comb_abajo

# funcion recursiva que recorre la tabla segun quiera
def obtenerFila(unos,variables,i):
    if variables == 1:
        if unos == 1:
            return [1]
        else:
            return [0]
    elif unos == 1:
        if i == variables:
            return [1]+[0 for i in range(variables-1)]
        else:
            return [0] + obtenerFila(1,variables-1,i)
    elif unos == variables:
        return [1 for k in range(variables)]
    else:
        comb = math.comb(variables-1, unos)
        if i > comb:
            i = i - comb
            comb = 0 # libero memoria
            return [1] + obtenerFila(unos-1,variables-1, i)
        else:
            comb = 0 # libero memoria
            return [0] + obtenerFila(unos  ,variables-1, i)

lista_objetos = [
    ("L", 35),
    ("A0", 32),  
    ("A", 30),  
    ("B", 20),  
    ("C", 11),  
    ("D", 3),  
]
lista_objetos = sorted(
    lista_objetos,
    key=lambda x: x[1],
    reverse=False
)
suma_objetivo = obtener_suma_de_valores_en_el_indice(lista_objetos, random.randint(1, 2**len(lista_objetos)))
suma_objetivo = 38
print(lista_objetos)
if suma_objetivo == obtener_suma(lista_objetos, [1 for l in lista_objetos]):
    print("solucion:", lista_objetos)

#algoritmo iterativo en el numero de letras y por cada numero de letras
# busca en el espacio de soluciones 2**n cortando por mitades que pasa a ser orden n
# orden n la parte interna del for

for numero_de_unos in range(1,len(lista_objetos)):
    tope = obtener_tope(numero_de_unos, len(lista_objetos)) +1
    print("tope:", tope)
    piso = 1
    # idx = 0
    # and idx < 10:
    while tope >= piso: 
        indice = math.floor(( tope + piso )/2)
        eleccionEnEseIndice = obtenerFila(numero_de_unos, len(lista_objetos), indice)
        sumaLocal = obtener_suma(lista_objetos, eleccionEnEseIndice)
        print("DEBUG:", 'letras:', obtener_letras(lista_objetos, eleccionEnEseIndice), 'indice:', eleccionEnEseIndice, 'suma:', sumaLocal, 'tope:', tope, 'piso:', piso, 'index:', math.floor(( tope + piso )/2))
        if (sumaLocal < suma_objetivo):
            piso = indice + 1
        elif suma_objetivo < sumaLocal:
            tope = indice - 1
        else:
            print("solucion_:",
                obtener_letras(lista_objetos, eleccionEnEseIndice),
                obtener_suma(lista_objetos, eleccionEnEseIndice)
            )
            break
        # idx = idx + 1

    print() 

print(obtenerFila(2, 6, 1))
print(obtenerFila(2, 6, 2))
print(obtenerFila(2, 6, 3))
print(obtenerFila(2, 6, 4))
print(obtenerFila(2, 6, 5))
print(obtenerFila(2, 6, 6))
print(obtenerFila(2, 6, 7))
print(obtenerFila(2, 6, 8))
print(obtenerFila(2, 6, 9))
print(obtenerFila(2, 6, 10))
print(obtenerFila(2, 6, 11))
print(obtenerFila(2, 6, 12))
print(obtenerFila(2, 6, 13))
print(obtenerFila(2, 6, 14))
print(obtenerFila(2, 6, 15))