from Hrutar.stokkur import *
from Hrutar.blib import ANS
val1 = input("Verlkomin/n í hrútaspilið!\nHvað má bjóða þér að gera?\n1: Spila með venjulegum reglum?\n2: Spila með sérhönnuðum reglum?\n3: Sjá reglurnar\n4: Hætta að spila?")
stokk = stdstokk
computs = 1
while val1 != "4":
    if val1 == "2":
        computs = int(input("Hversu margar tölvur villtu keppa á móti?\n"))
        while computs < 1:
            computs = int(input("Það þarf að vera að minsta kosti ein tölva!\nReyndu aftur!\n"))
        stokklen = int(input("Hversu mörg spil eiga að vera í stokkinum?\n"))
        while stokklen % (computs + 1) != 0:
            stokklen = int(input(str(stokklen) + " spila stokkur er ekki deilanlegur með " + str(computs + 1) + " leikmönnum!\nReyndu aftur!\n"))
        temp = input("Villtu nota venjulegu spilin í þessum stokki?\n1: Já?\n2: Nei?\n")
        stdInclude = None
        while True:
            try:
                stdInclude = ANS(int(temp) - 1)
                break
            except ValueError:
                temp = input("' " + temp + " ' Var ekki valkostur!\nReyndu aftur\n")
        if stdInclude == ANS.yes:
            if stokklen < 52:
                stokk = stdstokk[0: stokklen]
            elif stokklen > 52:
                stokk = stdstokk + makeStokk(stokklen - 52)
        else:
            stokk = makeStokk(stokklen)
    if val1 == "3":
        print("Eftir að setja inn reglur")
    else:
        for x in stokk:
            print(x)
        input("Ýttu á 'enter' til þess að byrja!")
    val1 = input("Hvað má bjóða þér að gera?\n1: Spila með venjulegum reglum?\n2: Spila með sérhönnuðum reglum?\n3: Sjá reglurnar\n4: Hætta að spila?")
print("Takk fyrir að spila :)\nLove David (Daddy) Bjarki og Benedikt (Librarian) Aron")