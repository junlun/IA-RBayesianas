import re
import collections
import FileUtils

def discriminator(text):
    file = FileUtils.readFile("resources\\discriminator.txt")
    words = re.findall('\w+', file)
    
    for word in words:
        if word in text:
            text = text.replace(word, '')
    return text

def counter(text):
    print(text)
    words = re.findall('\w+', text)
    return collections.Counter(words)