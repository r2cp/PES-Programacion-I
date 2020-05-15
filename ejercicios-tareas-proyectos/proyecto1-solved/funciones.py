# %% ------------------------------------------------------------------------
def TableroZero(x,y):
    '''Matriz de x+2 * y+2. Va desde a celda (0,0) a la (x+1,y+1).
    Guarda la dimension de x en 'DimX' y la de y en 'DimY'. '''
    tablero={}
    for i in range(x+2):
        for j in range(y+2):
            tablero[(i,j)]=0
    tablero['DimX'] = x
    tablero['DimY'] = y
    return tablero
# %% ------------------------------------------------------------------------
def PrintTablero(dic,x,y):
    '''Imprime un diccionario-matriz dejando fuera un borde. es necesario
    especificar las dimesiones x y y de la matriz sin los bordes.'''
    for i in range(1,x+1):
        for j in range(1,y+1):
            if dic[(i,j)] == 0:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()
# %% ------------------------------------------------------------------------
def JuegoVida(dic,x,y):
    '''Recibe un diccionario con las condiciones iniciales del juego y
    el tamaño de la matrix'''
    dic2=dic.copy()
    for i in range(1,x+1):
        for j in range(1,y+1):
            aux=(dic[(i-1,j+1)],dic[(i,j+1)],dic[(i+1,j+1)],dic[(i-1,j)],\
                     dic[(i+1,j)],dic[(i-1,j-1)],dic[(i,j-1)],dic[(i+1,j-1)])
            aux=sum(aux)
            if dic[(i,j)]==0 and aux==3:
                dic2[(i,j)]=1
            elif dic[(i,j)]==1 and aux==2:
                dic2[(i,j)]=1
            elif dic[(i,j)]==1 and aux==3:
                dic2[(i,j)]=1
            else:
                dic2[(i,j)]=0
    return dic2


def JuegoVidaNeto(dic,x,y):
    '''Recibe un diccionario con las condiciones iniciales del juego y
    el tamaño de la matrix'''
    dic2=dic.copy()
    for i in range(1,x+1):
        for j in range(1,y+1):
            aux=(dic[(i-1,j+1)],dic[(i,j+1)],dic[(i+1,j+1)],dic[(i-1,j)],\
                     dic[(i+1,j)],dic[(i-1,j-1)],dic[(i,j-1)],dic[(i+1,j-1)])
            aux=sum(aux)
            if dic[(i,j)]==0 and aux>=4:
                dic2[(i,j)]=1
            elif dic[(i,j)]==1 and aux>4:
                dic2[(i,j)]=1
            elif dic[(i,j)]==0 and aux<=4:
                dic2[(i,j)]=0
            elif dic[(i,j)]==1 and aux<=4:
                dic2[(i,j)]=0
            else:
                dic2[(i,j)]=0
    return dic2
# %% ------------------------------------------------------------------------

def Simulacion(T0,T,x,y, JuegoVida = JuegoVida):
    '''T0 es el estado inicial del juego. T es la cantidad de periodos a\
    modelar. x y y son las dimensiones de la matrix.'''
    Juego =  [T0]
    for t in range(T):
        Juego.append(JuegoVida(Juego[t],x,y))
    return Juego
