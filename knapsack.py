import math
import random

def mochila01_O(Zord, costoM, pos):
    if pos == 1:
        if Zord[0][1] <= costoM:
            return [Zord[0]]
        else:
            return []
    else:
        if Zord[pos][1] > costoM:
            return mochila01_O(Zord, costoM, pos - 1)
        else:
            return [Zord[pos]] + mochila01_O(Zord, costoM - Zord[pos][1], pos - 1)

def mochila01_P(Zord, costoM, pos):
    if pos == 1:
        if Zord[0][1] + Zord[1][1] <= costoM:
            return [Zord[0], Zord[1]]
        else:
            return [Zord[0]]
    else:
        if Zord[pos][1] + Zord[0][1] > costoM:
            return mochila01_P(Zord, costoM, pos - 1)
        else:
            return [Zord[pos]] + mochila01_P(Zord, costoM - Zord[pos][1], pos - 1)
            
def mochila01_Q(Zord, costoM, pos):
    if pos == 1:
        if Zord[0][1] + Zord[1][1] <= costoM:
            return [Zord[1], Zord[0]]
        else:
            return [Zord[1]]
    else:
        if Zord[pos][1] + Zord[1][1] > costoM:
            return mochila01_Q(Zord, costoM, pos - 1)
        else:
            return [Zord[pos]] + mochila01_Q(Zord, costoM - Zord[pos][1], pos - 1)

def mochila_greedy(lista_items, capacidad):
    # 1. Ordenamos la lista de mayor a menor según la relación (valor / peso)
    # item[2] es el valor, item[1] es el peso
    items_ordenados = sorted(lista_items, key=lambda item: item[2] / item[1], reverse=True)
    
    valor_total = 0.0
    objetos_llevados = [] # Para guardar qué metimos y en qué cantidad
    
    # 2. Recorremos los objetos ordenados
    for etiqueta, peso, valor in items_ordenados:
        if capacidad == 0:
            break
            
        if peso <= capacidad:
            # Entra el objeto completo
            capacidad -= peso
            valor_total += valor
            objetos_llevados.append((etiqueta, peso, valor))
            
    return valor_total, objetos_llevados

def knapsack(items, capacidad):
    n = len(items)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        etiqueta, peso, valor = items[i - 1]

        for c in range(capacidad + 1):
            dp[i][c] = dp[i - 1][c]

            if peso <= c:
                dp[i][c] = max(
                    dp[i][c],
                    dp[i - 1][c - peso] + valor
                )

    seleccionados = []
    c = capacidad

    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            item = items[i - 1]
            seleccionados.append(item)
            c -= item[1]

    seleccionados.reverse()

    return dp[n][capacidad], seleccionados

def obtener_letras(tabla, pertenece):
    L = []
    for i in range(len(pertenece)):
        if pertenece[i] == 1:
            L.append(tabla[len(tabla)-i-1][0])
    return L

def numero_a_lista_fija(numero, bits_usados):
    l = [int(bit) for bit in f"{numero:b}"]
    l.reverse()
    return l

def obtener_costo_de_items_aleatorios(tabla):
    random_i = int(random.uniform(0, 2**len(tabla)))
    pertenece = numero_a_lista_fija(random_i, int(math.floor(2**len(tabla))))
    print("#SECRETO: combinacion aleatoria para tomar una muestra")
    print("indice", random_i)
    pertenece.reverse()
    print("pertenece", pertenece)
    L = obtener_letras(tabla, pertenece)
    costo = obtener_costo(tabla, pertenece)
    beneficio = obtener_beneficio(tabla, pertenece)
    print("letras", L)
    print("costo", costo)
    print("beneficio", beneficio)
    print("#SECRETO")
    return costo

def obtener_costo(tabla, pertenece):
    suma = 0
    for i in range(len(pertenece)):
        if pertenece[i] == 1:
            suma += tabla[len(tabla)-i-1][1]
    return suma

def obtener_beneficio(tabla, pertenece):
    suma = 0
    for i in range(len(pertenece)):
        if pertenece[i] == 1:
            suma += tabla[len(tabla)-i-1][2]
    return suma

# tenemos la lista de objecos, etiqueta, peso, valor
lista_objetos = [
    ("A", 10, 60),
    ("B", 20, 100),   
    ("C", 30, 120),     
    ("D", 5, 24),     
    ("E", 5, 24),     
    ("F", 6, 25),     
    ("G", 7, 26),     
    ("H", 8, 28),     
    ("I", 9, 30),     
    ("J", 10, 31),     
    # ("K", 11, 32),     
    # ("L", 12, 33),     
    # ("M", 13, 34),     
    # ("N", 14, 35),     
    # ("O", 15, 36),     
    # ("P", 16, 37),     
    # ("Q", 17, 38),     
    # ("R", 18, 39),     
    # ("S", 19, 40),     
    # ("T", 20, 41) 
]

#tenemos la lista ordenada de objetos decreciente
lista_objetos = sorted(
    lista_objetos,
    key=lambda x: x[2],
    reverse=False
)
lista_objetos = [(e[0], e[1], e[2]) for e in lista_objetos]


print("lista_objetos: ")
print(lista_objetos)
print()

costo_aleatorio = obtener_costo_de_items_aleatorios(lista_objetos)
print()

beneficio_maximo, solucion = knapsack(lista_objetos, costo_aleatorio)
print("algoritmo pseudo polinomial conocido",
    "letras", [l[0] for l in solucion],
    "costo", obtener_costo(solucion,[1 for l in solucion]),
    "beneficio", beneficio_maximo)
print()
beneficio_greedy, solucion = mochila_greedy(lista_objetos.copy(), costo_aleatorio)
print("algoritmo greedy ", " letras", [l[0] for l in solucion],
    "costo", obtener_costo(solucion,[1 for l in solucion]),
    "beneficio", beneficio_greedy)


O = mochila01_O(lista_objetos, costo_aleatorio, len(lista_objetos) - 1)
costo_O = obtener_costo(O, [1 for l in O])
beneficio_O = obtener_beneficio(O, [1 for l in O])

P = mochila01_P(lista_objetos, costo_aleatorio, len(lista_objetos) - 1)
costo_P = obtener_costo(P, [1 for l in P])
beneficio_P = obtener_beneficio(P, [1 for l in P])

Q = mochila01_Q(lista_objetos, costo_aleatorio, len(lista_objetos) - 1)
costo_Q = obtener_costo(Q, [1 for l in Q])
beneficio_Q = obtener_beneficio(Q, [1 for l in Q])

print(" -------------------------------------")
print(" algoritmo polinomial recursivo ")
if beneficio_O == beneficio_maximo or \
    beneficio_P == beneficio_maximo or \
    beneficio_Q == beneficio_maximo:
   print("se llego por solucion recursiva!")
else:
    print("NO se llego por solucion recursiva")
print("O", "letras", obtener_letras(O, [1 for l in O]),
" costo", costo_O, " beneficio", beneficio_O)

print("P"," letras", obtener_letras(P, [1 for l in P]),
" costo", costo_P, " beneficio", beneficio_P)

print("Q", " letras", obtener_letras(Q, [1 for l in Q]),
" costo", costo_Q, " beneficio", beneficio_Q)

print("-------------------------------------")
