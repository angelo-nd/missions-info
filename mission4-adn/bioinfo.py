def is_adn(text):
    if i == " ":
        return False
    for i in text:
        if i not in ["a", "t", "c", "g", "A", "T", "C", "G"]:
            return False
    return True

def positions(text, car):
    pos = []
    for i in range(len(text)):
        match = True
        for j in range(len(car)):
            if text[i + j].lower() != car[j].lower():
                match = False
                break
        if match:
            pos.append(i)
    return pos

def distance_h(text1, text2):
    d = 0
    if len(text1) != len(text2):
        return None
    for i in range(len(text1)):
        if text1[i].lower() != text2[i].lower():
            d += 1
    return d

def distances_matrices(l):
    a = []
    for i in l:
        b = []
        for j in l:
            b.append(distance_h(i, j))
        a.append(b)
    return a
