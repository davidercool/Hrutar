'''

COPYRIGHT: BENEDIKT ARON SIGURÞÓRSSON

ÞETTA SKJAL INNIHELDUR GANGATÝPUR SEM BENEDIKT A. SIGURÞÓRSSON BJÓ TIL

'''


#In case range based Btypes are given an incorrect range
class RangeError(Exception):
    def __init__(self, *args, **kwargs):
        pass

'''

BType Rules:
    All BTypes are represented as follows: <?!BTYPE!?>i: #[Three digit index]

'''

BTypes = ("<?!BTYPE!?>i: #001")


class cNum:
    "cNum:\n\tA Btype representing a circular integer with a min - max range in which a value can exist.\n\tBtype representation: <?!BTYPE!?>i: #001\n\tMore info at: placeholderWebsite.com'"
    def __init__(self, MIN, MAX, VAL):
        if MIN > MAX:
            raise RangeError("\n\tIncorrect range:\n\t\tMIN: " + str(MIN) + " is bigger than MAX: " + str(MAX)) #Range must be from low to high
        self.__min = MIN
        self.__max = MAX
        self.__val = ((VAL - MIN) % ((MAX + 1) - MIN)) + MIN    #Forces numbers into the range of the cNum
    def val(self):  #Returns the value
        return self.__val
    def min(self):  #Returns the minimum
        return self.__min
    def max(self):  #Returns the maximum
        return self.__max
    def self(self, newVal = None): #Returns a string containing all info on the cNum such as min, max, value, range and Btype representation, used to shift info from one cNum to another or one Btype to another
        return "<?!BTYPE!?>i: #001\t{\tMIN: " + str(self.__min) + ", MAX: " + str(self.__max) + ", VAL: " + (str(self.__val) if newVal is None else str(cNum(self.__min, self.__max, newVal))) + ", range: " + str([x for x in range(self.__min, self.__max + 1)]) + "\t}"
    def __set__(self, instance, value):
        if type(value) == int or type(value) == float or type(value) == cNum:
            self.__val = cNum(self.__min, self.__max, int(value))
        else:
            raise ValueError("Cannot set <?!BTYPE!?>i: #001 to " + str(type(other)))

    def __get__(self):
        return self.__val
    def __lshift__(self, other):    #Shifts info between cNums
        if type(other) == cNum:
            try:
                self.__min = int(other.self()[other.self().index("MIN: ") + 5: other.self().index(", MAX: ")])
                self.__max = int(other.self()[other.self().index(", MAX: ") + 7: other.self().index(", VAL: ")])
                self.__val = int(other.self()[other.self().index(", VAL: ") + 7: other.self().index(", range: ")])
            except ValueError:
                raise ValueError("Incorrect usage of <?!BTYPE!?>i: #001:\n\t<?!BTYPE!?>i: #001 does not recognize " + other)
        elif type(other) == str and "<?!BTYPE!?>i: #001" in other:
            try:
                self.__min = int(other[other.index("MIN: ") + 5: other.index(", MAX: ")])
                self.__max = int(other[other.index(", MAX: ") + 7: other.index(", VAL: ")])
                self.__val = int(other[other.index(", VAL: ") + 7: other.index(", range: ")])
            except ValueError:
                raise ValueError("Incorrect usage of <?!BTYPE!?>i: #001:\n\t<?!BTYPE!?>i: #001 does not recognize " + other)
        elif "<?!BTYPE!?>i: " in other:
            raise ValueError("Incorrect use of <?!BTYPE!?>:\n\t" + other + " is not a recognisable Btype to <?!BTYPE!?>i: #001")
        else:
            raise ValueError("Cannot set <?!BTYPE!?>i: #001 to " + str(type(other)))
    def __rshift__(self, other):
        other << self
    def __add__(self, other):
        return cNum(self.__min, self.__max, int(self.__val + float(other)))
    def __sub__(self, other):
        return cNum(self.__min, self.__max, int(self.__val - float(other)))
    def __mul__(self, other):
        return cNum(self.__min, self.__max, int(self.__val * float(other)))
    def __truediv__(self, other):
        return cNum(self.__min, self.__max, int(self.__val / float(other)))
    def __mod__(self, other):
        return cNum(self.__min, self.__max, int(self.__val % float(other)))
    def __pow__(self, power, modulo=None):
        return cNum(self.__min, self.__max, int(self.__val ** float(power)))
    def __and__(self, other):
        return self.__val and int(other)
    def __xor__(self, other):
        return self.__val ^ int(other)
    def __or__(self, other):
        return self.__val or int(other)
    def __eq__(self, other):
        return self.__val == float(other)
    def __gt__(self, other):
        if type(other) == cNum:
            return self.__val > other.val()
        return self.__val > float(other)
    def __lt__(self, other):
        if type(other) == cNum:
            return self.__val < other.val()
        return self.__val < float(other)
    def __ge__(self, other):
        if type(other) == cNum:
            return self.__val >= other.val()
        return self.__val >= float(other)
    def __le__(self, other):
        if type(other) == cNum:
            return self.__val <= other.val()
        return self.__val <= float(other)
    def __ne__(self, other):
        return self.__val != float(other)
    def __repr__(self):
        return str(self.__val)
    __str__ = __repr__
    def __int__(self):
        return self.__val
    def __float__(self):
        return float(self.__val)
    def __neg__(self):
        return self.__val
    def __abs__(self):
        return abs(self.__val)
    __pos__ = __abs__
    def __invert__(self):
        return ~self.__val
    def __complex__(self):
        return complex(self.__val)
    def __iter__(self):
        for x in range(self.__min, self.__max + 1):
            yield x
    def __len__(self):
        return len([x for x in range(self.__min, self.__max + 1)])
    def __contains__(self, item):
        return item in [x for x in range(self.__min, self.__max + 1)]
    def __getitem__(self, item):
        return [x for x in range(self.__min, self.__max + 1)][item]