import math
import random

# orden n siendo n la cantidad de elemntos de Z
def obtener_Zarriba_y_Zabajo(n_dado, suma, Z):
    Z_arriba = []
    Z_abajo = []

    i = 0
    print(suma, n_dado)
    print("n_dado: ", n_dado, "Prom:", (suma/n_dado))

    while i < len(Z) and Z[i][1] < (suma/n_dado):
        print("P: ", Z[i][0] ," distancia: ", (Z[i][1] - (suma/n_dado)))
        Z_abajo.append((Z[i][0], Z[i][1], abs(Z[i][1] - (suma/n_dado))))
        i += 1

    while i < len(Z):
        Z_arriba.append((Z[i][0], Z[i][1], abs(Z[i][1] - (suma/n_dado))))
        i += 1
    Z_abajo.reverse()
    print(Z_abajo)
    print(Z_arriba)
    return Z_abajo, Z_arriba

# orden m*m siendo m el tamaño de la solucion acotada por el numero de elementos de la entrada
# retorna la solucion completa con una variante comun que es quitar uno de solucionDOWN y agregar uno de Z_arriba
def quitar_menor_y_agregarle_un_mayor(solucion, solucionUP, solucionDOWN, Z_arriba, idx_Z_arriba, suma):
    idx_DOWN = 0
    while idx_DOWN < len(solucionDOWN) and idx_Z_arriba < len(Z_arriba):
        if sum([l[1] for l in solucion]) - solucionDOWN[idx_DOWN][1] + Z_arriba[idx_Z_arriba][1] == suma:
            solucionDOWN.pop(idx_DOWN)
            # union de conjuntos
            return solucionDOWN + solucionUP
        idx_DOWN += 1
    return solucion

# orden n*n*n siendo n la cantidad de elemntos de Z
def solucion_por_promedio(n_dado, suma, Z):
    Z_abajo, Z_arriba = obtener_Zarriba_y_Zabajo(n_dado, suma, Z)
    idx_Z_abajo = 0
    idx_Z_arriba = 0 
    solucionUP = []
    solucionDOWN = []
    solucion = []
    i = 0
    while i < n_dado and idx_Z_abajo < len(Z_abajo) and idx_Z_arriba < len(Z_arriba):
        print(Z_arriba[idx_Z_arriba])
        
        #agrego mas cercano
        if Z_abajo[idx_Z_abajo][2] >= Z_arriba[idx_Z_arriba][2]:
            
            if sum([l[1] for l in solucion]) + Z_arriba[idx_Z_arriba][1] <= suma:
                solucion.append(Z_arriba[idx_Z_arriba])
                solucionUP.append(Z_arriba[idx_Z_arriba])
                idx_Z_arriba += 1
                i += 1
            else:
                break
        else:
            if sum([l[1] for l in solucion]) + Z_abajo[idx_Z_abajo][1] <= suma:
                solucion.append(Z_abajo[idx_Z_abajo])
                solucionDOWN.append(Z_abajo[idx_Z_abajo])
                idx_Z_abajo += 1
                i += 1
            else:
                break
    # si la lista de arriba se termina sigo intentando agregar a los de abajo hasta pasarse en la suma
    while i < n_dado and sum([l[1] for l in solucion]) < suma and idx_Z_abajo < len(Z_abajo):
        if sum([l[1] for l in solucion]) + Z_abajo[idx_Z_abajo][1] <= suma:    
            solucion.append(Z_abajo[idx_Z_abajo])
            solucionDOWN.append(Z_abajo[idx_Z_abajo])
            i += 1
        idx_Z_abajo += 1
    
    # si la lista de arriba se termina sigo intentando agregar a los de abajo hasta pasarse en la suma
    while i < n_dado and sum([l[1] for l in solucion]) < suma and idx_Z_arriba < len(Z_arriba):
        #agrego mas cercano
        if sum([l[1] for l in solucion]) + Z_arriba[idx_Z_arriba][1] <= suma:    
            solucion.append(Z_arriba[idx_Z_arriba])
            solucionUP.append(Z_arriba[idx_Z_arriba])
            i += 1
        idx_Z_arriba += 1

    # si hay solucion para el n_dado
    if len(solucion) > 0:
        print("primera solucion: ", solucion, sum([l[1] for l in solucion]))
        # esta solucion esta siempre por debajo de la solucion verdadera por un cambio de combinacion
        print("idx_Z_abajo",idx_Z_abajo)
        print("idx_Z_arriba",idx_Z_arriba)
        
        if sum([l[1] for l in solucion]) < suma:
            solucion = quitar_menor_y_agregarle_un_mayor(solucion, solucionUP, solucionDOWN, Z_arriba, idx_Z_arriba, suma)

        print("ajuste para n: ", solucion, sum([l[1] for l in solucion]))

    return solucion

def main(lista_objetos, suma_objetivo):
    n_dado = 1
    sol = []
    while n_dado < len(lista_objetos)+1:
        sol = solucion_por_promedio(n_dado, suma_objetivo, lista_objetos)
        print(sol, sum([l[1] for l in sol]))
        if sum([l[1] for l in sol]) == suma_objetivo:
            break
        n_dado += 1
    return sol


def numero_a_lista_fija(numero, bits_usados):
    l = [int(bit) for bit in f"{numero:b}"]
    l.reverse()
    return l

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
    ("A", 1),  
    ("B", 2),  
    ("C", 5),  
    ("D", 7),  
    # ("E", 8),  
    # ("F", 12),  
    # ("G", 14)
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
# este for es para verificacion de que cubre todas las combinaciones
# la parte interna es la que ejecuta el algoritmo
# en la ejecucion usual no se usa el 2**n ni j
j=1
while j < 2**len(lista_objetos): 
    suma_objetivo = obtener_suma_de_valores_en_el_indice(lista_objetos, j)

    print("==")
    print("COMIENZO")
    print("==")
    sol = main(lista_objetos, suma_objetivo)

    print("Solucion estimada: ", sol, sum([l[1] for l in sol]))

    if sum([l[1] for l in sol]) != suma_objetivo:
        print("error")
        break

    j = j + 1