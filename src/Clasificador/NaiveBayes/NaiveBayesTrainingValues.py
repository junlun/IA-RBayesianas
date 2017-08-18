import sys
import os.path
sys.path.append(os.path.realpath("."))
import src.Preprocesador.FileUtils as fu
import math 

N = fu.getNumberOfDocuments("resources\\data\\training") #Número total de documentos del conjunto de entrenamiento

def generaValores():
    textosPorCategoria = fu.readAllFiles("resources\\data\\training")
    for categoria in textosPorCategoria:
        generaTexto(categoria)

def generaTexto(categoria):
    text = categoria[0] + ", "
    Nc = fu.getNumberOfDocuments("resources\\data\\training\\" + categoria[0]) #Número de documentos de la categoría en el conjunto de entrenamiento
    pc = Nc/N
    text += pc + ", "
    ptc = calculaPtc(categoria)
    text += ptc

def calculaPtc(categoria):
    lines = fu.readFile("resources\\data\\dictionaries" + categoria[0] + ".txt")
    for t in lines.split():
        
