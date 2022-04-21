#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random as r
def dado():
    a = r.randrange(1,7)
    return a

def juego(): 
    cant_j = int(input('Ingrese el numero de jugadores:\n '))
    apuesta = int(input('Ingrese el valor inicial de la apuesta:\n '))
    

    jugadores = list(range(1,cant_j+1))
    l = {}
    for jugador in jugadores:
        n= 1000-apuesta
        l[jugador] = n 
    
    pozo= cant_j * apuesta    
    turno = 1
    
    while pozo>0:
        lan1 = dado()
        lan2 = dado()
        
        print(l)
        print(' ')
        
        print('jugador',turno)
        print('Primer lanzamiento: ',lan1)
        comision = 0.05
        casino = 0
        
        if lan1 == 1:
            print("Perdiste la apuesta")
            pozo += apuesta
            print ('Pozo:',pozo)
            l[turno] -= apuesta
            
        if lan1 == 6:
            print("Ganaste la apuesta")
            pozo = pozo-apuesta
            print ('Pozo:',pozo)
            l[turno]+=apuesta 
            
        
        if 1<lan1<6:
            casino_alerta = pozo*comision
            pozo_alerta = (pozo-casino_alerta)
            apuestaa = int(input(f'Ingrese el valor a apostar que no sea mayor a {int(pozo_alerta)} y a {l[jugador]}: '))
            print ('Segundo lanzamiento: ',lan2)
            if lan1<lan2:
                print("Ganaste la apuesta")
                print('Pozo', pozo)
                casino = pozo*comision
                pozo = (pozo-casino)-apuestaa
                pozo_alerta = (pozo-casino_alerta)
                l[turno] += apuestaa
                
            elif pozo<apuesta:
                print('Error, la apuesta es mayor que pozo')
                print('Pozo:',pozo)
                
            if lan1>=lan2:
                print("Perdiste la apuesta")
                pozo = pozo+apuestaa
                print('Pozo:',pozo)
                l[turno] -= apuestaa
            
            
        if turno>=cant_j:
            turno = 0
            print(' ')
            
        if pozo <= 0 :
            print('Pozo:', int(pozo))
            print('Fin del juego')
        
        turno+=1 
        
        print(' ')
    
        if l[jugador] == 0:
            l.popitem()


# ***
