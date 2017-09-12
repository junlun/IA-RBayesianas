import os
import sys
import codecs
import collections

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir = script_dir.replace("\src\Preprocesador","")

#Accede a la ruta dada y devuelve las lineas leidas del fichero.
def readFile(path):
    thePath = os.path.join(script_dir, path)
    file=codecs.open(thePath,"r",encoding='utf-8')
    lines = file.read().lower()
    file.close()

    return lines 

#Busca de manera recursiva todos los ficheros en la ruta dada, devuelve un dicccionario key: nombre de la carpeta,
#  value: textos de los ficheros dentro de la carpeta concatenados en un solo string
def readAllFiles(path):
    return __readAllFiles(path,dict())

#Busca de manera recursiva todos los ficheros en la ruta dada, devuelve un dicccionario key: nombre de la carpeta,
#  value: textos de los ficheros dentro de la carpeta concatenados en un solo string
def __readAllFiles(path,textos):
    
    basePath = path
    names = os.listdir(path)
    
    for directorio in names:
        newPath = os.path.join(basePath,directorio)
        if os.path.isfile(newPath):
            folderName = os.path.basename(basePath)
            
            value = textos.get(folderName,"")
            value +=readFile(newPath)
            textos[folderName] = value
        else:
            __readAllFiles(newPath,textos)    
    return textos

#Busca de manera recursiva todos los ficheros en la ruta dada, devuelve un dicccionario key: nombre de la carpeta,
#  value: textos de los ficheros dentro de la carpeta
def readAllFilesNotFlat(path):
    return __readAllFilesNotFlatPrivate(path,dict())

#Busca de manera recursiva todos los ficheros en la ruta dada, devuelve un dicccionario key: nombre de la carpeta,
#  value: textos de los ficheros dentro de la carpeta
def __readAllFilesNotFlatPrivate(path,textos2):
   
    basePath = path
    names = os.listdir(path)
    
    for directorio in names:
        newPath = os.path.join(basePath,directorio)
        if os.path.isfile(newPath):
            folderName = os.path.basename(basePath)
            
            value = textos2.get(folderName,[])
            value.append(readFile(newPath))
            textos2[folderName] = value
        else:
            __readAllFilesNotFlatPrivate(newPath,textos2)    
    return textos2

#Busca de manera recursiva todos los ficheros en la ruta dada, devuelve un dicccionario key: nombre del fichero, value: texto del fichero
def readAllFilesFileNames(path):
    return __readAllFilesFileNames(path,dict())

#Busca de manera recursiva todos los ficheros en la ruta dada, devuelve un dicccionario key: nombre del fichero, value: texto del fichero
def __readAllFilesFileNames(path,textos3):
    basePath = path
    names = os.listdir(path)
    
    for directorio in names:
        newPath = os.path.join(basePath,directorio)
        if os.path.isfile(newPath):
            folderName = os.path.basename(basePath)
            
            value = textos3.get(folderName,dict())
            value[directorio]=readFile(newPath)
            textos3[folderName] = value
        else:
            __readAllFilesFileNames(newPath,textos3)  
         
    return textos3
#Esribe source en el fichero de ruta dada
def writeFile(path, source):
    thePath = os.path.join(script_dir, path)
    file=codecs.open(thePath,"w+", encoding="utf-8")
    file.write(source)
    file.close()
#Devuelve el numero de documentos que hay en la ruta aportada
def getNumberOfDocuments(path):
    count = 0
    dict = readAllFilesNotFlat(path)
    for pair in dict.items():
        count += len(pair[1]) 
    return count
#Devulve un contador que contiene las ocurrencias de cada palabra en el texto dado
def countWordInText(word, text):
    res = 0
    count = collections.Counter(text.split())
    if word in count.keys():
        res = count.get(word)

    return res

#Comprueba si el string aportado es una dirección relativa desde la raiz del proyecto, en cuyo caso, la abre.
def urlchecker(url):
    result = url
    parts = url.split(".")
    if parts[-1] == "txt":
        result = readFile(url)
    return result    

