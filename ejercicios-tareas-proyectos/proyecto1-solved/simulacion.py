# %% Importar modulos
import funciones as fun #Mi modulo de funciones
import os
import time

DELAY_TIME = 2

# %% Leer archivo
Iniciales = open('iniciales-3knb.txt', 'r')
Iniciales = Iniciales.readlines(0)

for i in range(len(Iniciales)):
    Iniciales[i] = Iniciales[i].replace('\n','')
    Iniciales[i] = Iniciales[i].split(sep=',')
    
# %% Condiciones iniciales
DimX = int(Iniciales[0][0])
DimY = int(Iniciales[0][1])
T = int(Iniciales[0][2])

T0 = fun.TableroZero(DimX,DimY)

for i in range(1,len(Iniciales)):
    T0[(int(Iniciales[i][0]),int(Iniciales[i][1]))]=1

# %% Simulaciòn del juego

Juego =  fun.Simulacion(T0,T,T0['DimX'],T0['DimY'], fun.JuegoVidaNeto)
    
# %% Animacion del juego
for t in Juego:
    fun.PrintTablero(t,t['DimX'],t['DimY'])
    time.sleep(DELAY_TIME)
    os.system('cls' if os.name == 'nt' else 'clear')
    