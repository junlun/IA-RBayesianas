import KNNTrainingValues as vectores
import math
from operator import mul

values = vectores.inicializar()
  
def distancia(d1,d2):
    v1 = [float(i.strip()) for i in values[d1]]
    v2 = [float(i.strip()) for i in values[d2]]
    
    numerador = sum(map(mul, v1, v2))
    if(numerador !=0): #Si el numerador es 0, el numerador también lo será, además ya sabemos el resultado.
        raiz1 = math.sqrt(sum(map(mul,v1,v1)))
        raiz2 = math.sqrt(sum(map(mul,v2,v2)))
        dist = numerador /(raiz1*raiz2)
    else:
        dist = 0    
    return dist
