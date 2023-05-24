import random
import Mesta
import Nacitani
import Planek
import PraceSHracem
poctah=0
odpocet=0
dobodpoc=0
predpoved=0
prip=1
planek = []
kostka = [1,2,3,4,5,6]
planek = []
datal = []
Pozice=549
silautoku=0
kam=0
GeneralCislo=0
Ziv=0
Penize=0
jmenogenerala=str()
"""Promenne nacitane z txt"""
"""Prisery"""
polePriser = Nacitani.prisera()
PoleSilPriser=Nacitani.silapris()
IndexyPriseryDelka=len(polePriser)-1
"""Prisery(generalove)"""
poleGeneralu=Nacitani.gengen()
silaGeneralu=Nacitani.silagen()
"""Mesta"""
PoleMest=Mesta.mestanazvy()
"""Veci"""
PoleVeci=Nacitani.veci()
PoleSilVeci=Nacitani.vecisila()
IndexTveVeci=random.randint(0,(len(PoleVeci)-1))
TvojeVec=PoleVeci[IndexTveVeci]
TvojeVecSila=PoleSilVeci[IndexTveVeci]
"""Obleceni"""
poleObleceni=Nacitani.obleceni()
poleSilObleceni=Nacitani.oblecenisila()
IndexTvehoObleceni=random.randint(0,(len(poleObleceni)-1))
Ziv=1+int(poleSilObleceni[IndexTvehoObleceni])
print(f"Mas {poleObleceni[IndexTvehoObleceni]}")
"""Tvorba zakladniho planku"""
planek=Planek.start(PoleSilPriser,IndexyPriseryDelka)
"""Tvorba 20 mest na zacatek"""
planek=Mesta.mestazaklad(planek,PoleMest)
"""Tvorba hlavnich mest"""
planek=Mesta.klicovamesta(planek,poleGeneralu,silaGeneralu)
"""Zaklad prichystan-dale kod hry"""






"""Nehraje hrac hraji mesta a zlo
prip(zlo momentalne dobyva)
prozporoma(co mesto hraje)
kam(jake klicove mesto zlo napada)
"""
def TahDaZ(tah):
    global odpocet
    global dobodpoc
    global prip
    global kam
    global GeneralCislo
    global silautoku
    global jmenogenerala
    global planek
    global predpoved
    citah=1
    for i in range(3):
        penize=Mesta.pen(planek)
        nahodnecislo=random.randint(1,3)
        if nahodnecislo==1:
            planek=Mesta.tvorbamest(citah,penize,planek)
        elif nahodnecislo==2:
            Mesta.utok(planek,citah)
        elif nahodnecislo==3:
            Mesta.kolonizace(planek)
    if tah==20:
        predpoved=1
        print("Zlo se prichystalo a chce vest valku s kralovstvim.")
        print("Carodejove ti vzdy oznami za kolik tahu probehne utok a na jake mesto")
        print("Budes mit zpravu pod nazvem predikce, ktera se bude kazde kolo aktualizovat")
    if tah>19:
        if prip==1:
            odpocet=random.randint(50,60)
            dobodpoc=random.randint(10,30)
            kam=random.randint(5,6)
            GeneralSeznamDelka=len(poleGeneralu)
            GeneralSeznamDelka-=1
            GeneralCislo=random.randint(0,GeneralSeznamDelka)
            print(GeneralCislo)
            jmenogenerala=poleGeneralu[GeneralCislo]
            silautoku=silaGeneralu[GeneralCislo]
            for i in planek:
                if i[1]==kam:
                    i[1]=kam*(-1)
                    i[3]=GeneralCislo
                    i[4]=silautoku
            prip=0
        odpocet-=1
        if prip==0:
            for i in planek:
                if i[1]<0:
                    if i[4]==0:
                        i[1]=int(i[1])*(-1)
                        prip=1
        if odpocet<1 and prip==0:
            dobodpoc-=1
            planek=Mesta.dobyvani(planek,dobodpoc)
            if dobodpoc==0:
                prip=1
        Planek.zpravy(kam,odpocet,jmenogenerala,dobodpoc,silautoku)
    Planek.MapaViz(planek,Pozice)



"""Hraje hrac vyuziva soubor PraceSHracem"""
def tahhrac():
    global TvojeVec
    global Pozice
    global Ziv
    global Pozice
    global PoleMest
    global planek
    global Penize
    global TvojeVecSila
    print("Chces si neco otevrit?")
    print("M(mapu)")
    mozotevrit = ["M"]
    if predpoved==1:
        mozotevrit.append("P")
        print("P(predikci)")
    mozotevritstr=""
    for i in mozotevrit:
        mozotevritstr+=i
    odpoved=(input(f"Otevrit({mozotevritstr}): ")).upper()
    if odpoved in mozotevrit:
        if odpoved=="M":
            print(Planek.MapaVizu(planek,Pozice))
        else:
            print(Planek.zpravy(kam,odpocet,jmenogenerala,dobodpoc,silautoku))          
    Pozice=PraceSHracem.Pohyb(Pozice)
    Obsaz=PraceSHracem.DorazilNaMisto(PoleMest,Pozice,planek,polePriser,TvojeVec,poleGeneralu)
    if Obsaz==0:
        Obsaz=Obsaz
    else:
        """Potkani prisery"""
        Rozhodnuti=PraceSHracem.setkspris()
        if Rozhodnuti==1:
            """Boj"""   
            listshodnotami=PraceSHracem.boj(Pozice,Ziv,Penize,TvojeVecSila,planek)
            Penize=listshodnotami[0]
            Ziv=listshodnotami[1]
        elif Rozhodnuti==-5:
            """Nechal se sezrat"""
            Ziv=Rozhodnuti
            while (True):
                Rozhodnuti=Rozhodnuti
    mestotrh=PraceSHracem.mesto(Pozice,planek,Penize,TvojeVec,PoleVeci,PoleSilVeci,TvojeVecSila,poleObleceni,poleSilObleceni,Ziv)
    Penize=mestotrh[0]
    TvojeVec=mestotrh[1]
    TvojeVecSila=mestotrh[2]
    Ziv=mestotrh[3]
    if Ziv==0:
        return(1)
    else:return(0) 



"""Spousti TahDaZ a tahhrac"""
def hra():
    tah=0
    konechry=0
    while konechry==0:
        TahDaZ(tah)
        Planek.MapaViz(planek,Pozice)
        konechry=tahhrac()
        tah+=1
hra()
"""Hra skoncila vypisuje kontolni udaje"""  
print(poctah)
print("Kontrola penez")
penize=Mesta.pen(planek)
print(penize)
print("Kontrola penez")
with open ("Kontrola.txt","w") as f1:
    f1.write(str(planek))
            
