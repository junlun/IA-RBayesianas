import os
import sys
#from ...definitions import ROOT_DIR

class Recolector:
    #ROOT_DIR=os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
    script_dir = script_dir.replace("\src\Preprocesador","")
    
    @staticmethod
    def readFile(path):
        thePath = os.path.join(Recolector.script_dir, path)
        file=open(thePath,"r")
        lines = file.read().lower()
        
        
        return lines 
    @staticmethod
    def readAllFiles(path):
        basePath = path

        return True

print(Recolector.readFile("resources\prueba.txt"))