import sys
import os.path
sys.path.append(os.path.realpath('.'))
import src.Preprocesador.FileUtils as fu
import math
import src.InicializadorDatos as data

pathToData = "src\\Clasificador\\Knn\\trainingValues.txt"
pathToDictionaries = "resources\\data\\dictionaries"
vectores = dict()
data = data.Data()

class KNNTrainingValues:
    def __init__(self):
        self.keywords = data.getTermsPlain()
        #self.keywords = fu.readAllFiles(pathToDictionaries)["dictionaries"].split("\r\n")
        #self.keywords=self.keywords[0:len(self.keywords)-1]
        self.texts = data.getTrainingTexts()
        self.frecuenciasDocumentales=calcularFrecuenciasDocumentalsIniciales(self.keywords,self.texts)
        self.vectores = inicializar()

#Devuelve un diccionario leido desde el fichero de vectores, key: categoria-nombre del fichero, value: array de pesos
def inicializar():
    fileRead = fu.readFile(pathToData)
    lines = fileRead.split("\n")
    for line in lines:
        spl = line.split(",")
        category = spl[0]
        name = spl[1]
        id = category+"-"+name
        values = spl[2:len(spl)]
        vectores[id]=[float(i.strip()) for i in values]
    return vectores

#Dados los terminos, los documentos de entrenamiento y el diccionario de frecuencias documentales, escribe el fichero de vectores
def escribePesos(keywords,texts,fdocumentales):
    toWrite = ""
    for category,documents in texts.items():
        for name,text in documents.items():
            toWrite+=category+","+name+","
            for keyword in keywords:
               toWrite+=str(calculaPesoDocumento(keyword,text,fdocumentales[keyword]))+","
            toWrite = toWrite[0:len(toWrite)-1]
            toWrite += "\n"   

                
    fu.writeFile(pathToData,toWrite.strip())

#Dado un termino del vocabulario, un documento y la frecuencia documental inversa del termino, devuelve el peso del termino en 
#el documento
def calculaPesoDocumento(keyword,text,fdocumental):
    frecuencia = fu.countWordInText(keyword,text)
    return round(fdocumental*frecuencia,4)

#Dados los terminos del diccionario y los documentos de entrenamiento devuelve un diccionario, key: termino , value: f documental inversa
def calcularFrecuenciasDocumentalsIniciales(keywords,texts):
    n = fu.getNumberOfDocuments("resources\\data\\training")
    frecuenciaDocumental = dict()
    #buscamos la palabra en los documentos y contamos las ocurrencias
    for keyword in keywords:
        count = 0.
        for category,documents in texts.items():
            for name,text in documents.items():
                    if keyword in text:
                        count +=1

        if(count!=0):
            frecuenciaDocumental[keyword]=math.log(float(n/count))
        else:
            frecuenciaDocumental[keyword]=0 
    return frecuenciaDocumental 