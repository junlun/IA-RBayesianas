import sys
import os.path
sys.path.append(os.path.realpath("."))
import Preprocesador.FileUtils as fu
import InicializadorDatos as data


N = fu.getNumberOfDocuments("resources\\data\\training") #Número total de documentos del conjunto de entrenamiento
data = data.Data()

class NaiveBayesTrainingValues:

    def __init__(self):
        self.probabilidades = leeValores()

    def getProbabilidades(self):
        return self.probabilidades

def generaValores():
    textosPorCategoria = fu.readAllFiles("resources\\data\\training")
    text = ""
    for categoria in textosPorCategoria.items():
        text += __generaTexto(categoria)
    
    fu.writeFile("src\\Clasificador\\NaiveBayes\\trainingValues.txt", text)

def __generaTexto(categoria):
    text = categoria[0] + ", "
    Nc = fu.getNumberOfDocuments("resources\\data\\training\\" + categoria[0]) #Número de documentos de la categoría en el conjunto de entrenamiento
    pc = round(Nc/N, 4)
    text += str(pc) + ", "
    ptc = __calculaPtc(categoria)
    ptc = ptc[0:len(ptc)-2] #Quita los dos últimos caracteres del string (", ")
    text += str(ptc) + "\n"

    return text

def __calculaPtc(categoria):
    vocabulary = data.getTermsPlain()
    textosAplanados = data.getTextOfCategoryPlain(categoria[0])
    tcs = 0
    text = ""
    for t in vocabulary:
        tcs += fu.countWordInText(t, textosAplanados) + 1 #Suma de apariciones de todos los términos del vocabulario en los documentos de la categoría
    for t in vocabulary:
        tct = fu.countWordInText(t, textosAplanados) + 1 #Cuenta todas las apariciones de cada término del vocabulario en la categoría
        text += str(round(tct/tcs, 4)) + ", "
    return text

def leeValores():
    probs = dict()
    lines = fu.readFile("src\\Clasificador\\NaiveBayes\\trainingValues.txt")
    lines = lines.splitlines()
    for line in lines:
        spl = line.split(',')
        name = spl[0]
        values = spl[1:len(spl)]
        probs[name]=values

    return probs
