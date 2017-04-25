from enum import Enum

class prop(Enum):
    nafn = 0
    stad = 1
    kilo = 2
    mjolk = 3
    ull = 4
    afk = 5
    leg = 6
    frjo = 7
    bak = 8
    mal = 9

class hrutur:
    def __init__(self, nafn, stad, kilos, mjolk, ull, afk, leg, frjo, bak, mal):
        self.__props = dict()
        self.__props[prop.nafn] = nafn
        self.__props[prop.stad] = stad
        self.__props[prop.kilo] = kilos
        self.__props[prop.mjolk] = mjolk
        self.__props[prop.ull] = ull
        self.__props[prop.afk] = afk
        self.__props[prop.leg] = leg
        self.__props[prop.frjo] = frjo
        self.__props[prop.bak] = bak
        self.__props[prop.mal] = mal
    def property(self, PROP):
        return self.__props[PROP]
    def battle(self, other, PROP):
        return ("Vann" if self.__props[PROP] > other.property(PROP) else "Tap") if self.__props[PROP] != other.property(PROP) else "Jafn"
    def __repr__(self):
        return self.__props[prop.nafn] + " af " + self.__props[prop.stad]