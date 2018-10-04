import nltk
import pandas as pd

df=pd.read_csv('C:\Users\Pranit\Desktop\write2.csv')
#print df['Address']
add=df['Address']
flag = 0
relation="RELATION:{<NN>{1}<IN>{1}<NNP>{1,2}}"
#elem = " son of Tari Singh fatehabad haryana in code 999999"
#print elem=elem.strip()
for elem in add:
    elem = str(elem)
    text=nltk.word_tokenize(elem)
    sentence=nltk.pos_tag(text)
    cp=nltk.RegexpParser(relation)
    result = cp.parse(sentence)   
    for subtree in result.subtrees():
        if subtree.label() == 'RELATION':
                
                print elem
                if(subtree[0][0] == 'son'):
                    if(flag):
                        print "GRAND FATHER/MOTHER'S NAME"
                        for i in range(2,10):
                            try :
                                print(subtree[i][0])
                            except IndexError:
                                #print "index error"
                                break
                    else:    
                        print "FATHER/MOTHER'S NAME"
                        for i in range(2,10):
                            try :
                                print(subtree[i][0])
                            except IndexError:
                                #print "index error"
                                break
                    flag = 1

    flag =0
