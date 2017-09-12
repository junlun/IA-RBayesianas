import sys
import os.path
sys.path.append(os.path.realpath("."))
import src.Clasificador.Knn.KNNTrainingValues as knntv
import math
import types
import operator
from operator import mul
import src.Preprocesador.PreprocesadorUtils  as putils
from urllib.parse import urlparse
import src.Preprocesador.FileUtils as fu

tv = knntv.KNNTrainingValues()

#Clasifica un text con un número de vecinos N, por defecto 30
def clasifica(text,N=30):
    text = fu.urlchecker(text)
    #Obtenemos el vector asociado al nuevo texto
    v1 = calculaFrecuenciaDocumentalNueva(text)
    
    categorias = dict()
    result = ""
    #Primero buscamos los N vecinos mas cercanos
    for k,v in tv.vectores.items():
        categorias[k]=__similitud(v,v1)

    #Ordenamos la lista según la similitud obtenida ordenada de mayor similitud a menor
    sorted_cat = sorted(categorias.items(), key=operator.itemgetter(1),reverse=True)
    sorted_cat=sorted_cat[0:N]
    
    #Nos quedamos con la categoría del elemento
    for i in sorted_cat:
        result+=i[0].split("-")[0] +" "  

    #Cogemos la categoría más repetida.
    return putils.counter(result).most_common(1)[0][0]


def distanciaDocumentos(d1,d2):
    v1 = [float(i.strip()) for i in tv.vectores[d1]]
    v2 = [float(i.strip()) for i in tv.vectores[d2]]
    return __similitud(v1,v2)

def __similitud(v1,v2):    
    numerador = sum(map(mul, v1, v2))
    if(numerador !=0): #Si el numerador es 0, el numerador también lo será, además ya sabemos el resultado.
        raiz1 = math.sqrt(sum(map(mul,v1,v1)))
        raiz2 = math.sqrt(sum(map(mul,v2,v2)))
        dist = numerador /(raiz1*raiz2)
    else:
        dist = 0    
    return dist

def calculaFrecuenciaDocumentalNueva(text):
    result = []
    keywords = tv.keywords
    fDocumentales = tv.frecuenciasDocumentales
    for keyword in keywords:
        result.append(knntv.calculaPesoDocumento(keyword,text,fDocumentales[keyword]))
    return result

def refrescaPesos():
    knntv.escribePesos(tv.keywords,tv.texts,tv.frecuenciasDocumentales)

