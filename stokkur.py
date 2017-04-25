from Hrutar.blib import indexOfNth
from Hrutar.hrutar import *
stdstokk = []
with open("Hrutar.txt", "r") as f:
    for x in f:
        line = "".join(x.split("\n"))
        stdstokk.append(hrutur(
            line[indexOfNth(line, ";") + 1: indexOfNth(line, ";", 2)],
            line[indexOfNth(line, ";", 2) + 1: indexOfNth(line, ";", 3)],
            line[indexOfNth(line, ";", 3) + 1: indexOfNth(line, ";", 4)],
            line[indexOfNth(line, ";", 4) + 1: indexOfNth(line, ";", 5)],
            line[indexOfNth(line, ";", 5) + 1: indexOfNth(line, ";", 6)],
            line[indexOfNth(line, ";", 6) + 1: indexOfNth(line, ";", 7)],
            line[indexOfNth(line, ";", 7) + 1: indexOfNth(line, ";", 8)],
            line[indexOfNth(line, ";", 8) + 1: indexOfNth(line, ";", 9)],
            line[indexOfNth(line, ";", 9) + 1: indexOfNth(line, ";", 10)],
            line[indexOfNth(line, ";", 10) + 1: indexOfNth(line, ";", 11)]
        ))
def makeStokk(length):
    # Býr til nýjann stokk útfrá lengd sem er gefin
    pass