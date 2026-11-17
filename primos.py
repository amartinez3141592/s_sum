import math

A_3_bits = [1,2,3,5]
primos = [1,2,3,5]
#tope de numeros de primos en resultado
tope=50

# maximo corrimiento de bits
max_corrimientos=22
idx_primo_sin_correr=0

while idx_primo_sin_correr< len(primos) and idx_primo_sin_correr < tope:
    primo_sin_correr= primos[idx_primo_sin_correr]
    if primo_sin_correr != 2:
        for primo_corrido in A_3_bits:
            if primo_corrido != primo_sin_correr:
                for corrimiento in range(primo_sin_correr.bit_length()+1, max_corrimientos):
                    primo_candidato = primo_corrido * (2**corrimiento) + primo_sin_correr
                    
                    # esta parte es conjetura, vi que siempre en este caso siempre
                    # hay un 3 5 o 7 que determina si es primo o no si 
                    if primo_candidato % 3 != 0 and \
                            primo_candidato % 5 != 0 and \
                            primo_candidato % 7 != 0:
                        print("a.primo sin correr: ",primo_corrido,"primo corrido: ", primo_sin_correr,"cantidad: ", corrimiento, "primo: ", primo_candidato)
                        primos.append(primo_candidato)
                   
    idx_primo_sin_correr += 1

primos=list(set(primos))
print("primos:", sorted(primos))
