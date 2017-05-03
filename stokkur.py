from Hrutar.blib import indexOfNth
from random import choice, shuffle, randint
from Hrutar.hrutar import *
stdstokk = []
nofn = []
stadir = []
with open("Hrutar.txt", "r") as f:
    for x in f:
        line = "".join(x.split("\n"))
        if line[indexOfNth(line, ";") + 1: indexOfNth(line, ";", 2)] != "Nafn":
            nofn.append(line[indexOfNth(line, ";") + 1: indexOfNth(line, ";", 2)])
            stadir.append(line[indexOfNth(line, ";", 2) + 1: indexOfNth(line, ";", 3)])
            stdstokk.append(hrutur(
                line[indexOfNth(line, ";") + 1: indexOfNth(line, ";", 2)],
                line[indexOfNth(line, ";", 2) + 1: indexOfNth(line, ";", 3)],
                float(line[indexOfNth(line, ";", 3) + 1: indexOfNth(line, ";", 4)]),
                int(line[indexOfNth(line, ";", 4) + 1: indexOfNth(line, ";", 5)]),
                float(line[indexOfNth(line, ";", 5) + 1: indexOfNth(line, ";", 6)]),
                int(line[indexOfNth(line, ";", 6) + 1: indexOfNth(line, ";", 7)]),
                float(line[indexOfNth(line, ";", 7) + 1: indexOfNth(line, ";", 8)]),
                int(line[indexOfNth(line, ";", 8) + 1: indexOfNth(line, ";", 9)]),
                int(line[indexOfNth(line, ";", 9) + 1: indexOfNth(line, ";", 10)]),
                float(line[indexOfNth(line, ";", 10) + 1: indexOfNth(line, ";", 11)])
            ))

def makeStokk(lengd):
    nameCount = 0
    newStokk = []
    for x in range(lengd):
        '''
            MG = Mjög Gott
            G = Gott
            ES = Ekkert Spes
            L = Lélegt
        '''
        dist = [
            "MG" if randint(1, 100) <= 25 else "G",
            "G",
            "G" if randint(1, 100) <= 25 else "ES",
            "ES",
            "ES",
            "ES",
            "ES" if randint(1, 100) <= 25 else "L",
            "L"
        ]
        shuffle(dist)
        nafn = choice(nofn)
        stadur = choice(stadir)
        if nafn + ";" + stadur in open("Hrutar.txt").read() or nafn + " af " + stadur in [str(y) for y in newStokk]:
            nameCount += 1
            nafn += str(nameCount)
        newStokk.append(hrutur(
            nafn,
            stadur,
            ((randint(38, 44) if dist[0] == "L" else randint(45, 49)) if dist[0] != "G" else randint(50, 56)) if dist[0] != "MG" else randint(57, 86),
            ((randint(82, 98) if dist[0] == "L" else randint(99, 104)) if dist[0] != "G" else randint(105, 109)) if dist[0] != "MG" else randint(110, 121),
            ((randint(7, 74) / 10 if dist[0] == "L" else randint(75, 80) / 10) if dist[0] != "G" else randint(81, 84) / 10) if dist[0] != "MG" else randint(85, 88) / 10,
            ((randint(0, randint(0, 100)) if dist[0] == "L" else randint(101, 250)) if dist[0] != "G" else randint(251, 450)) if dist[0] != "MG" else randint(451, 1400),
            ((randint(160, 169) / 10 if dist[0] == "L" else randint(170, 175) / 10) if dist[0] != "G" else randint(176, 179) / 10) if dist[0] != "MG" else randint(180, 185) / 10,
            ((randint(95, 105) if dist[0] == "L" else randint(106, 112)) if dist[0] != "G" else randint(113, 120)) if dist[0] != "MG" else randint(121, 135),
            ((randint(90, 109) if dist[0] == "L" else randint(110, 121)) if dist[0] != "G" else randint(122, 130)) if dist[0] != "MG" else randint(131, 150),
            ((randint(81, 83) / 10 if dist[0] == "L" else randint(84, 86) / 10) if dist[0] != "G" else randint(87, 89) / 10) if dist[0] != "MG" else randint(90, 92) / 10,
        ))
        newStokk[-1].setProp(prop.afk, 0) if randint(1, 100) <= 35 else None
    return newStokk