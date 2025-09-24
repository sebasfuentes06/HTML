números=[1,2,2,3,4,4,4,5,6,6,6,6]
conteo = {}
for n in números:
    conteo[n] = conteo.get(n, 0) + 1
    print(conteo)