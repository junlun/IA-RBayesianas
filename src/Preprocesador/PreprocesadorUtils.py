import re
import collections
import FileUtils

def discriminator(text):
    file = FileUtils.readFile("resources\\discriminator.txt")
    words = re.findall('\w+', file)
    
    for word in words:
        s = ' ' + word + ' '
        if s in text:
            text = text.replace(s, '')
    return text

def counter(text):
    words = re.findall('\w+', text)
    return collections.Counter(words)