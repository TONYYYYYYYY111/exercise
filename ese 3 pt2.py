import random

punti_cartesiano=[]
for i in range (0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
minimox=punti_cartesiano[0]
for i in range(0,20):
    if punti_cartesiano[i][0]<minimox[0]:
        minimox=punti_cartesiano[i]
print("la coppia con le x più piccole è ",minimox)

massimoy=punti_cartesiano[1]
for i in range(0,20):
    if punti_cartesiano[i][1]>massimoy[1]:
        massimoy=punti_cartesiano[i]
print("il massimo delle y è ",massimoy)       
    
    