a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
c = int(input("Entrez le troisième nombre : "))

print("Nombres d'origine :")
print("a =", a)
print("b =", b)
print("c =", c)

temp = a
a = b

b = c

c = temp

print("Nombres après permutation :")
print("a =", b)
print("b =", c)
print("c =", a)