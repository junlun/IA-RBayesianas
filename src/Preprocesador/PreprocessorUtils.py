import re
import collections
import Recolector

def discriminator(text):
    file = Recolector.Recolector.readFile("resources\\discriminator.txt")
    words = re.findall(r'\w+', file)
    print(words)
    for word in words:
        if word in text:
            text = text.replace(word, '')
    print(text)
    return text

def counter(text):
    words = re.findall(r'\w+', text.lower())
    return collections.Counter(words)
