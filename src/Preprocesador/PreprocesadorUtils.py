import re
import collections
import sys
import os
import os.path
sys.path.append(os.path.realpath('.'))
import src.Preprocesador.FileUtils as FileUtils

def discriminator(text):
    file = FileUtils.readFile("resources\\discriminator.txt")
    words = re.findall('\w+', file)
    text = text.replace(os.linesep, ' ') #Se eliminan los caracteres de retorno de carro y salto de línea
    text = text.replace('\ufeff', ' ') #Se eliminan los caracteres de inicio de texto
    for word in words:
        s = ' ' + word + ' '
        if s in text:
            text = text.replace(s, ' ')
    return text

def counter(text):
    words = re.findall('\w+', text)
    return collections.Counter(words)