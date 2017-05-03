from enum import Enum
import copy

class playerType(Enum):
    computer = 0
    user = 1

class diff(Enum):
    easy = 1
    normal = 2
    advanced = 3
    hard = 4

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

propNames = {prop.nafn: "Nafn", prop.stad: "Staðsetning", prop.kilo: "Þyngd í kílóum", prop.mjolk: "Mjólkurlagni dætra", prop.ull: "Einkunn ullar", prop.afk: "Fjöldi afkvæma", prop.leg: "Einkunn læris", prop.frjo: "Frjósemi", prop.bak: "Gerð/þykkt bakvöðva", prop.mal: "Einkunn fyrir malir"}

class Player:
    def __init__(self, nafn, Stokk, type):
        self.__nafn = nafn
        self.__stokk = Stokk
        self.__type = type
        self.__lost = False
        self.__jafn = False
        self.__playing = True
        self.__RPS = None
        for x in self.__stokk:
            x.owner(self)
    def type(self):
        return self.__type
    def stokk(self):
        return self.__stokk
    def vann(self, pool):
        for x in pool:
            x.owner(self)
            self.__stokk.append(x)
    def draw(self):
        temp = copy.copy(self.__stokk[0])
        del self.__stokk[0]
        return temp
    def jafn(self, newVal = None):
        self.__jafn = self.__jafn if newVal is None else newVal
        return self.__jafn
    def playing(self, newVal = None):
        self.__playing = self.__playing if newVal is None else newVal
        return self.__playing
    def lost(self, ans = None):
        self.__lost = self.__lost if ans is None else ans
        return self.__lost
    def RPS(self, newVal = None):
        self.__RPS = self.__RPS if newVal is None else newVal
        return self.__RPS
    def __repr__(self):
        return self.__nafn
    __str__ = __repr__

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
        self.__owner = None
    def property(self, PROP):
        return self.__props[PROP]
    def setProp(self, PROP, newVal):
        self.__props[PROP] = newVal
    def owner(self, newOwner = None):
        self.__owner = (self.__owner if newOwner is None else newOwner)
        return self.__owner
    def battle(self, other, PROP):
        return ("Vann" if self.__props[PROP] > other.property(PROP) else "Tap") if self.__props[PROP] != other.property(PROP) else "Jafn"
    def __repr__(self):
        return self.__props[prop.nafn] + " af " + self.__props[prop.stad]
    __str__ = __repr__