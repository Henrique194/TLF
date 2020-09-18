from random import randint

TOTAL_DE_JOGADAS = 50

results = dict([ (1, 0), 
                 (2, 0), 
                 (3, 0),
                 (4, 0),
                 (5, 0),
                 (6, 0) ])

sums = dict([ (3, 0),
              (4, 0),
              (5, 0),
              (6, 0),
              (7, 0),
              (8, 0),
              (9, 0),
              (10, 0),
              (11, 0),
              (12, 0),
              (13, 0),
              (14, 0),
              (15, 0),
              (16, 0),
              (17, 0),
              (18, 0) ])

print("=== LANÇAMENTOS ===\n")
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Lançamento", "Dado 1", "Dado 2", "Dado 3", "Soma"))
print("----------------------------------------------------------------")
for i in range(1, TOTAL_DE_JOGADAS + 1) :
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)
    s = d1 + d2 + d3
    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i, d1, d2, d3, s))

    results[d1] += 1
    results[d2] += 1
    results[d3] += 1
    sums[s] += 1

total = 0
for i in range(1, 7) :
    total += results[i]

print("\n\n")

print("=== OCORRÊNCIA DAS FACES ===\n")
po = 0 
di = 0
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Face", "Ocorrências", "Porcentagem", "Esperado", "Diferênça"))
print("---------------------------------------------------------------------")
for i in range(1, 7) :
    p = round((100 * results[i]) / total, 2)

    d = 0
    if p < 16.67 :
        d = round(16.67 - p, 2)
    else :
        d = round(p - 16.67, 2)

    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i, results[i], p, 16.67, d))

    di += d
print("---------------------------------------------------------------------")
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Soma", total, 100, 100, round(di, 2)))
print("\n\n")

print("=== OCORRÊNCIAS DAS SOMAS ===\n")
print("{:<15}{:<15}{:<15}".format("Soma", "Combinações", "Ocorrência"))
print("----------------------------------------")
j = 1
cp = 0
st = 0
p = [ 1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1 ]
for i in range(3, 19) :
    cp += p[i-3]
    print("{:<15}{:<15}{:<15}".format(i, p[i-3], sums[i]))
    st += sums[i]
print("----------------------------------------")
print("{:<15}{:<15}{:<15}".format("Soma", cp, st))
print("\n\n")

print("=== PORCENTAGEM DAS SOMAS ===\n")
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Soma", "Ocorrências", "Porcentagem", "Esperado", "Diferênça"))
print("---------------------------------------------------------------------")
dt = 0
for i in range(3, 19) :
    p = (100 * sums[i]) / st
    d = 0

    if p < 5.56 :
        d = round(5.56 - p, 2)
    else :
        d = round(p - 5.56, 2)
    dt += d

    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(i, sums[i], p, 5.56, d))
print("---------------------------------------------------------------------")
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Soma", st, 100, 100, dt))
print("\n\n")

print("=== OCORRÊNCIAS DAS SOMAS X SOMAS ===\n")
fmt = "{:<3}|{:<"+str(TOTAL_DE_JOGADAS)+"}({})"
for i in range(3, 19) :
    print(fmt.format(i, '*' * sums[i], sums[i]))

print("\n\n")

print("=== PORCENTAGEM DAS SOMAS X SOMAS ===\n")
for i in range(3, 19) :
    p = int((100 * sums[i]) / st)
    print(fmt.format(i, '*' * p, p))
