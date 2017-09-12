import sys
import os.path
sys.path.append(os.path.realpath("."))
import collections
import Preprocesador.PreprocesadorUtils as PreprocesadorUtils
import Preprocesador.FileUtils as FileUtils

#Lee todos los textos de entrenamiento en un diccionario con relación categoría-textos de la categoría
#N = número de palabras que contendrá cada diccionario
def createDictionaries(N=20):
    dictionary = FileUtils.readAllFiles("resources\\data\\training")
    for key in dictionary:
        createDictionary(key, dictionary[key], N)

#Preprocesa el texto (con el discriminador), cuenta las N palabras más comunes y las
#escribe en un fichero
def createDictionary(category, text, N=20):
    text = PreprocesadorUtils.discriminator(text)
    counter = PreprocesadorUtils.counter(text)
    pairs = counter.most_common(N)
    texto = ""
    for pair in pairs:
        texto += pair[0] + os.linesep
    FileUtils.writeFile("resources\\data\\generatedDictionaries\\"+category+".txt", texto)

