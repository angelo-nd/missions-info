x = int(input("Entrez la valeur du coefficient x : "))
a = int(input("Entrez la valeur du coefficient a : "))
y = int(input("Entrez la valeur du coefficient y : "))
b = int(input("Entrez la valeur du coefficient b : "))
z = int(input("Entrez la valeur du coefficient z : "))
c = int(input("Entrez la valeur du coefficient c : "))

ansx = x ** a
ansy = y ** b
ansz = z ** c

print(ansx, " + ", ansy, " = ", ansz)
if (ansx + ansy) == ansz:
    print('égalitée confirmée')
else:
    print('égalitée non confirmée')