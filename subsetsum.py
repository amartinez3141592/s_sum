import math
import random

def greedy_subset_sum(nums, target):
    # Sort descending to pick the largest numbers first
    sorted_nums = sorted(
        lista_objetos.copy(),
        key=lambda x: x[1],
        reverse=False
    )
    subset = []
    current_sum = 0

    for etiqueta, num in sorted_nums:
        if current_sum + num <= target:
            subset.append((etiqueta, num))
            current_sum += num
        if current_sum == target:
            return subset

    # May return False even when an exact subset exists
    return subset

# estas soluciones buscan la solucion en los subbloques ignorando la solucion greedy
# por un tema de orden no puede recorrer la solucion greedy sin dejar de ser polinomial

# base
# 1 1 0
# 1 1 1
def solucionS(maximo, n, V):
    if n == 2:
        if V[2][1]+V[1][1] == maximo:
            return [V[2][0], V[1][0]]
        else:
            return [V[2][0], V[1][0], V[0][0]]
    else:
        if V[n][1] + V[2][1] + V[1][1] > maximo:
            return solucionS(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionS(maximo - V[n][1], n-1, V)

# base
# 1 0 0
# 1 0 1
def solucionQ(maximo, n, V):
    if n == 2:
        if V[2][1] == maximo:
            return [V[2][0]]
        else:
            return [V[2][0],V[0][0]]
    else:
        if V[n][1] + V[2][1] > maximo:
            return solucionQ(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionQ(maximo - V[n][1], n-1, V)
    
# base
# 0 1 0
# 0 1 1
def solucionP(maximo, n, V):
    if n == 2:
        if V[1][1] == maximo:
            return [V[1][0]]
        else:
            return [V[1][0], V[0][0]]
    else:
        if V[n][1] + V[1][1] > maximo:
            return solucionP(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionP(maximo - V[n][1], n-1, V)

# base
# 0 0 0
# 0 0 1    
def solucionO(maximo, n, V):
    if n == 2:
        if V[0][1] == maximo:
            return [V[0][0]]
        else:
            return []
    else:
        if V[n][1] > maximo:
            return solucionO(maximo, n-1, V)
        else:
            return [V[n][0]] + solucionO(maximo - V[n][1], n-1, V)
    

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
 
    # ("L", 1542),  
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

print(lista_objetos)

# j=1
# while j < 100: 
#obtenemos suma
suma_random = obtener_suma_de_valores_aleatorios(lista_objetos)
suma_random= 64

print("==")
print("COMIENZO")
print("==")

O=solucionO(suma_random,len(lista_objetos)-1, lista_objetos)
P=solucionP(suma_random,len(lista_objetos)-1, lista_objetos)
Q=solucionQ(suma_random,len(lista_objetos)-1, lista_objetos)
S=solucionS(suma_random,len(lista_objetos)-1, lista_objetos)

sumaO = obtener_suma_con_letras(lista_objetos, O)
sumaP = obtener_suma_con_letras(lista_objetos, P)
sumaQ = obtener_suma_con_letras(lista_objetos, Q)
sumaS = obtener_suma_con_letras(lista_objetos, S)

if sumaO == suma_random:
    print("solucion O encontrada!")
    print(O,sumaO)
elif sumaP == suma_random:
    print("solucion P encontrada!")
    print(P,sumaP)
elif sumaQ == suma_random:
    print("solucion Q encontrada!")
    print(Q,sumaQ)
elif sumaS == suma_random:
    print("solucion S encontrada!")
    print(S,sumaS)
else:
    # hago greedy porque la solucion es una combinacion de los elementos mas chicos posibles
    # porque cuando elijo entre A[n] y A[n-1]...A[1] puede ser que me convenga elegir la segunda y por hipotesis de orden no va por ahi
    print("solucion greedy es la solucion a menos de una diferencia de la segunda fila paso base")
    entrada = greedy_subset_sum(lista_objetos, suma_random)
    suma = obtener_suma(entrada, [1 for l in entrada])
    
    if suma == suma_random:
        print("S no exploro: ", [l[0] for l in entrada], suma_random)
    elif suma - lista_objetos[1][1] == suma_random:
        print("Q no exploro: ", [l[0] for l in entrada if l != lista_objetos[1]], suma_random)
    elif suma - lista_objetos[2][1] == suma_random:
        print("P no exploro: ", [l[0] for l in entrada if l != lista_objetos[2]], suma_random)
    elif suma - lista_objetos[2][1] - lista_objetos[1][1] == suma_random:
        print("O no exploro: ", [l[0] for l in entrada if l != lista_objetos[2] and l != lista_objetos[1]], suma_random)

# if sumaO != suma_random and sumaP != suma_random and sumaQ != suma_random and sumaS != suma_random:
#     print("error")
#     break

# j = j + 1