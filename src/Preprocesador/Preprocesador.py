import sys
import os.path
sys.path.append(os.path.realpath("."))
import collections
import Preprocesador.PreprocesadorUtils as PreprocesadorUtils
import Preprocesador.FileUtils as FileUtils

def createDictionaries(N=20):
    dictionary = FileUtils.readAllFiles("resources\\data\\training")
    for key in dictionary:
        createDictionary(key, dictionary[key], N)

def createDictionary(category, text, N=20):
    text = PreprocesadorUtils.discriminator(text)
    counter = PreprocesadorUtils.counter(text)
    pairs = counter.most_common(N)
    texto = ""
    for pair in pairs:
        texto += pair[0] + os.linesep
    FileUtils.writeFile("resources\\data\\generatedDictionaries\\"+category+".txt", texto)

