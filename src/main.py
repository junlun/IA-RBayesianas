import sys
import os.path
print(sys.path)
sys.path.append(os.path.realpath("."))
print(os.path.realpath("."))
import Preprocesador as pre
import Clasificador.Knn as knn
import Clasificador.NaiveBayes as naive
import test.Tester as test


def main():
    messages = ["Generar diccionarios automáticamente","Clasificar desde consola con ambos algoritmos",
    "Clasificar textos de la carpeta test con ambos algoritmos","Clasificar un texto desde consola con Naive Bayes",
    "Clasificar un texto desde consola con Knn","Clasificar los textos de la carpeta test con Naive Bayes",
    "Clasificar los textos de la carpeta test con Knn","Recalcular Pesos de ambos algoritmos",
    "Buscar la N óptima para Knn con el conjunto de test"]
    print("seleccione acción a realizar:")
    for i, m in enumerate(messages):
        print(i+1,". ", m)

    selection = input("Opción elegida: ")
    selection = int(selection)
    if selection == 1:
        pre.createDictionaries()
        print("Diccionarios creados")

    if selection == 2:
        texto = input("Teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt) ")
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        na = naive.ClasificadorNaiveBayes.clasifica(texto)
        kn = knn.ClasificadorKNN.clasifica(texto, n)
        print("Resultado con Naive Bayes: ")
        print(na)
        print("Resultado con Knn: ")
        print(kn)
        
    if selection == 3:
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)

        verbose = input("¿Desea ver la estructura de clasificación? S/N: ")
        verbose = verbose == "S"
        print("Knn: ")
        test.testKnn(verbose, n)
        print("Naive Bayes: ")
        test.testNaiveBayes(verbose)

    if selection == 4:
        texto = input("Teclee el texto que quiere clasificar o la dirección al mismo desde la raíz del proyecto (ej: resources\\data\\dictionaries\\1.txt): ")
        print("Categoría calculada: ",naive.ClasificadorNaiveBayes.clasifica(texto))

    if selection == 5:
        texto = input("Teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt): ")
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)
        print("Categoría calculada: ",knn.ClasificadorKNN.clasifica(texto, n))    

    if selection == 6:
        verbose = input("¿Desea ver la estructura de clasificacion? S/N: ")
        verbose = verbose == "S"
        test.testNaiveBayes(verbose)

    if selection == 7:
        n = input("Introduzca el número de vecinos deseado para el cálculo del KNN (por defecto 30): ")
        if n == "":
            n = 30
        else:
            n = int(n)
        verbose = input("¿Desea ver la estructura de clasificacion? S/N: ")
        verbose = verbose == "S"
        test.testKnn(verbose, n)
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