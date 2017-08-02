import os
import sys 

class Recolector:
    
    basePath= sys.argv[0].replace("/src/Preprocesador/Recolector.py","")
    @staticmethod
    def readFile(path):
       
        file=open(Recolector.basePath+path,"r")
        lines = file.readlines()
        
        result =""
        for line in lines:
            result += line
        return lines
    @staticmethod
    def readAllFiles(path):
        return True
