import sys
import os.path
sys.path.append(os.path.realpath('.'))
import src.Preprocesador.FileUtils as fu
pathToDictionaries = "resources\\data\\dictionaries"
pathToTraining = "resources\\data\\training"
class Data:

    def __init__(self):
        self.trainingTexts = fu.readAllFilesFileNames(pathToTraining)
        self.keywords = readVocabulary()
        self.NDocumentos = fu.getNumberOfDocuments(pathToTraining)
    
    def getTextsOfCategory(self,category):
        return self.trainingTexts[category]

    def getTermsOfVocabulary(self,category):
        return self.keywords[category]

    def getTextOfCategoryPlain(self,category):
        result =""
        for k,v in self.trainingTexts[category].items():
            result+= v+" "
        return result    

    def getTermsPlain(self):
        result = []
        for k,v in self.keywords.items():
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