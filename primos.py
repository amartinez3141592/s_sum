import math

def es_primo(k):
    if k == 1 or k == 2:
        return True, -1
    
    if k % 2 == 0:
        return False, 2
    for i in range(3, int(k**0.5)+1, 2):
        if k % i == 0:
            return False, i
    return True , -1

primos_a = [1,2,3,5,7]
primos_b = [1,2,3,5,7]
#tope de numeros de primos en resultado
tope=30

idx=1

# primo = primos[idx]

# if  idx > 0:
#     print("0a ",idx, ((3 * (2**idx)) + 5), es_primo((3 * (2**idx)) + 5))
#     primos.append((3 * (2**idx)) + 5)

# if ((2 * (2**idx)) + 1) % 3 != 0 and ((2 * (2**idx)) + 1) % 5 != 0 and idx > 1:
#     primos.append((2 * (2**idx)) + 1)
#     print("a ",idx, ((2 * (2**idx)) + 1), es_primo((2 * (2**idx)) + 1))

# if  ((2 * (2**idx)) + 5) % 11 != 0 and ((2 * (2**idx)) + 5) % 7 != 0 and ((2 * (2**idx)) + 5) % 3 != 0 and idx > 3:
#     primos.append((2 * (2**idx)) + 5)
#     print("b ",idx, ((2 * (2**idx)) + 5), es_primo((2 * (2**idx)) + 5))

while idx < len(primos_a) and idx < tope:
    f = idx
    if idx > 0:
        divide, i = es_primo((3 * (2**f)) + 7)
        
        if i == -1:
            print("3*2 **",f," + 7", (3 * (2**f)) + 7, bin((3 * (2**f)) + 7))
        else:
            print("3*2 **",f," + 7", (3 * (2**f)) + 7, bin((3 * (2**f)) + 7), bin(i), "X", f % 3 == 0)
        primos_a.append((3 * (2**f)) + 7)
    
    idx += 1
    primos_a=sorted(list(set(primos_a)))
    # primos_b=sorted(list(set(primos_b)))
print("primos:", sorted(primos_a))
