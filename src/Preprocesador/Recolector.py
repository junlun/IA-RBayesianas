import os
import sys

script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
script_dir = script_dir.replace("\src\Preprocesador","")
textos = dict()

def readFile(path):
    thePath = os.path.join(script_dir, path)
    file=open(thePath,"r")
    lines = file.read().lower()
    
    
    return lines 

def readAllFiles(path):
    
    basePath = path
    names = os.listdir(path)
    
    for directorio in names:
        newPath = os.path.join(basePath,directorio)
        if os.path.isfile(newPath):
            array = textos.get(newPath.replace(directorio,""),[])
            array.append(readFile(newPath))
            textos[newPath.replace(directorio,"")] = array
        else:
            readAllFiles(newPath)    

    return names

print(readAllFiles("resources"))
print(textos)