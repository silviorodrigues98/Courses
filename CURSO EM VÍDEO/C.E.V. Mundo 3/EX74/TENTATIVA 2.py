from random import randint as rt


r1 = r2 = r3 = r4 = r5 = 0
for randoms in range(0, 5):
    random = rt(0, 100)
    if randoms == 0:
        r1 = random
    elif randoms == 1:
        r2 = random
    elif randoms == 2:
        r3 = random
    elif randoms == 3:
        r4 = random
    else:
        r5 = random
randomicos = r1, r2, r3, r4, r5
print("Os números sorteados foram:", randomicos)
print(F"O maior entre eles foi {max(randomicos)}")
print(f"E o menor entre eles foi {min(randomicos)}")
