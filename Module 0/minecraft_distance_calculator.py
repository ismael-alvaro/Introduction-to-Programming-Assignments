import math

X = int(input())
Z = int(input())

H = "{:,.2f}".format(math.sqrt((X - 34) ** 2 + (Z - 220) ** 2))
K = "{:,.2f}".format(math.sqrt((X - 0) ** 2 + (Z - 0) ** 2))
S = "{:,.2f}".format(math.sqrt((X - 140) ** 2 + (Z - 456) ** 2))

print("Distancia para Hogsmeade: " + str(H))
print("Distancia para Kakariko: " + str(K))
print("Distancia para Solitude: " + str(S))
