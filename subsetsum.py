import math
import random


def solucionO(maximo, n, V):
    if n == 2:
        if V[2][1]+V[1][1]+V[0][1] == maximo:
            return [V[2][0], V[1][0], V[0][0]]
        elif V[2][1]+V[1][1] == maximo:
            return [V[2][0],V[1][0]]
        elif V[0][1] == maximo:
            return [V[0][0]]
        else:
            return []
    else:
        if V[n][1] > maximo:
            return solucionO(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionO(maximo - V[n][1], n-1, V)
    

def solucionP(maximo, n, V):
    if n == 2:
        if V[1][1]+V[0][1] == maximo:
            return [V[1][0], V[0][0]]
        else:
            return [V[1][0]]
    else:
        if V[n][1] > maximo:
            return solucionP(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionP(maximo - V[n][1], n-1, V)
    

def solucionQ(maximo, n, V):
    if n == 2:
        if V[2][1]+V[0][1] == maximo:
            return [V[2][0], V[0][0]]
        else:
            return [V[2][0]]
    else:
        if V[n][1] > maximo:
            return solucionQ(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionQ(maximo - V[n][1], n-1, V)
    

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


def obtener_suma_de_valores_aleatorios(tabla):
    random_i = int(random.uniform(0, 2**len(tabla)))
    pertenece = numero_a_lista_fija(random_i, int(math.floor(2**len(tabla))))
    print("#SECRETO: variable local")
    print("indice", random_i)
    print("pertenece", pertenece.reverse())
    L = obtener_letras(tabla, pertenece)
    suma = obtener_suma(tabla, pertenece)
    print(L)
    print(suma)
    print("#SECRETO")
    return suma

# tenemos la lista de objecos
lista_objetos = [
    ("A", 3),  
    ("Z", 3),  
    ("B", 4), 
    ("E", 5),  
    ("F", 6),  
    ("G", 7),  
    ("H", 8),  
    ("I", 9),  
    ("J", 1011),  
    ("K", 11),  
    ("L", 1542),  
    ("M", 13),  
    ("N", 1154),  
    ("O", 15),  
    ("P", 1),  
    ("Q", 17),  
    ("R", 168),  
    ("S", 19),  
    ("T", 20)  
]

#tenemos la lista ordenada de objetos decreciente
lista_objetos = sorted(
    lista_objetos,
    key=lambda x: x[1],
    reverse=False
)

print(lista_objetos)


#obtenemos suma
suma_random = obtener_suma_de_valores_aleatorios(lista_objetos)

print("==")
print("COMIENZO")
print("==")

O=solucionO(suma_random,len(lista_objetos)-1, lista_objetos)
P=solucionP(suma_random,len(lista_objetos)-1, lista_objetos)
Q=solucionQ(suma_random,len(lista_objetos)-1, lista_objetos)

sumaO = obtener_suma_con_letras(lista_objetos, O)
sumaQ = obtener_suma_con_letras(lista_objetos, Q)
sumaP = obtener_suma_con_letras(lista_objetos, P)


if sumaO == suma_random:
    print(O,sumaO)
if sumaP == suma_random:
    print(P,sumaP)
if sumaQ == suma_random:
    print(Q,sumaQ)