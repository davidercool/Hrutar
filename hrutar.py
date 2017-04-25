from enum import Enum

class prop(Enum):
    nafn = -1
    stad = 0
    kilo = 1
    mjolk = 2
    ull = 3
    afk = 4
    leg = 5
    frjo = 6
    bak = 7
    mal = 8

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
    def setProp(self, PROP, newVal):
        self.__props[PROP] = newVal
    def battle(self, other, PROP):
        return ("Vann" if self.__props[PROP] > other.property(PROP) else "Tap") if self.__props[PROP] != other.property(PROP) else "Jafn"
    def __repr__(self):
        return self.__props[prop.nafn] + " af " + self.__props[prop.stad]
    __str__ = __repr__