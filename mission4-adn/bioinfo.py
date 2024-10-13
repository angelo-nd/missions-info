def is_adn(s):
    for i in s:
        if i not in ["a", "t", "c", "g"] or i not in ["A", "T", "C", "G"]:
            return False
    return True

def positions(s, p):
    pos = []
    for i in range(len(s)):
        match = True
        for j in range(len(p)):
            if s[i + j] != p[j]:
                print(s[i + j], "is not equal to", p[j])
                match = False
                break
        if match:
            pos.append(i)
    return pos

def distance_h(s1, s2):
    d = 0
    if len(s1) != len(s2):
        return None
    for i in range(len(s1)):
        if s1[i] != s2[i]:
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
