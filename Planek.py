import random
def start(PoleSilPriser,IndexyPriseryDelka):
    planek = []
    for i in range(900):
        a=1
        b=0
        c=random.randint(0,IndexyPriseryDelka)
        d=PoleSilPriser[c]
        e=0
        stat = [a,0,0,c,d,e]
        planek.append(stat)
    return(planek)


"""Tiskne mapu do txt"""
def MapaViz(planek,Pozice):
    mujplanek = []
    a=-1
    b=-1
    for i in range(30):
        jplanek = []
        for i in range(30):
            a+=1
            b+=1
            if b==Pozice:
                jplanek.append("P")
            else:
                jplanek.append(planek[a][1])
        mujplanek.append(jplanek)
        
    with open ("mapa.txt","w") as f:
        lines=str(mujplanek)
        nl=""
        a=1
        for i in lines:
         
            """if ord i not in"""
            if (ord(i)<91) or (ord(i)>93):
                
                if ((ord(i)!=44) and(ord(i)!=32) and (ord(i)!=39)) and a==1:
                    nl+=i
                    if ord(i)!=45:
                        nl+=" "
                    else:
                        nl+=" "
                        a=0
                else:
                    a=1
            elif ord(i)==93:
                nl+= "\n"

        f.write(nl)
    


"""prevede mapu do podoby ve ktere se tiskne do konzole"""
def MapaVizu(planek,Pozice):
    mujplanek = []
    a=-1
    b=-1
    for i in range(30):
        jplanek = []
        for i in range(30):
            a+=1
            b+=1
            if b==Pozice:
                jplanek.append("P")
            else:
                jplanek.append(planek[a][1])
        mujplanek.append(jplanek)
    lines=str(mujplanek)
    nl=""
    a=1
    for i in lines:
         
        """if ord i not in"""
        if ord(i) not in[91,92,93]:
                
            if ((ord(i)!=44) and(ord(i)!=32) and (ord(i)!=39)) and a==1:
                nl+=i
                if ord(i)!=45:
                    nl+=" "
                else:
                    nl+=" "
                    a=0
            else:
                a=1
        elif ord(i)==93:
            nl+= "\n"
    return(nl)

"""Vytvari predikci"""
def zpravy(kam,odpocet,jmenogenerala,dobodpoc,silautoku):
    if kam==6:
        misto="Hlavniho mesta"
    else:
        misto="Univerzitniho mesta"
    lines=(f"Napadeni {misto} probehne za {odpocet} tahu. Utok povede {jmenogenerala}.\nMa silu {silautoku}." )
    return(lines)
