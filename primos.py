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
tope=33

idx=1

# primo = primos[idx]

# if  idx > 0:
#     print("0a ",idx, ((7 * (2**idx)) + 5), es_primo((7 * (2**idx)) + 5))
#     primos.append((7 * (2**idx)) + 5)

# if ((2 * (2**idx)) + 1) % 3 != 0 and ((2 * (2**idx)) + 1) % 5 != 0 and idx > 1:
#     primos.append((2 * (2**idx)) + 1)
#     print("a ",idx, ((2 * (2**idx)) + 1), es_primo((2 * (2**idx)) + 1))

# if  ((2 * (2**idx)) + 5) % 11 != 0 and ((2 * (2**idx)) + 5) % 7 != 0 and ((2 * (2**idx)) + 5) % 3 != 0 and idx > 3:
#     primos.append((2 * (2**idx)) + 5)
#     print("b ",idx, ((2 * (2**idx)) + 5), es_primo((2 * (2**idx)) + 5))

while idx < len(primos_a) and idx < tope:
    f = idx
    if idx > 0:
        if ((3 * (2**f)) + 5) % 5 != 0:
            divide, i = es_primo((3 * (2**f)) + 5)
            if i == -1:
                print("3*2 **",f," + 5", (7 * (2**f)) + 5, bin((7 * (2**f)) + 5),"","V, bin(f)", bin(f), " count 0: ",  bin((7 * (2**f)) + 5).count("0")-1)
            # if i != -1:
            #     print("3*2 **",f," + 5", (7 * (2**f)) + 5, bin((7 * (2**f)) + 5),"", "|i:", i,"| bin(i):", bin(i), "X, bin(f)", bin(f), " count 0: ",  bin((7 * (2**f)) + 5).count("0")-1)

        primos_a.append((7 * (2**f)) + 5)

    idx += 1
    primos_a=sorted(list(set(primos_a)))
    # primos_b=sorted(list(set(primos_b)))
print("primos:", sorted(primos_a))
