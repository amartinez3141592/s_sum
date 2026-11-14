import math
import random

# base
# 0 0
# 0 1    
def solucionO(maximo, pos, V, costoTotal):
    if pos == 1:
        if V[0][1] == maximo:
            return [V[0][0]]
        else:
            return [] 
    else:
        if V[pos][1] > maximo:
            return               solucionO(maximo            ,pos-1, V, costoTotal - V[pos][1])
        else:
            # if V[pos][1] + V[pos-1][1] > maximo and costoTotal - V[pos][1] < V[pos][1]:
                # return             solucionO(maximo            ,pos-1, V, costoTotal - V[pos][1])
            # else:
            return [V[pos][0]] + solucionO(maximo - V[pos][1], pos-1, V, costoTotal - V[pos][1])
    

# base
# 1 0
# 1 1
def solucionP(maximo, n, V, costoTotal):
    if n == 1:
        if V[1][1] == maximo:
            return [V[1][0]]
        else:
            return [V[1][0], V[0][0]]
    else:
        if V[n][1] + V[1][1] > maximo:
            return                 solucionP(maximo, n-1, V, costoTotal - V[n][1])
        else:
            return                 solucionP(maximo, n-1, V, costoTotal - V[n][1])

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

# tenemos la lista de objecos
lista_objetos = [
    ("A0", 32),  
    ("A", 30),  
    ("B", 20),  
    ("C", 11),  
    ("D", 3),  
    ("L", 35),  
    # ("N", 1154),  
    # ("T", 20),  
    # ("S", 19),  
    # ("Q", 17),  
    # ("O", 15),  
    # ("P", 1), 
    # ("A", 3),  
    # ("B", 4), 
    # ("E", 5),  
    # ("F", 6),  
    # ("G", 7),  
    # ("H", 8),  
    # ("I", 9),  
    # ("J", 1011),  
    # ("K", 11),  
    # ("M", 13),  
    # ("R", 168),  
]

#tenemos la lista ordenada de objetos decreciente
lista_objetos = sorted(
    lista_objetos,
    key=lambda x: x[1],
    reverse=False
)
valor_total = obtener_suma(lista_objetos, [1 for l in lista_objetos])
print(valor_total)
print(lista_objetos)
# este for es para verificacion de que cubre todo las combinaciones
# la parte interna es la que ejecuta el algoritmo
# en la ejecucion usual no se usa el 2**n ni j
j=1
while j < 2**len(lista_objetos): 
    #obtenemos suma
    suma_random = obtener_suma_de_valores_en_el_indice(lista_objetos, j)
    # suma_random= 64

    print("==")
    print("COMIENZO")
    print("==")

    O=solucionO(suma_random,len(lista_objetos)-1, lista_objetos, valor_total - lista_objetos[1][1])
    P=solucionP(suma_random,len(lista_objetos)-1, lista_objetos, valor_total)

    sumaO = obtener_suma_con_letras(lista_objetos, O)
    sumaP = obtener_suma_con_letras(lista_objetos, P)

    print("O", O,sumaO)
    print("P", P,sumaP)

    if sumaO == suma_random:
        print("solucion O encontrada!")
        print(O,sumaO)
    elif sumaP == suma_random:
        print("solucion P encontrada!")
        print(P,sumaP)

    if sumaO != suma_random and sumaP != suma_random:
        print("error")
        break

    j = j + 1