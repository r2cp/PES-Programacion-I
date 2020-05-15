# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#import pdb


def biseccion(f, a=-100, b=100, epsilon=0.001, max_iter=100):

    guess = (a + b) / 2

    # Contador de iteraciones
    num_guesses = 0
    
    #pdb.set_trace()
    while abs(f(guess)) >= epsilon and num_guesses < max_iter:
        if f(a)*f(guess) > 0:
            # Si f(a) y f(guess) tienen el mismo signo, se debe
            # acortar el intervalo por la izquierda
            # Tu código acá:
            a = guess
        else:
            # De lo contrario, se acorta por el lado derecho
            # Tu código acá:
            b = guess
        # Siguiente guess en el punto medio del espacio de búsqueda
        guess = (a + b) / 2
        num_guesses += 1

    print('Iteraciones: ', num_guesses)
    print('Solución encontrada: f(%0.4f) = %0.4f' % (guess, f(guess)))
    return guess

f = lambda x: x**2 - x - 1
approx_phi = biseccion(f, a=1, b=2, epsilon=1e-6)
print(approx_phi)