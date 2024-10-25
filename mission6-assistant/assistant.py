command = ""
arguments = ""
file = ""
commandlist = ["file", "info", "words", "search", "sum", "avg", "help", "exit"]

def assistant_command():
    global command
    global arguments
    
    user_response = input("Bonjour, comment puis-je vous aider ?\nCommandes disponibles: file <name>, info, words, search <word>, sum <number1> ... <numbern>, avg <number1> ... <numbern>, help, exit\n")
    command = user_response.split(" ")[0]
    for thing in user_response.split(" ")[1:]:
        arguments += thing + " "
    
def assistant_file():
    global arguments
    global file
    try:
        file = open(arguments, "r")
    except:
        print("Fichier pas trouvé.")

def assistant_info():
    if file == "":
        print("Fichier non ouvert.")
        return
    
    lines_number = len(file.readlines())
    caracters_number = len(file.read())
    print("Le fichier " + arguments + " contient " + str(lines_number) + " lignes et " + str(caracters_number) + " caractères.")
    

    