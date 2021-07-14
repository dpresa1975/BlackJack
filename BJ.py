import random
A=(1 or 11)
J=10
Q=10
K=10
jug=0
deal=0
Baraja=[A,2,3,4,5,6,7,8,9,10,J,Q,K]
for i in range(100000):
    print("Cartas jugador")
    carta1=random.choice(Baraja)
    carta2=random.choice(Baraja)
    print(carta1,carta2)

    cartad=random.choice(Baraja)
    totaljugador=carta1+carta2

    print("Carta dealer")
    print(cartad)
    totaldealer=cartad

    
    while totaljugador < 17:
        print("nueva carta jugador")
        nueva_carta=random.choice(Baraja)
        print(nueva_carta)
        totaljugador=totaljugador+nueva_carta
        print("jugada jugador")
        print(totaljugador)

#turno dealer
    while totaldealer < 17:
        print("nueva carta dealer")
        nueva_carta=random.choice(Baraja)
        print(nueva_carta)
        totaldealer=totaldealer+nueva_carta
        print("jugada dealer")
        print(totaldealer)
    diferenciajugador=21-totaljugador
    diferenciadealer=21-totaldealer
    if totaljugador>21:
        print("GANA DEALER")
        deal+=1
    elif totaldealer>21:
        print("GANA JUGADOR")
        jug+=1
    elif diferenciadealer<=diferenciajugador:
        print("jugada dealer")
        print(totaldealer)
        print("VS")
        print("jugada jugador")
        print(totaljugador)
        print("GANA DEALER")
        deal+=1
    else:
        print("jugada dealer")
        print(totaldealer)
        print("VS")
        print("jugada jugador")
        print(totaljugador)
        print("GANA JUGADOR")             
        jug+=1         
print ("partidas Ganadas por dealer")
print(deal)
print("Porcentaje Dealer")
print(deal/500)
print ("partidas Ganadas por jugador")
print(jug)
print("Porcentaje Jugdor")
print(jug/500)
