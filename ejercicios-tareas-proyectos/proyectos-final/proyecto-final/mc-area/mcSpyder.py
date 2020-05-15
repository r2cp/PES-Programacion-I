# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:59:56 2020

@author: MAVE
"""

#%%
class AreaMonteCarlo(object):
    
    """ En esta sección debe definir correctamente el método constructor. """
    def __init__(self,superior,inferior,infizq,supder):
        self.superior = # Función correspondiente al límite superior del área sombreada.
        self.inferior = # Función correspondiente al límite superior del área sombreada.
        self.infizq = # Coordenadas correspondientes a la esquina inferior izquierda del rectángulo.
        self.supder = # Coordenadas correspondientes a la esquina superior derecha del rectángulo.
        self.dardos = # Al inicio corresponde a un NoneType
        self.n = # Número de dardos lanzados. Al inicio es NoneType.
       
    """ En esta sección debe definir un método que permita generar una matriz 
    de n filas y 2 columnas, rellena completamente de números aleatorios 
    uniformemente distribuidos. Dicha matrix debe ser almacenada el atributo 'dardos'"""
    
    def lanzarDardos(self,n):
        pass
    
    """ En esta sección debe definir un método que grafique algo similar al ejemplo. 
    El método debe poder graficar aún cuando el atributo "dardo" esté vacío.
    Debe graficar en un rectágulo que tenga las esquinas 'infizq' y 'supder'
    como límites. Se debe poder elegir guardar o no la gráfica de 
    alta calidad con nombre 'mc.png'. La cantidad de filas 'n' se debe
    guardar en el atributo con mismo nombre. """
    
    def graficar(self, guardar=False):
        pass
    
    """ En esta sección calcule el área por método Monte Carlo. Debe devolver 
    un flotante con el área. """"
    
    def calcularArea(self):
        pass
    
    """ En esta sección, escriba un método que devuelva un DataFrame con las
    siguientes columnas:
        - Coordenada en x del dardo
        - Coordenada en y del dardo
        - 1 si está dentro del área y 0 si no lo está. 
        
        Se debe poder elegir guardar un archivo mc.csv con los resultados."""
    def dardosResultados(self, guardar=False):
        pass