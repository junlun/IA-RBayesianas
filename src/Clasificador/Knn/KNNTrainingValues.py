import sys
import os.path
sys.path.append(os.path.realpath('.'))
import src.Preprocesador.FileUtils as fu


pathToData = "src\\Clasificador\\Knn\\trainingValues.txt"
pathToDictionaries = "resources\\data\\dictionaries"
vectores = dict()


def inicializar():
    calculaPesosDiccionario()
    fileRead = fu.readFile(pathToData)
    lines = fileRead.split("\n")
    for line in lines:
        spl = line.split(",")
        name = spl[0]
        values = spl[1:len(spl)]
        vectores[name]= values
    return vectores


def calculaPesosDiccionario():
    keywords = fu.readAllFiles(pathToDictionaries)["dictionaries"]
    keywords = keywords.split("\r\n")
    keywords = keywords[0:len(keywords)-1]
    texts = fu.readAllFilesFileNames("resources\\data\\training")
    fdocumental = calculaFrecuenciaDocumental(keywords,texts)
    toWrite = ""
    for category,documents in texts.items():
        for name,text in documents.items():
            toWrite+=name+","
            for keyword in keywords:
               toWrite+=str(calculaPesoDocumento(keyword,name,text,fdocumental[keyword]))+","
            toWrite = toWrite[0:len(toWrite)-1]
            toWrite += "\n"   

                
    fu.writeFile(pathToData,toWrite.strip())

def calculaPesoDocumento(keyword,name,text,fdocumental):
    frecuencia = fu.countWordInText(keyword,text)
    return round(fdocumental*frecuencia,4)

def calculaFrecuenciaDocumental(keywords,texts):
    n = fu.getNumberOfDocuments("resources\\data\\training")
    frecuenciaDocumental = dict()
    #buscamos la palabra en los documentos y contamos
    
    for keyword in keywords:
        count = 0
        for category,documents in texts.items():
            for name,text in documents.items():
                    if keyword in text:
                        count +=1

        count*=1.
        if(count!=0):
            frecuenciaDocumental[keyword]=float(n/count)
        else:
            frecuenciaDocumental[keyword]=0 

    return frecuenciaDocumental                  
