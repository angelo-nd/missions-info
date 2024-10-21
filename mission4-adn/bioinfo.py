def is_adn(text):
    if not text.strip():
        return False
    for i in text:
        if i not in ["a", "t", "c", "g", "A", "T", "C", "G"]:
            return False
    return True

def positions(text, car):
    pos = []
    text_len = len(text)
    car_len = len(car)
    for i in range(text_len - car_len + 1):
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

def distances_matrice(l):
    a = []
    for i in l:
        b = []
        for j in l:
            try:
                b.append(distance_h(i, j))
            except:
                b.append(None)
        a.append(b)
    return a
