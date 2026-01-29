#scrivere un programma che dati 2 punti in un piano
#cartesiano scriva l'equazione della retta associata e mandi
#in output il messaggio la positivita del
#coefficente angolare
import random

def calcolo_m(xuno,xdue,yuno,ydue):
    m=(ydue-yuno/xdue-xuno)
    return(m)

def equazione(m,x,y):
    eq="y-"+ str(y)+"="+ str(m)+"(x-"+ str(x)+")"
    print(eq)
    
def controllo_m(m):
    if m>0:
        print("m ha segno positivo")
    elif m==0:
        print("m è nullo")
    else:
        print("m ha segno negativo")

def incremento_uno(a):
    a=a+1
    print(a)
    
if __name__=="__main__":
    xuno=random.randint(-20,20)
    xdue=random.randint(-20,20)
    yuno=random.randint(-20,20)
    ydue=random.randint(-20,20)
    
    coefficente_angolare=calcolo_m(xuno,xdue,yuno,ydue)
    print(coefficente_angolare)
    equazione(coefficente_angolare,xdue,ydue)
    controllo_m(coefficente_angolare)
    incremento_uno(xuno)
    
