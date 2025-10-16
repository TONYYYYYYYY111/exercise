import random

punti_cartesiano=[]
for i in range (0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
"""
come accedere alla x del primo punto?
print(punti_cartesiano[0][0])

come accederealla y del primo punto?
print(punti_cartesiano[0][1])
"""
massimox=punti_cartesiano[0]
for i in range(0,20):
    if punti_cartesiano[i][0]>massimox[0]:
        massimox=punti_cartesiano[i]
print("il massimo delle x è ",massimox)

massimoy=punti_cartesiano[1]
for i in range(0,20):
    if punti_cartesiano[i][1]>massimoy[1]:
        massimoy=punti_cartesiano[i]
print("il massimo delle y è ",massimoy)
        

