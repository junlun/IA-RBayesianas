import sys
import os.path
sys.path.append(os.path.realpath('.'))
import Preprocesador.FileUtils as fu
pathToDictionaries = "resources\\data\\dictionaries"
pathToTraining = "resources\\data\\training"

class Data:
    instance = None
    def __init__(self):
        if not Data.instance:
            Data.instance = Data.__Data()
    class __Data:
        def __init__(self):
            self.trainingTexts = fu.readAllFilesFileNames(pathToTraining)
            self.keywords = readVocabulary()
            self.NDocumentos = fu.getNumberOfDocuments(pathToTraining)
        
    def getTextsOfCategory(self,category):
        return self.instance.trainingTexts[category]

    def getTermsOfVocabulary(self,category):
        return self.instance.keywords[category]

    def getTextOfCategoryPlain(self,category):
        result =""
        for k,v in self.instance.trainingTexts[category].items():
            result+= v+" "
        return result    

    def getTermsPlain(self):
        result = []
        for k,v in self.instance.keywords.items():
            for line in v:
                spl = line.splitlines()
                for term in spl:
                    result.append(term)
        return result  
    def getTrainingTexts(self):
        return self.instance.trainingTexts  
    def getKeyWords(self):
        return self.instance.keywords
    def getNumberOfDocuments(self):
        return self.instance.NDocumentos    

def readVocabulary():
    result = dict()
    keywords = fu.readAllFilesFileNames(pathToDictionaries)["dictionaries"]
    for k,v in keywords.items():
        category = k.replace(".txt","")
        values = v.split("\r\n")
        result[category] = values
    return result   