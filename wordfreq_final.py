
import nltk

import re





input_file = "C:\\Users\\admin\\Desktop\\address.txt"

fp = open(input_file, 'r')

words = fp.read()






words = words.split()
words = [word.lower() for word in words]

for i, word in enumerate(words):
    word = re.sub('[^a-zA-Z0-9\n]', '',word)
    word = re.sub(',','',word)
    words[i]=word


fdist = nltk.FreqDist(words)



for word, frequency in fdist.most_common(150):
    print(u'{};{}'.format(word,frequency))

