# from .assistant import *
import sys
sys.path.insert(0, r'E:\Misc\Code\UCL\missions-info\mission6-assistant')
from assistant import *

def test_assistant_command():
    assert assistant_command() == "file"

def test_assistant_file():
    assert assistant_file() == True, "test_assistant_file failed!"

def test_assistant_info():
    assert assistant_info() == "Le fichier contient 2 lignes et 56 caract res."

def test_assistant_words():
    assert assistant_words() == "Le fichier sera lu comme une liste de mots."

def test_assistant_search():
    assert assistant_search() == True, "test_assistant_search failed!"

def test_assistant_sum():
    assert assistant_sum() == 287, "test_assistant_sum failed!"

def test_assistant_avg():
    assert assistant_avg() == "La moyenne des mots est 617.0."

def test_binary_search():
    assert binary_search(1, [(1,2), (3,4)]) == (True, (1,2)), "binary_search failed!"


file = open("all-words.dat", "r")
file.seek(0)
assistant_words()
test_binary_search()
arguments = "theology"
test_assistant_search()
arguments = "sun heat"
test_assistant_sum()