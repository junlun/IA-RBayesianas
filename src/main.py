import sys
import os.path

sys.path.append(os.path.realpath("."))
import Preprocesador as fu
import Clasificador.Knn as knn
import Clasificador.NaiveBayes as naive
import test.Tester as test


def main():
    messages = ["Generar diccionarios automáticamente","Clasificar desde consola con ambos algoritmos",
    "Clasificar textos de la carpeta test con ambos algoritmos","Clasificar un texto desde consola con Naive Bayes",
    "Clasificar un texto desde consola con Knn","Clasificar los textos de la carpeta test con Naive Bayes",
    "Clasificar los textos de la carpeta test con Knn"]
    print("seleccione acción a realizar:")
    for i, m in enumerate(messages):
        print(i+1,". ", m)

    selection = input("opción elegida: ")
    selection = int(selection)
    if selection == 1:
        fu.Preprocesador.createDictionaries()
        print("diccionarios creados")

    if selection == 2:
        texto = input("teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt) ")
        na = naive.ClasificadorNaiveBayes.clasifica(texto)
        kn = knn.ClasificadorKNN.clasifica(texto)
        print("resultado con Naive Bayes:")
        print(na)
        print("resultado con Knn:")
        print(kn)
        
    if selection == 3:
        verbose = input("desea ver la estructura de clasificacion? S/N")
        verbose = verbose == "S"
        print("Knn: ")
        test.testKnn(verbose)
        print("Naive Bayes: ")
        test.testNaiveBayes(verbose)

    if selection == 4:
        texto = input("teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt) ")
        print("categoría calculada: ",naive.ClasificadorNaiveBayes.clasifica(texto))

    if selection == 5:
        texto = input("teclee el texto que quiere clasificar o la dirección al mismo desde la raiz del proyecto (ej: resources\\data\\dictionaries\\1.txt) ")
        print("categoría calculada: ",knn.ClasificadorKNN.clasifica(texto))    

    if selection == 6:
        verbose = input("desea ver la estructura de clasificacion? S/N ")
        verbose = verbose == "S"
        test.testNaiveBayes(verbose)

    if selection == 7:
        verbose = input("desea ver la estructura de clasificacion? S/N ")
        verbose = verbose == "S"
        test.testKnn(verbose)          

while True:
    main()