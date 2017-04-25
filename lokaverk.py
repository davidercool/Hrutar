from Hrutar.stokkur import *
val1 = input("Verlkomin/n í hrútaspilið!\nHvað má bjóða þér að gera?\n1: Spila með venjulegum reglum?\n2: Spila með séhönnuðum reglum?\n3: Sjá reglurnar\n4: Hætta að spila?")
stokk = None
computs = 1
while val1 != "4":
    if val1 == "1":
        stokk = stdstokk
    elif val1 == "2":
        computs = int(input("Hversu margar tölvur villtu keppa á móti?\n"))
        while computs < 1:
            computs = int(input("Það þarf að vera að minsta kosti ein tölva!\nReyndu afur\n"))
        stokklen = int(input("Á stokkurinn að nota einhver venjuleg "))
    if val1 == "3":
        print("Eftir að setja inn reglur")
    elif val1 != "Retry":
        input("Ýttu á 'enter' til þess að byrja!")
    val1 = input("Hvað má bjóða þér að gera?\n1: Spila með venjulegum reglum?\n2: Spila með séhönnuðum reglum?\n3: Sjá reglurnar\n4: Hætta að spila?")

print("Takk fyrir að spila :)")