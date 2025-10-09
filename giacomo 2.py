#dato un insieme di 20 punti su un piano cartesiano
#random compresi nel intervallo 0,10. calcolare il
#punto con ascissa massima o il punto con coordinata minima

import random
puntix=[]
puntiy=[]
for i in range(0,20):
    puntix.append(random.randint(0,10))
    puntiy.append(random.randint(0,10))
    
punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
#come accedere alla x del rimo punto
print(punti_cartesiano[0][0])
#come accedere alla x del rimo punto
print(punti_cartesiano[0][1])
