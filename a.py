import math
from pyvis.network import Network


def obtener_palabra_de_particiones(particiones):
    l = []
    for pcc in particiones_con_costo:
        for elemento in pcc["particion"]:
            l.append(elemento["nombre"])
    return l
# palabra es la lista de nombre, costo, valor,....
def pertenece(nombre, palabra):
    for l in palabra:
        if l == nombre:
            return True
    return False

# palabra es la lista de nombre, costo, valor,....
def anterior(letra, orden_c, palabra):
    opciones_c = []
    opciones_v = []
    for edge in orden_c.edges:
        if (edge['from'] == letra["nombre"]) and (not pertenece(edge["to"], palabra)):
            opciones_c.append({
                "nombre": edge["to"],
                "valor": edge["value"]
            })
    minimo = opciones_c[0]
    for opcion in opciones_c:
        if minimo["valor"] > opcion["valor"]:
            minimo = opcion

    return minimo


# palabra es la lista de nombre, costo, valor,....
def costo_de_palabra(palabra):
    suma = 0
    for l in palabra:
        suma = suma + l["valor"]
    return suma

# palabra es la lista de nombre, costo, valor,....
def proxima_palabra(palabra, orden_c):
    opciones = []

    # no es necesario, se hace en el siguiente while
    # for letra_a_quitar in palabra:
    #     palabra_mas_chica = []
    #     for letra in palabra:
    #         if (letra != letra_a_quitar):
    #             palabra_mas_chica.append(letra)
    #     opciones.append(palabra_mas_chica)
    print(palabra)
    for letra_a_remplazar in palabra:
        palabra_mas_chica = []
        bajada = 0
        for letra in palabra:
            if (letra == letra_a_remplazar):
                if anterior(letra, orden_c, palabra)["nombre"] != "null":
                    palabra_mas_chica.append(anterior(letra, orden_c, palabra))
                bajada = anterior(letra, orden_c, palabra)["valor"]
            else:
                palabra_mas_chica.append(letra)
        opciones.append({
            "palabra": palabra_mas_chica,
            "bajada":  bajada
        })
        
    opcion_min = opciones[0] 
    for opcion in opciones:
        if opcion_min["bajada"] > opcion["bajada"]:
            opcion_min = opcion
    return opcion_min

def obtener_orden_de_remplazo_en_costo(particiones):
    ordenes = []
    for elementos in particiones:    
        net = Network()
        for e in elementos:
            net.add_node(e["nombre"])
            
        net.add_node("null")

        i = 0
        while i+1 < len(elementos):
            net.add_edge(elementos[i+1]["nombre"], elementos[i]["nombre"],
            value=((elementos[i+1]["costo"]-elementos[i]["costo"])**2)+ ((elementos[i+1]["valor"]-elementos[i]["valor"])**2))
            i = i +1
        i = 0
        while i < len(elementos):
            net.add_edge(elementos[i]["nombre"], "null", value=elementos[i]["costo"])
            i = i +1
        # net.show("grafo_nombres.html")
        # print(net)
        ordenes.append(net)
    return ordenes

def particionado(elementos):
    L = []
    L.append([elementos[0]])
    posicionDelPuntoAnterior=0
    j=1 # indice del punto
    i=0 # nivel actual
    while j<len(elementos):
        if elementos[j]["ro"] > elementos[posicionDelPuntoAnterior]["ro"]:
            L[i].append(elementos[j])
        else:
            i = i + 1
            L.append([elementos[j]])
        j = j + 1
    return L

def knapsack_p(capacidad, elementos):
    elementos_con_angulo = []
    for nombre, costo, valor in elementos:
        elementos_con_angulo.append({
            "nombre": nombre,
            "costo": costo,
            "valor": valor,
            "angulo": math.atan(costo/valor),
            "ro": math.sqrt((costo*costo)+(valor*valor)),
        })
    # print("Elementos con angulo y ro: ", elementos_con_angulo)
    
    # print()

    elementos_ordenados_por_angulo_creciente = sorted(
        elementos_con_angulo,
        key=lambda x: x["angulo"],
        reverse=False
    )
    # print("Elementos ordenados: ", elementos_ordenados_por_angulo_creciente)
    # print()
    
    particiones = particionado(elementos_ordenados_por_angulo_creciente)
    # print("Particiones: ", particiones)

    ordenes_de_remplazo_en_c = obtener_orden_de_remplazo_en_costo(particiones)
    # print("ordenes_de_remplazo: ", ordenes_de_remplazo)
    
    particiones_con_costo = []

    for i in range(len(particiones)):

        particiones_con_costo.append({
            "particion": particiones[i],
            "costo_disminuido": proxima_palabra(particiones[i], ordenes_de_remplazo_en_c[i])["bajada"],
            "proxima_particion": proxima_palabra(particiones[i], ordenes_de_remplazo_en_c[i])["palabra"]
        })
    # print()
    # print()
    # print("particiones con costo de dar un paso: ", particiones_con_costo)
    
    # calculo el costo de la actual combinacion para tener de referencia
    costo_total = 0
    for p in particiones:
        costo_total = costo_total + costo_de_palabra(p)

    while capacidad < costo_total:

        indice_de_remplazo_efectivo = 0
        for i in range(len(particiones_con_costo)):
            # print("particiones con costo de dar un paso: ", particiones_con_costo[i].keys())
        
            if particiones_con_costo[indice_de_remplazo_efectivo]["costo_disminuido"] > particiones_con_costo[i]["costo_disminuido"]:
                indice_de_remplazo_efectivo = i
        print("indice_de_remplazo_efectivo", indice_de_remplazo_efectivo)

        particion = particiones_con_costo[indice_de_remplazo_efectivo]["proxima_particion"]
        prox_costo_disminuido = proxima_palabra(particion, ordenes_de_remplazo_en_c[indice_de_remplazo_efectivo])["bajada"]
        proxima_particion = proxima_palabra(particion, ordenes_de_remplazo_en_c[indice_de_remplazo_efectivo])["palabra"]
        
        particiones_con_costo[indice_de_remplazo_efectivo] = {
            "particion": particion,
            "costo_disminuido": prox_costo_disminuido,
            "proxima_particion": proxima_particion
        }
        costo_total -= particiones_con_costo[indice_de_remplazo_efectivo]["costo_disminuido"]
    
        print(costo_total)
        # print(particiones_con_costo[0])
        l = []
        for pcc in particiones_con_costo:
            for elemento in pcc["particion"]:
                l.append(elemento["nombre"])
        print(l)
    
    respuesta = []
    for pcc in particiones_con_costo:
        for elemento in pcc["particion"]:
            respuesta.append(elemento["nombre"])
        
    return respuesta
# esta funcion la hizo la ia 
def knapsack_01(capacidad, objetos):
    n = len(objetos)

    tabla = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Construir tabla
    for i in range(1, n + 1):
        etiqueta, peso, valor = objetos[i - 1]

        for c in range(capacidad + 1):
            tabla[i][c] = tabla[i - 1][c]

            if peso <= c:
                tabla[i][c] = max(
                    tabla[i][c],
                    tabla[i - 1][c - peso] + valor
                )

    # Reconstruir solución
    seleccionados = []
    c = capacidad

    for i in range(n, 0, -1):
        if tabla[i][c] != tabla[i - 1][c]:
            seleccionados.append(objetos[i - 1])
            c -= objetos[i - 1][1]

    seleccionados.reverse()

    return tabla[n][capacidad], seleccionados, tabla

# esta funcion la hizo la ia 
def fractional_knapsack(capacity, items):

    items = sorted(
        items,
        key=lambda x: x[2] / x[1],
        reverse=True
    )

    total_value = 0
    total_weight = 0
    selected = []

    for nombre, weight, value in items:
        if total_weight >= capacity:
            break

        remaining = capacity - total_weight
        fraction = min(1, remaining / weight)
        if (fraction == 1):
            total_weight += weight * fraction
            total_value += value * fraction

            selected.append({
                "nombre" : nombre,
                "weight": weight * fraction,
                "value": value * fraction
            })

    return selected, total_weight, total_value

# Configuración de prueba
capacidad_mochila = 50
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
    ("K", 11, 32),  
    ("L", 12, 33),  
    ("M", 13, 34),  
    ("N", 14, 35),  
    ("O", 15, 36),  
    ("P", 16, 37),  
    ("Q", 17, 38),  
    ("R", 18, 39),  
    ("S", 19, 40),  
    ("T", 20, 41)  
]

# Ejecución 0/1
beneficio, seleccionados, tabla = knapsack_01(capacidad_mochila, lista_objetos)
print("=== MOCHILA 0/1 ===")
print(f"Valor Máximo: {beneficio}")
print(f"Objetos seleccionados (etiqueta): {seleccionados}\n")

seleccionados, peso_total, valor_total = fractional_knapsack(capacidad_mochila, lista_objetos)
print("=== fraccional ===")

print(f"Valor Máximo Total: {valor_total}")
print(f"Valor Peso Total: {peso_total}")
print(f"Objetos seleccionados (etiqueta): {seleccionados}\n")

respuesta = knapsack_p(capacidad_mochila, lista_objetos)
print("=== Mochila polinoimial ===")

# print(f"Valor Máximo Total: {valor_total}")
# print(f"Valor Peso Total: {peso_total}")
print(f"Objetos seleccionados (etiqueta): {respuesta}\n")
