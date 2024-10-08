# Recherche des racines d'une équation x ** a + y ** b = z ** c
# Angelo Nardo, octobre 2024

solutions = 0
a = int(input("Entrez la valeur du coefficient a : "))
b = int(input("Entrez la valeur du coefficient b : "))
c = int(input("Entrez la valeur du coefficient c : "))
max = int(input("Entrez la valeur maximale pour x, y et z : ")) # un nombre plus grand obtient plus de solutions, mais dure plus longtemps

for x in range(1, max+1):
    for y in range(1, max+1):
        for z in range(1, max+1):
            if (x ** a) + (y ** b) == z ** c: # ici on verifie l'egalité pour chaque x y et z de 1 jusqu'a la valeur donnée par l'utilisateur  
                print("x =", x, " y =", y, " z =", z)
                solutions += 1 # on augmente le nombre de solutions de 1 a chaque fois qu'on en trouve

if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees")