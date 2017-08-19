import sys
import os.path
sys.path.append(os.path.realpath('.'))
import src.Preprocesador.FileUtils as fu
pathToDictionaries = "resources\\data\\dictionaries"
pathToTraining = "resources\\data\\training"

trainingTexts = fu.readAllFilesFileNames(pathToTraining)
NDocumentos = fu.getNumberOfDocuments(pathToTraining)

def getTextsOfCategory(category):
    return trainingTexts[category]

def getTermsOfVocabulary(sf,category):
    return keywords[category]

def getTextOfCategoryPlain(category):
    result =""
    for k,v in trainingTexts[category].items():
        result+= v+" "
    return result    

def getTermsPlain():
    result = []
    for k,v in keywords.items():
        for line in v:
            spl = line.splitlines()
            for term in spl:
                result.append(term)
    return result        

def readVocabulary():
    result = dict()
    keywords = fu.readAllFilesFileNames(pathToDictionaries)["dictionaries"]
    for k,v in keywords.items():
        category = k.replace(".txt","")
        values = v.split("\r\n")
        result[category] = values
    return result 

keywords = readVocabulary()  