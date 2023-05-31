

def prisera():
    polePriser = []
    try:
        soubor = open('priseraob.txt', 'r')
        souborstr = soubor.readlines()
        souborstr = str(souborstr)
        clenylistu = str()
        for i in souborstr:
            if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
                pass
            elif ord(i)== 44:
                polePriser.append(clenylistu)
                clenylistu = str()
            else:
                clenylistu += i
    except FileNotFoundError:
        print("Soubor nenalezen")
    return(polePriser)


def silapris():
    SiList = []
    soubor = open('sila.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
                clenylistu=int(clenylistu)
                SiList.append(clenylistu)
                clenylistu = str()
        else:
             clenylistu += i
    return(SiList)


def gengen():
    GeneraloveList=[]
    soubor = open('sef.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            GeneraloveList.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(GeneraloveList)


def silagen():
    generalListSila=[]
    soubor = open('sefsila.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            generalListSila.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(generalListSila)


def veci():
    veclist=[]
    soubor = open('veci.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            veclist.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(veclist)


def vecisila():
    veciSilaList=[]
    soubor = open('vecisila.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            veciSilaList.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(veciSilaList)


def obleceni():
    obleceniList=[]
    soubor = open('obleceni.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            obleceniList.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(obleceniList)


def oblecenisila():
    obleceniSilaList=[]
    soubor = open('oblecenisila.txt', 'r')
    souborstr = soubor.readlines()
    souborstr = str(souborstr)
    clenylistu = str()
    for i in souborstr:
        if ord(i)== 39 or ord(i)== 91 or ord(i) == 93:
            pass
        elif ord(i)== 44:
            obleceniSilaList.append(clenylistu)
            clenylistu = str()
        else:
            clenylistu += i
    return(obleceniSilaList)
def navod():
    try:
        with open ("navod.txt","r") as f:
            text= f.read()
    except FileNotFoundError:
        print("Soubor navod nenalezen")
    return(text)
