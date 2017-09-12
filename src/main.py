import sys
import os.path
sys.path.append(os.path.realpath("."))
from Preprocesador import Preprocesador as pre
import Clasificador.Knn as knn
import Clasificador.NaiveBayes as naive
import test.Tester as test
import time


def main():
    messages = ["Generar diccionarios automáticamente","Clasificar desde consola con ambos algoritmos",
    "Clasificar textos de la carpeta test con ambos algoritmos","Clasificar un texto desde consola con Naive Bayes",
    "Clasificar un texto desde consola con Knn","Clasificar los textos de la carpeta test con Naive Bayes",
    "Clasificar los textos de la carpeta test con Knn","Recalcular Pesos de ambos algoritmos",
    "Buscar la N óptima para Knn con el conjunto de test"]
    print("Seleccione acción a realizar:")
    for i, m in enumerate(messages):
        print(i+1,". ", m)

    selection = input("Opción elegida: ")
    selection = int(selection)

    if selection == 1:
        n = input("Introduzca el número de palabras que contendrán los diccionarios (por defecto 20): ")
        if n == "":
            n = 20
        else:
            n = int(n)
        pre.createDictionaries(n)
        print("Diccionarios creados")

    if selection == 2:
        texto = input("Teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt) ")
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)
        t1I = time.time()
        na = naive.ClasificadorNaiveBayes.clasifica(texto)
        t1F = time.time()
        kn = knn.ClasificadorKNN.clasifica(texto, n)
        t2F = time.time()
        print("Resultado con Naive Bayes: ")
        print("Resultado: ",na," tiempo transcurrido (s): ",float((t1F-t1I)))
        print("Resultado con Knn: ")
        print("Resultado: ",kn," tiempo transcurrido (s): ",float((t2F-t1F)))
        
    if selection == 3:
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)

        verbose = input("¿Desea ver la estructura de clasificación? S/N: ")
        verbose = str(verbose).upper() == "S"
        print("Knn: ")
        t1I = time.time()
        test.testKnn(verbose, n)
        t1F = time.time()
        print("Tiempo transcurrido (s): ",float((t1F-t1I)))
        print("Naive Bayes: ")
        t2I = time.time()
        test.testNaiveBayes(verbose)
        t2F=time.time()
        print("Tiempo transcurrido (s): ",float((t2F-t2I)))

    if selection == 4:
        texto = input("Teclee el texto que quiere clasificar o la dirección al mismo desde la raíz del proyecto (ej: resources\\data\\dictionaries\\1.txt): ")
        t1I = time.time()
        na = naive.ClasificadorNaiveBayes.clasifica(texto)
        t1F = time.time()
        print("Resultado: ",na," tiempo transcurrido (s): ",float((t1F-t1I)))
        

    if selection == 5:
        texto = input("Teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt): ")
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)
        t1I = time.time()
        kn = knn.ClasificadorKNN.clasifica(texto, n)
        t1F = time.time()
        print("Resultado: ",kn," tiempo transcurrido (s): ",float((t1F-t1I)))   

    if selection == 6:
        verbose = input("¿Desea ver la estructura de clasificacion? S/N: ")
        verbose = str(verbose).upper() == "S"
        t1I = time.time()
        test.testNaiveBayes(verbose)
        t1F = time.time()
        print("Tiempo transcurrido (s): ",float((t1F-t1I)))

    if selection == 7:
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)
        verbose = input("¿Desea ver la estructura de clasificacion? S/N: ")
        verbose = str(verbose).upper() == "S"
        t1I= time.time()
        test.testKnn(verbose, n)
        t1F = time.time()
        print("Tiempo transcurrido (s): ",float((t1F-t1I)))
    if selection == 8:
        print("Refrescando pesos... ")
        knn.ClasificadorKNN.refrescaPesos()      
        naive.NaiveBayesTrainingValues.generaValores()
        print("pesos correctamente refrescados")   
    if selection == 9:
        print("optimizando N para el conjunto de test...")
        test.optimiceN()         
       

while True:
    main()