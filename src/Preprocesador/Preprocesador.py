import sys
import os.path
sys.path.append(os.path.realpath("."))
import collections
import Preprocesador.PreprocesadorUtils as PreprocesadorUtils
import Preprocesador.FileUtils as FileUtils

def createDictionaries():
    dictionary = FileUtils.readAllFiles("resources\\data\\training")
    for key in dictionary:
        createDictionary(key, dictionary[key])

def createDictionary(category, text):
    text = PreprocesadorUtils.discriminator(text)
    counter = PreprocesadorUtils.counter(text)
    pairs = counter.most_common(50)
    texto = ""
    for pair in pairs:
        texto += pair[0] + "\n"
    FileUtils.writeFile("resources\\data\\dictionaries\\"+category+".txt", texto)

createDictionaries()
