# estrarre 3 carte da mazzo (lista) [1,2,3,4,5,6,7,8,9,J,Q,K]
# calcolare il punteggio usando dizionario che associ carta al suo valore


import random


mazzo = ["1", "2", "3", "4", "5", "6", "7", "8", "9","10", "J", "Q", "K"]
valori = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,"10":10,'J': 10,'Q': 10,'K': 10}
carte_estratte = random.sample(mazzo,3)
print(carte_estratte)

punteggio=0
for carta in carte_estratte:
    punteggio=punteggio+valori[carta]
    
print("Carte estratte:", carte_estratte)
print("Punteggio totale:", punteggio)
    



