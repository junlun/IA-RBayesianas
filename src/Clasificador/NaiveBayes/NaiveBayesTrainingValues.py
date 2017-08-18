import sys
import os.path
sys.path.append(os.path.realpath("."))
import src.Preprocesador.FileUtils as fu
import math 

N = fu.getNumberOfDocuments("resources\\data\\training") #Número total de documentos del conjunto de entrenamiento

def generaValores():
    textosPorCategoria = fu.readAllFiles("resources\\data\\training")
    text = ""
    for categoria in textosPorCategoria.items():
        text += generaTexto(categoria)
    
    fu.writeFile("src\\Clasificador\\NaiveBayes\\trainingValues.txt", text)

def generaTexto(categoria):
    text = categoria[0] + ", "
    Nc = fu.getNumberOfDocuments("resources\\data\\training\\" + categoria[0]) #Número de documentos de la categoría en el conjunto de entrenamiento
    pc = round(Nc/N, 4)
    text += str(pc) + ", "
    ptc = calculaPtc(categoria)
    ptc = ptc[0:len(ptc)-2]
    text += str(ptc) + "\n"

    return text

def calculaPtc(categoria):
    lines = fu.readFile("resources\\data\\dictionaries\\" + categoria[0] + ".txt")
    textosAplanados = fu.readAllFiles("resources\\data\\training\\" + categoria[0])
    tcs = 0
    text = ""
    for t in lines.split():
        tcs += fu.countWordInText(t, textosAplanados.get(categoria[0])) #Suma todas las apariciones de todos los términos
    for t in lines.split():
        tct = fu.countWordInText(t, textosAplanados.get(categoria[0])) #Cuenta todas las apariciones de cada término
        text += str(round((tct+1) / (tcs+len(lines.split())), 4)) + ", "

    return text

generaValores()