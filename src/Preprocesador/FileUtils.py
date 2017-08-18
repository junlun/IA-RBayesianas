import os
import sys
import codecs

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir = script_dir.replace("\src\Preprocesador","")
textos = dict()


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
    result = dict()
    basePath = path
    names = os.listdir(path)
    
    for directorio in names:
        newPath = os.path.join(basePath,directorio)
        if os.path.isfile(newPath):
            folderName = os.path.basename(basePath)
            
            value = result.get(folderName,[])
            value.append(readFile(newPath))
            result[folderName] = value
        else:
            readAllFiles(newPath)    

    return result

def writeFile(path, source):
    thePath = os.path.join(script_dir, path)
    file=codecs.open(thePath,"w+",encoding='utf-8')
    file.write(source)
    file.close()

