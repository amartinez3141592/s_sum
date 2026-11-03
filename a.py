import math
from pyvis.network import Network


def obtener_orden_de_remplazo(elementos):
    net = Network()
    for e in elementos:
        net.add_node(e[0])

    i = 0
    while i+1 < len(elementos):
        net.add_edge(e)
    
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
    print("Elementos con angulo y ro: ", elementos_con_angulo)
    
    print()

    elementos_ordenados_por_angulo_creciente = sorted(
        elementos_con_angulo,
        key=lambda x: x["angulo"],
        reverse=False
    )
    print("Elementos ordenados: ", elementos_ordenados_por_angulo_creciente)
    print()
    
    particiones = particionado(elementos_ordenados_por_angulo_creciente)
    print("Particiones: ", particiones)

    ordenes_de_remplazo =
    print("Particiones: ", particiones)

    
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

knapsack_p(capacidad_mochila, lista_objetos)
print("=== pol con peso ===")

print(f"Valor Máximo Total: {valor_total}")
print(f"Valor Peso Total: {peso_total}")
print(f"Objetos seleccionados (etiqueta): {seleccionados}\n")
