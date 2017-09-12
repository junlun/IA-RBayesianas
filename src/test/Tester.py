import sys
import os.path
sys.path.append(os.path.realpath("."))
import Preprocesador.FileUtils as fu
import Clasificador.Knn.ClasificadorKNN as knn
import Clasificador.NaiveBayes.ClasificadorNaiveBayes as naive

pathToTest = "resources\\data\\test"

def testKnn(verbose, N=30):
    testFiles = fu.readAllFilesFileNames(pathToTest)
    
    result = dict()
    numberOfTrues = 0 
    for category,textos in testFiles.items():
        for nombre, texto in textos.items():
            clase = knn.clasifica(texto, N)
            result[category+"-"+nombre] = clase 
            if(clase == category):
                numberOfTrues = numberOfTrues +1
   
   
    percentage = numberOfTrues/len(result.keys())*100
    print("Porcentaje de acierto : ",percentage)
    if(verbose):
        print(result)
    return result

def _testKnn(N=30):
    testFiles = fu.readAllFilesFileNames(pathToTest)
    
    result = dict()
    numberOfTrues = 0 
    for category,textos in testFiles.items():
        for nombre, texto in textos.items():
            clase = knn.clasifica(texto, N)
            result[category+"-"+nombre] = clase 
            if(clase == category):
                numberOfTrues = numberOfTrues +1
   
   
    percentage = numberOfTrues/len(result.keys())*100
    return percentage

def testNaiveBayes(verbose):
    testFiles = fu.readAllFilesFileNames(pathToTest)
    
    result = dict()
    numberOfTrues = 0 
    for category,textos in testFiles.items():
        for nombre, texto in textos.items():
            clase = naive.clasifica(texto)
            result[category+"-"+nombre] = clase
            if(clase == category):
                numberOfTrues = numberOfTrues +1
   
   
    percentage = numberOfTrues/len(result.keys())*100
    print("Porcentaje de acierto : ",percentage)
    if(verbose):
        print(result)   
    return result

def optimiceN():
    maxPercentage = 0
    minPercetage = 101
    maxI = -1
    minI = 200
    for i in range(1,101):
        sys.stdout.write("Progreso: %d%%   \r" % (i) )
        sys.stdout.flush()
        newPercentage = _testKnn(i)
        if(newPercentage> maxPercentage):
            maxPercentage = newPercentage
            maxI = i
        if(newPercentage < minPercetage):
            minPercentage = newPercentage
            minI = i
    print("mejor valor de N encontrado en el rago [1,100]: ",maxI," con porcentaje de acierto", maxPercentage)        
    print("peor valor de N encontrado en el rago [1,100]: ",minI," con porcentaje de acierto", minPercentage)        
    return maxPercentage
