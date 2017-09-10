import sys
import os.path
sys.path.append(os.path.realpath("."))
import src.Preprocesador.FileUtils as fu
import src.Clasificador.Knn.ClasificadorKNN as knn
import src.Clasificador.NaiveBayes.ClasificadorNaiveBayes as naive

pathToTest = "resources\\data\\test"

def testKnn(verbose):
    testFiles = fu.readAllFilesFileNames(pathToTest)
    
    result = dict()
    numberOfTrues = 0 
    for category,textos in testFiles.items():
        for nombre, texto in textos.items():
            clase = knn.clasifica(texto)
            result[category+"-"+nombre] = clase == category
            if(clase == category):
                numberOfTrues = numberOfTrues +1
   
   
    percentage = numberOfTrues/len(result.keys())*100
    print("Porcentaje de acierto : ",percentage)
    if(verbose):
        print(result)
    return result

def testNaiveBayes(verbose):
    testFiles = fu.readAllFilesFileNames(pathToTest)
    
    result = dict()
    numberOfTrues = 0 
    for category,textos in testFiles.items():
        for nombre, texto in textos.items():
            clase = naive.clasifica(texto)
            result[category+"-"+nombre] = clase == category
            if(clase == category):
                numberOfTrues = numberOfTrues +1
   
   
    percentage = numberOfTrues/len(result.keys())*100
    print("Porcentaje de acierto : ",percentage)
    if(verbose):
        print(result)   
    return result