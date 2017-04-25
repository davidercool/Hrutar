'''

COPYRIGHT: BENEDIKT ARON SIGURÞÓRSSON

ÞETTA SKJAL INNIHELDUR FÖLL SEM BENEDIKT A. SIGURÞÓRSSON BJÓ TIL

'''
from BTYPE import *
from enum import Enum

class ANS(Enum):
    yes = 0
    no = 1

def indexOfNth(container, elem = " ", nth = 1):
    if nth == 0:
        return 0
    occ = 0
    for i, x in enumerate(container):
        if x == elem:
            occ += 1
        if occ == nth:
            return i
    if occ < nth:
        return len(container) - 1