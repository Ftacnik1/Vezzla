import random
kostka = [1,2,3,4,5,6]


"""Funkce pro souboj s priserou (Pocet penez za jeji smrt je odvozen od jeji sily)"""
def boj(Pozice,Ziv,Penize,TvojeVecSila,planek):
    tvujhod=int(random.choice(kostka))
    priseryhod=int(random.choice(kostka))
    print(f"Hodil jsi {tvujhod}")
    print(f"Prisera hodila {priseryhod}")
    if (int(tvujhod)+int(TvojeVecSila))>(int(priseryhod)+int(planek[Pozice][4])):
        print("Zabil jsi priseru.")
        Penize+=4*int(planek[Pozice][4])                       
        planek[Pozice][3]=0
        planek[Pozice][4]=0
        print(f"Mas {Penize} Penez")
        return(Penize,Ziv)
    else:
        print("Prisera te zranila")
        Ziv-=1
        return(Penize,Ziv)
    
"""Zjistuje kam chce hrac jit"""
def Pohyb(Pozice):
    print(Pozice)
    tx=Pozice % 30
    ty= Pozice //30
    kammoznosti =kampohhrac(tx,ty)
    akce = (input(kammoznosti)).upper()
    while akce not in kammoznosti:
        akce = (input(kammoznosti)).upper()
    if akce=="Z":
        Pozice-=1
    if akce=="V":
        Pozice+=1
    if akce=="S":
        Pozice-=30
    if akce=="J":
        Pozice+=30
    return(Pozice)


"""Co se deje kdyz hrac dorazi na jakekoli misto"""
def DorazilNaMisto(PoleMest,Pozice,planek,polePriser,TvojeVec,poleGeneralu):
    misto=PoleMest[planek[Pozice][5]]
    if planek[Pozice][1]==5 or planek[Pozice][1]==-5:
        misto="Univerzitnim meste"
    elif planek[Pozice][1]==6 or planek[Pozice][1]==-6:
        misto="Hlavnim meste"
    elif planek[Pozice][1]==7 or planek[Pozice][1]==-7:
        misto="Zlem meste"
    elif planek[Pozice][1]==8 or planek[Pozice][1]==-8:
        misto="Hlavnim zlem meste"
    
    print(f"Jsi v {misto} a mas {TvojeVec}")
    if planek[Pozice][4]!=0:
        if planek[Pozice][0]==1:
            Prisera=polePriser[(planek[Pozice][3])]
            print(f"Vidis {Prisera}")
            return(1)
        else:
            a=int(planek[Pozice][3])
            Prisera=poleGeneralu[a]
            print(f"Vidis{Prisera}")
            return(1)
    else:
        return(0)
    


"""Vraci kam muze hrac jit(souradnice z tx a ty)"""
def kampohhrac(tx,ty):
    kammoznosti =[]
    if ty>0:
        kammoznosti.append("S")
    if ty<29:
        kammoznosti.append("J")
    if tx>0:
        kammoznosti.append("Z")
    if tx<29:
        kammoznosti.append("V")
    return(kammoznosti)



"""Neni primo boj hrac se setka s priserou a rozhoduje se"""
def setkspris():
    print("Co chces udelat? Zabit priseru, utect, nechat se sezrat: ")
    akce = (input("Z,U,NSS: ")).upper()
    while akce not in ["Z","U","NSS"]:
        akce = (input("Spatna akce, vyber z techto tri Z,U,NSS: ")).upper()
    if akce == "NSS":
        print("Nechal ses sezrat... hra pro tebe konci.")
        return(-5)
    elif akce == "U":
        print("Utekl jsi, zbabelce!")
        if int(random.choice(kostka))>int(random.choice(kostka)+1):
            print(f"Slysis za sebou utikat priseru.")
            akce = (input("Z,NSS: ")).upper()
            while akce not in ["Z","NSS"]:
                akce = input("Spatna akce, vyber z techto dvou Z,NSS: ")
            if akce == "NSS":
                print("Nechal ses sezrat... hra pro tebe konci.")
                return(-5)
            else:
                return(1)
        else: return(2)
    else:
        return(1)
    


"""Hrac nakupuje ve meste"""
def mesto(Pozice,planek,Penize,TvojeVec,PoleVeci,PoleSilVeci,TvojeVecSila,PoleObleceni,PoleSilObleceni,Ziv):
    if planek[Pozice][1]>1 and planek[Pozice][1]<7:
        obchod=[]
        obchodSlovy=[]
        obchodCisly=[]
        obchodCeny=[]
        obchodSily=[]              
        cislozbrane=0
        for i in range(planek[Pozice][1]):
            obchod=(random.randint(0,len(PoleVeci)-1))
            obchodSlovy.append(PoleVeci[obchod])
            obchodCisly.append(cislozbrane)
            obchodCeny.append((int(PoleSilVeci[obchod]))*3)
            obchodSily.append((PoleSilVeci[obchod]))
            cislozbrane+=1
        print("Mas moznost si koupit zbran, jestli chces odejit napis cokoli a zmackni cokoli mimo cisla nize")
        print("Nabidka")
        print(obchodSlovy)
        print("Cislo zbrane")
        print(obchodCisly)
        obchodCislystr=[]
        for h in obchodCisly:
            obchodCislystr.append(str(h))
            cislozbrane+=1  
        print("Cena")
        print(obchodCeny)
        akce = input(obchodCisly)
        if akce not in obchodCislystr:
            print("Nic jsi nekoupil.")
        
        else:
            akce=int(akce)
            if (Penize - int(obchodCeny[akce]))>-1:
                print("Koupeno")
                TvojeVec=obchodSlovy[akce]
                print(TvojeVec)
                Penize-=int(obchodCeny[akce])
                TvojeVecSila=int(obchodSily[akce])

            else:
                print("Mas malo penez")
    if planek[Pozice][1]>1 and planek[Pozice][1]<7:
        obchod=[]
        obchodSlovy=[]
        obchodCisly=[]
        obchodCeny=[]
        obchodSily=[]              
        cislozbrane=0
        for i in range(planek[Pozice][1]):
            obchod=random.randint(0,len(PoleObleceni)-1)
            obchodSlovy.append(PoleObleceni[obchod])
            obchodCisly.append(cislozbrane)
            obchodCeny.append((int(PoleSilObleceni[obchod]))*3)
            obchodSily.append((PoleSilObleceni[obchod]))
            cislozbrane+=1
        print("Mas moznost si koupit odev, jestli chces odejit napis cokoli a zmackni cokoli mimo cisla nize")
        print("Nabidka")
        print(obchodSlovy)
        print("Cislo obleceni")
        print(obchodCisly)
        obchodCislystr=[]
        for h in obchodCisly:
            obchodCislystr.append(str(h))
            cislozbrane+=1  
        print("Cena")
        print(obchodCeny)
        akce = input(obchodCisly)
        if akce not in obchodCislystr:
            print("Nic jsi nekoupil.")
        
        else:
            akce=int(akce)
            if (Penize - int(obchodCeny[akce]))>-1:
                print("Koupeno")
                Ziv=1+int(obchodSily[akce])
                print(f"Pocet zivotu:{Ziv}")
                Penize-=int(obchodCeny[akce])

            else:
                print("Mas malo penez")
    return(Penize,TvojeVec,TvojeVecSila,Ziv)
                