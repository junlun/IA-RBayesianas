import sys
import os.path
sys.path.append(os.path.realpath("."))
import Preprocesador.FileUtils as fu
import math
import Clasificador.NaiveBayes.NaiveBayesTrainingValues as nb
import InicializadorDatos as data

probabilidades = nb.NaiveBayesTrainingValues().getProbabilidades()
data = data.Data()

#Calcula y clasifica un texto dado utilizando Naive Bayes
def clasifica(texto):
    texto = fu.urlchecker(texto)
    max = float('-inf')
    res = ""
    for p in probabilidades.items():
        product = 1
        categoria = p[0]
        pc = float(p[1][0]) #P(c) obtenido del fichero de entrenamiento
        vocabulary = data.getTermsPlain() #vocabulary = Todos los vocabularios aplanados en uno solo
        for word in vocabulary:
            if word in texto.split():
                numApariciones = fu.countWordInText(word, texto)
                product *= math.pow(float(p[1][vocabulary.index(word)+1]), numApariciones) #P(t,c) obtenido del fichero de entrenamiento teniendo en cuenta todas sus apariciones
        if max < pc*product:
            max = pc * product
            res = categoria

    return res