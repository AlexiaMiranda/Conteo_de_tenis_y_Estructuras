#Programa que lleva el conteo de puntos en un torneo de tenis.
class Nombres:
    print('nombre de los jugadores:')
    nombres = input().split() 
    jugador1=nombres[0]
    jugador2= nombres[1]

#Funcion principal.
def main():
    
    i=0 #Puntos correspondientes al jugador1. 
    j=0 #Puntos correspondientes al jugador2.
    love = 0 #inicio del juego.
    pt1 = 15
    pt2 = 30
    pt3 = 45 #conveniencia, pero es de hecho 40
    game = False
    ventaja= -1 #ventaja i es ventaja para el jugador i, i=1,2

    while(game==False):
        if (i<pt3 or j<pt3) and ventaja==-1:
            
            punto_jugador = input("Punto para: ")
            
            match punto_jugador :
                case Nombres.jugador1 :
                    i +=15
                    if i==pt3 : ventaja = 1; print("Ventaja de A")
                    
                case Nombres.jugador2 :
                    j +=15
                    if j==pt3 : ventaja = 2; print("Ventaja de B")
                        
                
                case _ :
                    print("jugador no registrado")

        else:
            punto_final= input("Punto para: ")
            match punto_final :
                case Nombres.jugador1 if punto_final in Nombres.nombres :
                    i+=15
                    if ventaja==1 :
                        game = True
                        print("Juego para ", Nombres.jugador1)
                    elif i!=45: #Anoto, pero no es su tercer punto
                        ventaja= -1; print("B pierde ventaja")             
                        
                    else :
                        ventaja = 1
                        

                case Nombres.jugador2 if punto_final in Nombres.nombres :
                    j+=15
                    if ventaja==2 :
                        game = True
                        print("Juego para ", Nombres.jugador2)
                    elif j!=45: #Anoto, pero no es su tercer punto
                        ventaja= -1; print("A pierde ventaja")
                        
                    else :
                        ventaja = 2
                        

                case _ :
                    break
                    
        



main()