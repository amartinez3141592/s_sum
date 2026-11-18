import math

def es_primo(k):
    if k == 1 or k == 2:
        return True
    
    if k % 2 == 0:
        return False
    for i in range(3, int(k**0.5)+1, 2):
        if k % i == 0:
            print("ERROR: divide ", i)
            return False
    return True

A_3_bits = [1,2,3,5,7]
primos = [1,2,3,5,7]
#tope de numeros de primos en resultado
tope=5

# maximo corrimiento de bits
max_corrimientos=22
idx_primo=0
print(1)
print(2)
print(3)
print(5)
print(7)

while idx_primo < len(primos) and idx_primo < tope:
    primo = primos[idx_primo]

    # if ((2 * (2**primo)) + 1) % primo != 0 and primo > 2:
    #     primos.append((2 * (2**primo)) + 1)
    #     print("a ",primo, ((2 * (2**primo)) + 1), es_primo((2 * (2**primo)) + 1))

    # if ((2 * (2**primo)) + 5) % primo != 0 and primo > 2:
    #     primos.append((2 * (2**primo)) + 5)
    #     print("b ",primo, ((2 * (2**primo)) + 5), es_primo((2 * (2**primo)) + 5))

    # el primo tiene que pasar los bits de 5
    if ((3 * (2**primo)) + 5) % 3 == 5 % 3 and primo > 2:
        primos.append((3 * (2**primo)) + 5)
        print("c ", primo, (3 * (2**primo)) + 5, es_primo((3 * (2**primo)) + 5))
    # # el primo tiene que pasar los bits de 5
    
    if ((3 * (2**primo)) + 7) % 3 == 7 % 3 and primo > 2:
        primos.append((3 * (2**primo)) + 7)
        print("d ", primo, (3 * (2**primo)) + 7, es_primo((3 * (2**primo)) + 7))
    
    idx_primo += 1

primos=list(set(primos))
print("primos:", sorted(primos))
