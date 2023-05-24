import random

def mestanazvy():
    MestaNazvyList=[]
    soubor = open('lokace.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            MestaNazvyList.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(MestaNazvyList)




"""Vytvori dvacet zakladnich mest potlokme(lokace mesta) potnaz(nazev)"""
def mestazaklad(planek,PoleMest):
    for i in range (20):
        c=0
        while(c==0):
            potlokme=random.randint(0,899)
            potnaz=random.randint(1,len(PoleMest)-1)
            if (planek[potlokme][1])==0:
                planek[potlokme][0]=1
                planek[potlokme][1]=3
                planek[potlokme][2]=2
                planek[potlokme][3]=0
                planek[potlokme][4]=0
                planek[potlokme][5]=potnaz
                c=1
    return(planek)




"""Vytvori ctyri vyznamna mesta. dve hodna a dve zla potlokme(lokace mesta)"""
"""planek[potlokme][0] typ mesta hodne(2) zle (3)
    planek[potlokme][1] kazde klicove mesto ma jedno specicifke cislo hodna(5,6) zla(6,7)
    planek[potlokme][2] kolik penez ma mesto zaplatit u klicovych mest neni potreba
    planek[potlokme][3] jmeno generala(zleho)
    planek[potlokme][4] sila generala(zleho)"""
def klicovamesta(planek,poleGeneralu,silaGeneralu):
    c=0
    while(c==0):
        potlokme=int(random.randint(0,29))+int(random.randint(0,29)*30)
        if planek[potlokme][1]==0:
            planek[potlokme][0]=2           
            planek[potlokme][1]=5
            planek[potlokme][2]=2
            planek[potlokme][3]=0
            planek[potlokme][4]=0
            c=1
    c=0
    while(c==0):
        potlokme=int(random.randint(0,29))+int(random.randint(0,29)*30)
        if (planek[potlokme][1])==0:
            planek[potlokme][0]=2           
            planek[potlokme][1]=6
            planek[potlokme][2]=2
            planek[potlokme][3]=0
            planek[potlokme][4]=0
            c=1
    c=0
    gen= random.randint(0,(len(poleGeneralu)-1))
    print(gen)
    while(c==0):
        potlokme=int(random.randint(0,29))+int(random.randint(0,29)*30)
        if (planek[potlokme][1])==0:
            planek[potlokme][0]=3           
            planek[potlokme][1]=7
            planek[potlokme][2]=2
            planek[potlokme][3]=gen
            planek[potlokme][4]=silaGeneralu[gen]
            c=1

    c=0
    while(c==0):
        potlokme=int(random.randint(0,29))+int(random.randint(0,29)*30)
        if (planek[potlokme][1])==0:
            planek[potlokme][0]=3           
            planek[potlokme][1]=8
            planek[potlokme][2]=2
            planek[potlokme][3]=gen
            planek[potlokme][4]=silaGeneralu[gen]
            c=1
    return(planek)




"""Vybere penize z mest na planku"""
def pen(planek):
    penize=0
    for i in range(900):
        if planek[i][0]==1 and planek[i][1]>1:
            penize+= planek[i][2]
    return(penize)




"""Vylepsuje mesta na planku za penize"""
"""Prozprom nahodne vybrane misto na mape mnohokrat prepsanan nez dojdou penize"""
def tvorbamest(citah,penize,planek):
    c=0
    a=0
    print("tm")
    while c==0:
        if penize>0:
            prozprom=random.randint(0,899)
            a+=1
            if planek[prozprom][0]==citah and planek[prozprom][1]>1 and planek[prozprom][1]<4:
                penize=penize-(int(planek[prozprom][2]))*10
                planek[prozprom][1]=int(planek[prozprom][1])+1
                planek[prozprom][2]=(int(planek[prozprom][2]))*2
                a=0
            if a>30:
                c=1
        else: c=1
    return(planek)




"""Nahodne se vybere misto pokud je tam les je sance odtranit tam priseru
    prozprom(nahodne vybrana pozice)"""

def utok(planek,citah):
    prozprom=random.randint(0,899)
    if planek[prozprom][0]==citah and planek[prozprom][1]==0:
        hodprisery=random.randint(1,6)
        hodvojaku=random.randint(1,2) + 10
        if (hodprisery+int(planek[prozprom][4]))<(hodvojaku):
            planek[prozprom][1]=int(planek[prozprom][1])+1
            planek[prozprom][3]=0
            planek[prozprom][4]=0
    return(planek)



"""Neobydlene lesy se meni na vesnice potnaz(nazev) """
def kolonizace(planek):
    PoleMest=mestanazvy()
    for i in range(900):
        if planek[i][0]==1 and planek[i][1]==1:
            potnaz=random.randint(1,len(PoleMest)-1)
            planek[i][5]=potnaz
            planek[i][1]=2
            planek[i][2]=1
    return(planek)




"""Pokud je konec odpoctu hodne mesto se zmeni na zle mesto"""
def dobyvani(planek,dobodpoc):
    if dobodpoc==0:
        for i in range(900):
                if planek[i][1]<0:
                    planek[i][1]=7
                    planek[i][2]=3
    return(planek)
