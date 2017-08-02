import collections
import PreprocesadorUtils
import FileUtils

def createDictionaries():
    dictionary = FileUtils.readAllFiles("resources\\data\\training")
    for key in dictionary:
        createDictionary(key, dictionary[key])

def createDictionary(category, text):
    text = PreprocesadorUtils.discriminator(text)
    counter = PreprocesadorUtils.counter(text)
    text = counter.most_common(20)
    texto = ""
    for word in text:
        texto += str(word)
    FileUtils.writeFile("resources\\data\\dictionaries\\"+category+".txt", texto)

createDictionaries()
