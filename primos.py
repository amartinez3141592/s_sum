import math

A_3_bits = [1,2,3,5]
primos = [1,2,3,5]
tope=20
id_j=0
while id_j< len(primos) and id_j < tope:
    j= primos[id_j]

    for i in A_3_bits:
        for corrimiento in range(primos[id_j], primos[id_j] +1):
            if (i*(2**corrimiento)) > j and \
                    not ((i*(2**corrimiento)) % j != 0.0) and \
                    corrimiento + 1 in primos:
                    # True:

                print("a ",i,j,corrimiento,i*(2**corrimiento)+j, "primo")
                primos.append(i*(2**corrimiento)+j)
            elif j > i*(2**corrimiento)):
                print("ERROR")
    
    id_j+=1

primos=list(set(primos))
print("primos:", sorted(primos))
