import time

command = ""
arguments = ""
file = ""
commandlist = ["file", "info", "words", "search", "sum", "avg", "help", "exit"]
wordslist = []

def binary_search(name, list_of_names):
  first = 0
  last = len(list_of_names)-1
  found = (False, "")

  while first<=last and found == (False, ""):
    middle = (first + last)//2
    if list_of_names[middle][0] == name:
      found = (True, list_of_names[middle])
    else:
      if name < list_of_names[middle][0]:
        last = middle-1
      else:
        first = middle+1

  return found

def assistant_command():
    global command
    global arguments
    arguments = ""
    
    user_response = input("Tapez une commande.\nTapez \"help\" pour avoir la liste des commandes.\n")
    command = user_response.split(" ")[0]
    for thing in user_response.split(" ")[1:]:
        arguments += thing + " "
    arguments = arguments[:-1]
    
def assistant_file():
    global arguments
    global file
    global wordslist
    wordslist = []
    try:
        file = open(arguments, "r")
        print("Fichier", arguments, "ouvert.")
    except:
        print("Fichier pas trouvé.")

def assistant_info():
    if file == "":
        print("Fichier non ouvert.")
        return

    file.seek(0)
    caracters_number = len(file.read())
    file.seek(0)
    lines_number = len(file.readlines())
    print("Le fichier " + arguments + "contient " + str(lines_number) + " lignes et " + str(caracters_number) + " caractères.")

def assistant_words():
    if file == "":
        print("Fichier non ouvert.")
        return
    
    file.seek(0)
    global wordslist
    try:
        wordslist = [(line.split(',')[0], line.split(',')[1]) for line in file.read().splitlines()]
    except:
        print("ERREUR: Conversion en liste de mots impossible. Vérifiez")
    
    print("Le fichier sera lû comme une liste de mots.")
    
def assistant_search():
    global wordslist
    global arguments
    sorted_wordslist = sorted(wordslist)
    if wordslist == []:
        print("Liste de mots vide. Utilisez la commande \"words\" pour lire le fichier actuel en tant que liste de mots.")
    if len(arguments.split()) != 1:
        print("ERREUR: Plusieurs arguments.\n", arguments, "\nVous ne pouvez que chercher un seul mot à la fois.")
        return
    if binary_search(arguments.split()[0], sorted_wordslist)[0] == True:
        print("Le mot", arguments, "est dans la liste.")
    else:
        print("Le mot", arguments, "n'est pas dans la liste.")
    print(binary_search(arguments, sorted_wordslist))

def assistant_sum():
    global arguments
    if wordslist == []:
        print("Liste de mots vide. Utilisez la commande \"words\" pour lire le fichier actuel en tant que liste de mots.")
        return
    wordssum = 0
    sorted_wordslist = sorted(wordslist)
    for word in arguments.split():
        word2 = word.split(",")[0]
        binary_search_result = binary_search(word2, sorted_wordslist)
        if binary_search_result[0] == False:
            print("ERREUR: Le mot", word2, "n'est pas dans la liste de mots.")
        else:
            wordssum += int(binary_search_result[1][1])
    print("La somme des mots", arguments, "est", wordssum)
        
def assistant_avg():
    global arguments
    if wordslist == []:
        print("Liste de mots vide. Utilisez la commande \"words\" pour lire le fichier actuel en tant que liste de mots.")
        return
    wordsavg = 0
    sorted_wordslist = sorted(wordslist)
    for word in arguments.split():
        word2 = word.split(",")[0]
        binary_search_result = binary_search(word2, sorted_wordslist)
        if binary_search_result[0] == False:
            print("ERREUR: Le mot", word2, "n'est pas dans la liste de mots.")
        else:
            wordsavg += int(binary_search_result[1][1])
    wordsavg /= len(arguments.split())
    
    print("La somme des mots", arguments, "est", wordsavg)

def assistant_help():
    for command in commandlist:
        print(command)

if __name__ == "__main__":
    while True:
        
        assistant_command()
        if command in commandlist:
            if command == "file":
                assistant_file()
            elif command == "info":
                assistant_info()
            elif command == "words":
                assistant_words()
            elif command == "search":
                assistant_search()
            elif command == "sum":
                assistant_sum()
            elif command == "avg":
                assistant_avg()
            elif command == "help":
                assistant_help()
            elif command == "exit":
                print("Au revoir!")
                break
        else:
            print("ERREUR: Commande inconnue.")
        time.sleep(1)