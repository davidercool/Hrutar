from Hrutar.stokkur import *  # Fyrir hluti eins og stdstokk og makeStokk()
from Hrutar.blib import ANS, RPS  # ANS og RPS Enumin
from Hrutar.BTYPE import cNum  # fyrir cNum breytuna
val1 = input("Verlkomin/n í hrútaspilið!\nHvað má bjóða þér að gera?\n1: Spila með venjulegum reglum?\n2: Spila með sérhönnuðum reglum?\n3: Sjá reglurnar\n4: Hætta að spila?\n")  # Valmynd
stokk = stdstokk  # Stilla standard stokk value
stokklen = len(stdstokk)  # Stilla standard stokk lengd
diffi = None  # Hvaða erfiðleik stig er á leiknum
computs = 1  # Fjöldi tölva til að keppa á móti
players = []  # Listi af þeim sem eru að keppa
while val1 != "4":  # Meðan notandi vill ekki hætta
    if val1 == "2":  # Ef það var valið sérstakar reglur
        computs = int(input("Hversu margar tölvur villtu keppa á móti?\n"))  # Stilla fjölda tölva
        while computs < 1:  # Meðan of fáar tölvur voru valdar
            computs = int(input("Það þarf að vera að minsta kosti ein tölva!\nReyndu aftur!\n"))  # Stilla fjölda tölva
        stokklen = int(input("Hversu mörg spil eiga að vera í stokkinum?\n"))  # Stilla lengd stokks
        while stokklen % (computs + 1) != 0:  # Meðan stokklengd er ekki deilanleg með player fjölda
            stokklen = int(input(str(stokklen) + " spila stokkur er ekki deilanlegur með " + str(computs + 1) + " leikmönnum!\nReyndu aftur!\n"))  # Stilla lengd stokks
        temp = input("Villtu nota venjulegu spilin í þessum stokki?\n1: Já?\n2: Nei?\n")  # Vill notandinn nota eitthvað frá stdstokk
        stdInclude = None  # Breyta sem heldur um svarið
        while True:  # Meðan input notanda virkaði ekki
            try:  # Reyndu að lesa svarið
                stdInclude = ANS(int(temp) - 1)  # Reynir að lesa svarið
                break  # Fer úr lykkjunni
            except ValueError:  # Ef svarið var ekki talan 1 eða 2 (eða ef það var ekki tala)
                temp = input("' " + temp + " ' Var ekki valkostur!\nReyndu aftur\n")  # Vill notandinn nota eitthvað frá stdstokk
        if stdInclude == ANS.yes:  # Ef svarið var já
            shuffle(stdstokk)  # Stokkar stokknum
            if stokklen < 52:  # Ef stokklengd er minna en 52
                stokk = stdstokk[0: stokklen]  # stillir stokkinn
            elif stokklen > 52:  # Ef stokklengd er stærri en 52
                stokk = stdstokk + makeStokk(stokklen - 52)  # stillir stokkinn
        else:  # Ef svarið var nei
            stokk = makeStokk(stokklen)  # Býr til nýjann stokk og stillir stokkinn
    if val1 == "3":  # Ef notanda vill lesa reglurnar
        print("Eftir að setja inn reglur")  # Eftir að klára reglurnar
    else:  # Ef ekki var sýnt reglurnar þá má byrja leikinn
        #computs = 2  # Placeholder fyrir jafnteflis tests
        #stokklen = 27  # Placeholder fyrir jafnteflis tests
        #stokk = [hrutur("petur" + str(x), "Magasvið" + str(x), 10, 10, 10, 10, 10, 10, 10, 10) for x in range(25)] + [hrutur("lol", "I win", 9, 9, 9, 9, 9, 9, 9, 9)]  # Placeholder fyrir jafnteflis tests
        #stokklen = 6  # Placeholder fyrir jafnteflis tests
        #stokk = stokk[20:]  # Placeholder fyrir jafnteflis tests
        nafn = input("Hvað heitir þú\n")  # Nafn notanda
        while True:  # Meðan nafn notanda byrjar á "comp"
            if len(nafn) >= 4:  # Ef lengd nafns er 4 eða hærra (þá getur nafnið byrjað á "comp")
                if nafn.lower()[0:4] == "comp":  # Ef nafn byrjar á "comp"
                    nafn = input("Nafnið má ekki byrja á 'comp'.\nReyndu aftur\n")  # Nafn notanda
                else:  # Ef nafn byrjar ekki á "comp"
                    break  # Fer út úr lykkjunni
            else:  # Ef nafn er ekki 4 stafir eða meira
                break  # Fer út úr lykkjunni
        shuffle(stokk)  # Stokkar stokkinn
        players.append(Player(nafn, stokk[0:int(stokklen / (computs + 1))], playerType.user))  # Býr til notanda með rétt skiptum stokk
        del stokk[0:int(stokklen / (computs + 1))]  # Eyðir spilum notanda frá stokk
        for x in range(computs):  # Fjöldi tölva
            players.append(Player("Comp" + str(x + 1), stokk[0:int(stokklen / (computs + 1))], playerType.computer))  # Býr til tölvu með rétt skiptum stokk
            del stokk[0:int(stokklen / (computs + 1))]  # Eyðir spilum tölvu frá stokk
        turn = cNum(0, computs, 0)  # Býr til breytu sem segir hvaða leikmaður á að gera
        temp = input("Hvaða erfiðleikastig villt þú spila með?\n1: Létt?\n2: Venjulegt?\n3: krefjandi?\n4: Erfitt?\n")  # Stillir erfiðleika stig
        while True:  # Meðan rangt erfiðleikstig er valið
            try:  # Reyndu að stilla svarið
                diffi = diff(int(temp))  # Reynir að stilla svarið
                break  # Fer úr lykkjunni
            except ValueError:  # Ef rangt erfiðleikstig er valið
                temp = input("' " + temp + " ' Var ekki valkostur!\nReyndu aftur\n")  # Stillir erfiðleika stig
        pool = []  # Pool af spilum sem leikmaður fær ef hann vinnur
        lost = False
        while True:  # Meðann leikurinn er í gangi
            battleOn = None  # Breyta sem heldur um hvaða eiginleika á að vera að keppa í
            played = []  # breyta sem heldur um spilin sem hafa verið spiluð þessa umferð
            if players[int(turn)].type() == playerType.user:  # Ef notandi á að gera
                print("Þú átt að gera!\nSpilið sem þú drógst er:\n\t\t" + str(players[0].stokk()[0]))  # Valmynd
                print("\t1: Þyngd í kílóum" + (" " * (25 - len("1: Þyngd í kílóum"))) + str(players[0].stokk()[0].property(prop.kilo)))  # Valmynd
                print("\t2: Mjólkurlagni dætra" + (" " * (25 - len("2: Mjólkurlagni dætra"))) + str(players[0].stokk()[0].property(prop.mjolk)))  # Valmynd
                print("\t3: Einkunn ullar" + (" " * (25 - len("3: Einkunn ullar"))) + str(players[0].stokk()[0].property(prop.ull)))  # Valmynd
                print("\t4: Fjöldi afkvæma" + (" " * (25 - len("4: Fjöldi afkvæma"))) + str(players[0].stokk()[0].property(prop.afk)))  # Valmynd
                print("\t5: Einkunn læris" + (" " * (25 - len("5: Einkunn læris"))) + str(players[0].stokk()[0].property(prop.leg)))  # Valmynd
                print("\t6: Frjósemi" + (" " * (25 - len("6: Frjósemi"))) + str(players[0].stokk()[0].property(prop.frjo)))  # Valmynd
                print("\t7: Gerð/þykkt bakvöðva" + (" " * (25 - len("6: Gerð/þykkt bakvöðva"))) + str(players[0].stokk()[0].property(prop.bak)))  # Valmynd
                print("\t8: Einkunn fyrir malir" + (" " * (25 - len("7: Einkunn fyrir malir"))) + str(players[0].stokk()[0].property(prop.mal)))  # Valmynd
                temp = input("Hverju villt þú keppa í?\n")  # Tekur inn valkost
                while True:  # Meðan valkostur er rangur
                    try:  # Reyndu að stilla valkost
                        battleOn = prop(int(temp))  # Reynir að stilla valkost
                        break  # Fer út úr lykkjunni
                    except ValueError:  # Ef valkostur var í boði
                        temp = input("' " + temp + " ' Var ekki valkostur!\nReyndu aftur\n")  # Tekur inn valkost
            else:  # Ef tölvan á að gera
                print(players[int(turn)], "á að gera")  # Prentar hvaða tölva á að gera
                if diffi == diff.easy:  # Ef notandi valdi létt erfiðleikastig
                    fits = []  # Listi sem heldur um fitness allra eiginleika spilsins sem að tölvan dróg
                    for x in list(propNames.keys())[2:]:  # Öll props
                        fits.append((players[int(turn)].stokk()[0].property(x) * 100) / propTops[x])  # Bætir hversu há prósenta eiginleikin er af hæsta mögulega gildi þess eiginleika
                    battleOn = prop(fits.index(min(fits)) + 1)  # Velur eiginleikan með lægsta fitnessið
                elif diffi == diff.normal:  # Ef notandi valdi venjulegt erfiðleikastig
                    battleOn = prop(randint(1, 8))  # Velur eiginleika af handahófi
                elif diffi == diff.advanced:  # Ef notandi valdi venjulegt erfiðleikastig
                    fits = []  # Listi sem heldur um fitness allra eiginleika spilsins sem að tölvan dróg
                    for x in list(propNames.keys())[2:]:  # Öll props
                        fits.append((players[int(turn)].stokk()[0].property(x) * 100) / propTops[x])  # Bætir hversu há prósenta eiginleikin er af hæsta mögulega gildi þess eiginleika
                    fitsCop = copy.copy(fits)  # Býr til shallow copy af fits listanum
                    tops = []  # Listi sem á að halda um top 4 bestu eiginleikana
                    for x in range(4):  # For lykkja sem keyrir 4 sinnum
                        tops.append(max(fitsCop))  # Bætir besta eiginleika úr copylistanum
                        del fitsCop[fitsCop.index(tops[-1])]  # Eyður besta eiginleika úr copy listanum
                    battleOn = prop(fits.index(choice(tops)) + 1)  # Velur eiginleika úr 4 bestu af handahófi
                elif diffi == diff.hard:  # Ef notandi valdi erfitt erfiðleikastig
                    fits = []  # Listi sem heldur um fitness allra eiginleika spilsins sem að tölvan dróg
                    for x in list(propNames.keys())[2:]:  # Öll props
                        fits.append((players[int(turn)].stokk()[0].property(x) * 100) / propTops[x])  # Bætir hversu há prósenta eiginleikin er af hæsta mögulega gildi þess eiginleika
                    battleOn = prop(fits.index(max(fits)) + 1)  # Velur besta eiginleikan
            print("Það er keppt í", propNames[battleOn])  # Prentar hverju er keppt í
            for x in players:  # Allir leikmenn
                if x.playing():  # Ef leimaður tekur þátt í þessari umferð
                    print(x, "spilar:\n\t" + str(x.stokk()[0]) + "\n\t" + battleOn.name + "\t" + str(x.stokk()[0].property(battleOn)))  # Prentar spilið sem verður spilað af gefnum leikmanni
                    played.append(x.draw())  # Dregur spilið og setur það í played listann
            best = played[0]  # Best núverandi spilið
            jafn = False  # Breyta sem heldur um hvort jafntefli sé í gangi
            for x in played:  # Öll spiluð spil
                #print("besta spilið:", best, "fékk:", best.battle(x, battleOn), "á móti:", x)
                if best.battle(x, battleOn) == "Tap":  # Ef besta spilið tapaði
                    jafn = False  # Er ekki jafntefli
                    best.owner().jafn(False)  # Stillir jafnteflis eiginleika eignda besta spilsins
                    x.owner().jafn(False)  # Stillir jafnteflis eiginleika eignda x spilsins
                    best = x  # Besta spilið verður að andstæðings-spilinu
                elif best.battle(x, battleOn) == "Vann":  # Ef besta spilið vann
                    jafn = False  # Er ekki jafntefli
                    best.owner().jafn(False)  # Stillir jafnteflis eiginleika eignda besta spilsins
                    x.owner().jafn(False)  # Stillir jafnteflis eiginleika eignda x spilsins
                pool.append(x)  # Bætir spilinu í sigurvegara pottinn
            for x in played:  # Öll spiluð spil
                if best != x:  # Ef besta spilið er ekki x spilið
                    if best.battle(x, battleOn) == "Jafn":  # Ef var jafntefli með besta spilinu
                        jafn = True  # Er jafntefli
                        best.owner().jafn(True)  # Stillir jafnteflis eiginleika eignda besta spilsins
                        x.owner().jafn(True)  # Stillir jafnteflis eiginleika eignda besta spilsins
                        if len(best.owner().stokk()) == 0 or len(x.owner().stokk()) == 0:  # Ef það er jafntefli á síðasta spili í stokk
                            while True:  # Meðan það er jafntefli í skæri blað steinn
                                if best.owner().type() == playerType.user:  # Ef besta spilið er notandinn
                                    temp = input("Jafntefli á síðasta spili leikmans!\nÞarf að keppa í skæri blað steinn við hvort annað!\n\t1: Steinn?\n\t2: Blað?\n\t3: Skæri?\n")  # Tekur inn valkost
                                    while True:  # Meðan valkostur er rangur
                                        try:  # Reyndu að stilla valkost
                                            best.owner().RPS(RPS(int(temp) - 1))  # Reynir að stilla valkost
                                            break  # Fer út úr lykkjunni
                                        except ValueError:  # Ef valkostur var í boði
                                            temp = input("' " + temp + " ' Var ekki valkostur!\nReyndu aftur\n")  # Tekur inn valkost
                                else:  # Ef besta spilið er tölva
                                    best.owner().RPS(RPS(randint(0, 2)))  # Velur Skæri, blað eða stein að handahófi
                                if x.owner().type() == playerType.user:  # Ef x spilið er notandinn
                                    temp = input("Jafntefli á síðasta spili leikmans!\nÞarf að keppa í skæri blað steinn við hvort annað!\n\t1: Steinn?\n\t2: Blað?\n\t3: Skæri?\n")  # Tekur inn valkost
                                    while True:  # Meðan valkostur er rangur
                                        try:  # Reyndu að stilla valkost
                                            x.owner().RPS(RPS(int(temp) - 1))  # Reynir að stilla valkost
                                            break  # Fer út úr lykkjunni
                                        except ValueError:  # Ef valkostur var í boði
                                            temp = input("' " + temp + " ' Var ekki valkostur!\nReyndu aftur\n")  # Tekur inn valkost
                                else:  # Ef x spilið er tölva
                                    x.owner().RPS(RPS(randint(0, 2)))  # Velur Skæri, blað eða stein að handahófi
                                print(best.owner(), best.owner().RPS().name, "vs", x.owner(), x.owner().RPS().name)  # Hverjir eru að keppa í skæri blað stein
                                if cNum(0, 2, best.owner().RPS().value) - 1 == cNum(0, 2, x.owner().RPS().value):  # Ef best vinnur
                                    print(best.owner(), "vann skæri blað stein")  # Prentar hver vann skæri blað stein
                                    jafn = False  # Er ekki jafntefli
                                    break  # Hætta að spila skæri blað steinn
                                elif cNum(0, 2, best.owner().RPS().value) + 1 == cNum(0, 2, x.owner().RPS().value):  # Ef best tapar
                                    print(x.owner(), "vann skæri blað stein")  # Prentar hver vann skæri blað stein
                                    best = x  # Besta spilið er núna x
                                    jafn = False  # Er ekki jafntefli
                                    break  # Hætta að spila skæri blað steinn
                                elif cNum(0, 2, best.owner().RPS().value) == cNum(0, 2, x.owner().RPS().value):  # Ef það er jafntefli
                                    print("Jafntefli!")  # Prentar að það sé jafntefli
                                else:  # Ef ekkert að ofan gerist
                                    input("Eitthvað fór úrskeyðis")  # Kóðinn ætti ekki að geta komist hingað
            if jafn:  # Ef það er jafntefli
                for x in players:  # Allir leikmenn
                    if not x.jafn():  # Ef leikmaður fékk ekki jafntefli
                        x.playing(False)  # Leikmaður tekur ekki þátt í næstu umferð
                print("Jafntefli!")  # Prentar að það var jafntefli
            if not jafn:  # Ef það er ekki jafntefli
                print(best.owner(), "vann umferðina")  # Prenta eiganda sigursspilssins (prenta sigurvegara)
                best.owner().vann(pool)  # Setja spila pottinn í stokk sigurvegarans
                pool = []  # Tæma pottinn
                for x in players:  # Allir leikmennn
                    x.playing(True)  # Leimaður tekur þátt í næstu umferð
                    #print(x, x.stokk())  # Prenta nafn og stokk leimanns
            for x in players:  # Allir leikmenn
                if len(x.stokk()) == 0:  # Ef stokkur leikmanns er tómur
                    x.lost(True)  # Leikmaður tapaði
            toRemove = []  # Listi af leikmönnum sem á að eyða
            for x, elem in enumerate(players):  # Allir leikmenn
                if elem.lost():  # Ef leikmaður er búinn að tapa
                    if elem.type() == playerType.user:  # Ef notandi tapaði
                        lost = True  # Maður hefur tapað
                        break  # Fara út úr for lykkjunni
                    if players.index(elem) > turn:  # Endurstilling cNumsins
                        turn = cNum(0, turn.max() - 1, turn)  # Endurstilling cNumsins
                    elif players.index(elem) <= turn:  # Endurstilling cNumsins
                        turn = cNum(0, turn.max() - 1, turn - 1)  # Endurstilling cNumsins
                    #print(turn.self())  # Endurstilling cNumsins
                    toRemove.append(elem)  # Bæta leikmanni í eyðslulista
            for x in toRemove:
                print(x, "datt út")  # Prenta leikmann sem tapaði
                del players[players.index(x)]  # Eyða viðeygandi leikmanni frá leikmanna listanum
                print(len(players), "leikmenn eftir")
            if lost:
                print("Þú tapaðir!")
                break
            if len(players) == 1:  # Ef bara einn leikmaður er eftir (ef einhver er búinn að vinna)
                print(players[0], "vann!")
                break  # Hætta leiknum (Fara úr lykkjunni)
            for x in players:  # Allir leikmenn
                print(x, "spil:", len(x.stokk()))  # Prentar hversu mörg spil þeir eiga eftir
            turn += 1  # Leikmanna teljari fer upp
        input("Ýttu á 'enter' til þess að byrja!")  # Temp
    val1 = input("Hvað má bjóða þér að gera?\n1: Spila með venjulegum reglum?\n2: Spila með sérhönnuðum reglum?\n3: Sjá reglurnar\n4: Hætta að spila?\n")  # Valmynd
print("Takk fyrir að spila :)\nLove David (Daddy) Bjarki og Benedikt (Librarian) Aron")  # Prenta þökkunar skilaboð ef er hætt í leiknum