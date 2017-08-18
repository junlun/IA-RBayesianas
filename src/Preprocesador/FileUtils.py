import os
import sys
import codecs
import collections

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir = script_dir.replace("\src\Preprocesador","")
textos = dict()
textos2 = dict()
textos3 = dict()


def readFile(path):
    thePath = os.path.join(script_dir, path)
    file=codecs.open(thePath,"r",encoding='utf-8')
    lines = file.read().lower()
    file.close()

    return lines 

def readAllFiles(path):
    
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
            readAllFiles(newPath)    

    return textos

def readAllFilesNotFlat(path):
    
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
            readAllFilesNotFlat(newPath)    
    return textos2

def readAllFilesFileNames(path):
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
            readAllFilesFileNames(newPath)  
         
    return textos3

def writeFile(path, source):
    thePath = os.path.join(script_dir, path)
    file=codecs.open(thePath,"w+",encoding='utf-8')
    file.write(source)
    file.close()

def getNumberOfDocuments(path):
    count = 0
    dict = readAllFilesNotFlat(path)
    for pair in dict:
        count += pair[1].size()
    return count

def countWordInText(word, text):
    res = 0
    count = collections.Counter(text.split())
    if word in count.keys():
        res = count.get(word)

    print(res)
    return res