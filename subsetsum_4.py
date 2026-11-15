import math
import random

# orden n*logn siendo n la cantidad de elemntos de Z
def obtener_Zarriba_y_Zabajo_por_promedio(n_dado, suma_divisoria, Z):
    Z = sorted(
        Z,
        key=lambda x: x[1],
        reverse=False
    )
    Z_arriba = []
    Z_abajo = []
    i = 0
    while i < len(Z) and Z[i][1] <= (suma_divisoria/n_dado):
        # print("P: ", Z[i][0] ," distancia: ", (Z[i][1] - (suma/n_dado)))
        Z_abajo.append((Z[i][0], Z[i][1], abs(Z[i][1] - (suma_divisoria/n_dado))))
        i += 1

    while i < len(Z):
        Z_arriba.append((Z[i][0], Z[i][1], abs(Z[i][1] - (suma_objetivo/n_dado))))
        i += 1
    Z_abajo.reverse()

    return Z_abajo, Z_arriba


# orden n*n*n*logn siendo n la cantidad de elemntos de Z
def solucion_por_promedio(n_dado, suma_objetivo, Z):
    Z_abajo, Z_arriba = obtener_Zarriba_y_Zabajo_por_promedio(n_dado, suma_objetivo, Z)

    # no hay solucion con este n si el promedio no tiene elementos en alguno de los lados
    if (len(Z_abajo) == 0 or len(Z_arriba) == 0) and n_dado != 1:
        print("n_dado imposible por simetria: ", n_dado)
        return []

    # print(suma, n_dado)
    print("n_dado: ", n_dado, "Prom:", (suma_objetivo/n_dado))
    print("UP: ", Z_abajo)
    print("DOWN: ", Z_arriba)

    idx_Z_abajo = 0
    idx_Z_arriba = 0
    solucionUP = []
    solucionDOWN = []
    num_elecciones = 0

    # empiezo por el elemento mas cercano al promedio y el primer condicional es por el caso borde
    if n_dado < 2:
        busco_menor = True
    elif abs(Z_abajo[0][2]) < abs(Z_arriba[0][2]):
        busco_menor = True
    else:
        busco_menor = False

    while num_elecciones < n_dado:
        if busco_menor and idx_Z_abajo < len(Z_abajo):
            solucionDOWN.append(Z_abajo[idx_Z_abajo])
            idx_Z_abajo += 1
            num_elecciones += 1
        elif (not busco_menor) and idx_Z_arriba < len(Z_arriba):
            solucionUP.append(Z_arriba[idx_Z_arriba])
            idx_Z_arriba += 1
            num_elecciones += 1
        else:
            break
        busco_menor = not busco_menor

    # si hay solucion para el n_dado
    # las soluciones validas para un n tienen al menos un elemento en cada lado
    if sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]) != suma_objetivo:
        print("primera solucion UP: ", solucionUP, sum([l[1] for l in solucionUP]))
        print("primera solucion DOWN: ", solucionDOWN, sum([l[1] for l in solucionDOWN]))


        while num_elecciones <= n_dado and \
                sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]) != suma_objetivo:
           
            Z_abajo_, Z_arriba_ = obtener_Zarriba_y_Zabajo_por_promedio( \
                n_dado, \
                sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]), \
                # [e for e in Z_abajo if e not in solucionDOWN] + [e for e in Z_arriba if e not in solucionUP] 
                solucionUP + solucionDOWN
            )
            print("Z_arriba_", Z_arriba_)
            print("Z_abajo_", Z_abajo_)
            print("prom", ((sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]))/n_dado))
            if suma_objetivo < sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]) and idx_Z_abajo < len(Z_abajo):
                print("a")
                solucionDOWN.pop(0)
                print("solucion UP: ", solucionUP, sum([l[1] for l in solucionUP]))
                print("solucion DOWN: ", solucionDOWN, sum([l[1] for l in solucionDOWN]))
                solucionDOWN.append(Z_abajo[idx_Z_abajo])

                print("solucion UP: ", solucionUP, sum([l[1] for l in solucionUP]))
                print("solucion DOWN: ", solucionDOWN, sum([l[1] for l in solucionDOWN]))

                idx_Z_abajo +=1
                print("solucion UP: ", solucionUP, sum([l[1] for l in solucionUP]))
                print("solucion DOWN: ", solucionDOWN, sum([l[1] for l in solucionDOWN]))

            elif sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]) < suma_objetivo and idx_Z_arriba < len(Z_arriba):
                print("b")
                # diff_intercambio_mayores = sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]) - Z_arriba[idx_Z_arriba - 1] + Z_arriba[idx_Z_arriba]

                # if diff_intercambio_mayores <= suma_objetivo:
                solucionUP.pop(0)
                # solucionUP.remove(Z_arriba[0])
                solucionUP.append(Z_arriba[idx_Z_arriba])
                idx_Z_arriba += 1
                # elif diff_intercambio_mayores < suma_objetivo:
                # else:
                    

                print("solucion UP: ", solucionUP, sum([l[1] for l in solucionUP]))
                print("solucion DOWN: ", solucionDOWN, sum([l[1] for l in solucionDOWN]))
            else:
                break

        print("solucion opt:", solucionUP + solucionDOWN, sum([l[1] for l in solucionUP]) + sum([l[1] for l in solucionDOWN]))
        print()
    return solucionUP + solucionDOWN

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

valor_total = obtener_suma(lista_objetos, [1 for l in lista_objetos])
print(valor_total)
print(lista_objetos)
# este for es para verificacion de que cubre todas las combinaciones
# la parte interna es la que ejecuta el algoritmo
# en la ejecucion usual no se usa el 2**n ni j
j=1
while j < 2**len(lista_objetos): 
    suma_objetivo = obtener_suma_de_valores_en_el_indice(lista_objetos, j)
    # suma_objetivo = 8
    print("==")
    print("COMIENZO")
    print("==")
    sol = main(lista_objetos, suma_objetivo)

    print("Solucion estimada: ", sol, sum([l[1] for l in sol]))

    if sum([l[1] for l in sol]) != suma_objetivo:
        print("error")
        break

    j = j + 1