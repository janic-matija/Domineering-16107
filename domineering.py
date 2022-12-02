import time
import os
import platform

pocetak=time.time()

def izlaz():
    print("za izlaz unesite <q>")

def test(broj):
    broj+=5
    print(broj)

def unosPodataka():
    dimenzije = False
    while dimenzije:
        izlaz()
        print("Unesite dimenzije tabele u sledecem formatu: <BrojRedovaTabele> <BrojKolonaTabele> :")
        podaci=input().split()
        print(f'podaci:{podaci}' )
        if len(podaci)==2 and podaci[0].isdigit(): # isdigit za integer i veci od -1
            #start(int(podaci[0]), int(podaci[1]))
            break
        elif(podaci == ['q']):
            print('izlaz ...')
            break
    broj=3
    test(broj)
    print(broj)


def start(M,N):
    tabla=[[' ' for a in range(N)] for b in range(M)] # chr(32)
    print(len(tabla[0]))
    for i in tabla:
        print(i)
    crtaj(M,N,tabla)
    
    igraj(tabla)

def igraj(tabla):
    znak='3'
    while znak !='1' and znak != '2':
        znak=input("Zelite li da igrate prvi(1) ili drugi(2)?")
        # igrac1 ={
        # "znak": 'X'
    # }
    # igrac2 ={
        # "znak": 'O'
    # }
    prvi=''
    drugi=''
    if znak=='1':
        prvi='covek'
        racunar=igrac2
        potez(tabla,covek,covek["znak"])
    elif znak == '2':
        covek=igrac2
        racunar=igrac1
    while kraj()>0:
        potez(tabla,covek,covek["znak"])
        potez(tabla,racunar,covek["znak"])

def potez(M,N,plavi,zeleni,tabla,igrac,znak):
    #if igrac["znak"]==znak:
    dobarPotez=1
    noviPotez = []
    while dobarPotez:
        print("Unesite sledeci potez u formatu: Znak Pesak(1 ili 2) PotezVrsta PotezKolona BojaZida ZidVrsta ZidKolona")
        noviPotez=input().strip().split()
        if (noviPotez[0] != 'X' and noviPotez[0] != 'Y')  \
            or (noviPotez[1] != '1' and noviPotez[1] != '2') \
            or (int(noviPotez[2]<1) or int(noviPotez[2]>N)) \
            or (int(noviPotez[3]<1) or int(noviPotez[3]>M)) \
            or (noviPotez[4] != 'p' and noviPotez[4] != 'z') \
            or (int(noviPotez[5])<1 or int(noviPotez[5]>N)) \
            or (int(noviPotez[6]<1) or int(noviPotez[6]>M)):
                dobarPotez-=1
        else:
            znak=noviPotez[0]
            pesak=igrac["pesak"+noviPotez[1]]
            potez=[int(noviPotez[2])-1,int(noviPotez[3])-1]
            razlika=0
            if pesak[0]==potez[0] or pesak[1]==potez[1]:
                novo=pesak
                if potez[0]==pesak[0]:
                    if potez[1]<pesak[1]:
                        novo=potez
                    if zeleni[novo[0]][novo[1]]=='|'and zeleni[novo[0]][novo[1]+1] == '|':
                        tabla[potez[0]][potez[1]]=znak
                        tabla[pesak[0]][pesak[1]]=chr(32)
                    else:
                        dobarPotez-=1
                elif potez[1]==pesak[1]:
                    if potez[0]<pesak[0]:
                        novo=potez
                    if plavi[novo[0]][novo[1]]=='-'and plavi[novo[0]][novo[1]+1] == '-':
                        tabla[potez[0]][potez[1]]=znak
                        tabla[pesak[0]][pesak[1]]='='
                    else:
                        dobarPotez-=1
                else:
                    x=2
            boja=noviPotez[4]
            zidVrsta=int(noviPotez[5])-1
            zidKolona=int(noviPotez[6])-1
            if boja=='p':
                if plavi[zidVrsta][zidKolona] == '-' and plavi[zidVrsta][zidKolona+1] == '-':
                    plavi[zidVrsta][zidKolona]='='
                    plavi[zidVrsta][zidKolona+1]='='
                else:
                    dobarPotez-=1
            elif boja=='z':
                if zeleni[zidVrsta][zidKolona] == '|' and plavi[zidVrsta+1][zidKolona] == '|':
                    plavi[zidVrsta][zidKolona]=chr(0x01C1)
                    plavi[zidVrsta+1][zidKolona]=chr(0x01C1)
                else:
                    dobarPotez-=1
            else:
                    dobarPotez-=1
            #for x in plavi:
            #    print(x)
        if not dobarPotez:
            noviPotez = []
            print("\nPogresan unos podataka za potez ! Pokusajte ponovo:\n")
        else:
            break
    crtaj(M,N,plavi,zeleni,tabla)

    x=8


def crtaj(M,N,tabla):
    for i in range(3):
        simbol='='
        print(" ",end=' ')
        for x in range(N):
            if i == 0:
                simbol = hex(x+10)[2:]
            print(simbol,end=' ')
        print() # novi red
        if i==1:
            for a in range(M):
                simbol='║'
                print(hex(a+1)[2:],end='║') #chr(186) ne radi??
                for b in range(N-1):
                    print(tabla[a][b],end='|')
                print(tabla[a][N-1],end='║')
                
                if a<(M-1):
                    print()
                    print(" ",end=' ') 
                    for b in range(N):
                        print("-",end=' ')
                print()
    # print(time.time()-pocetak)
     
     
def kraj():
    x=2
    return 1
       
            
def main():
    odgovor="dn"
    while odgovor!='da' and odgovor!='ne':
        odgovor=input("Poceti novu igru? (da/ne): ")
    else:
        if odgovor=='da':
            unosPodataka()
        elif odgovor=='ne':
            exit
    
if __name__ == "__main__":
    main()