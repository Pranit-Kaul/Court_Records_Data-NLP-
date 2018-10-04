import pandas as pd
from fuzzywuzzy import fuzz
import re
import csv


df = pd.read_csv('C:\\Users\\admin\\Downloads\\vill_dict.csv')
add = pd.read_csv('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python36-32\\add.csv')
add = add['Address']
#print ("DATAFRAME",df)
dist = df['District Name']
subdist = df['Sub-District Name']
vill = df['city']


fieldnames = ['Address','District Name','City/Village']
dist = dist.drop_duplicates()
subdist = subdist.drop_duplicates()

with  open('write5.csv','w') as csvfile:
    
    #writers:
    writer2 = csv.DictWriter(csvfile,fieldnames=fieldnames,restval='')
    #writing headers
    writer2.writeheader()

    
    selected1 =''
    for elem1 in add:
        #print elem1
        try:
            elem1 = re.sub("^[a-zA-Z\s]","",elem1)
        

            for elem in dist:
               
                m = fuzz.partial_ratio(elem ,elem1)
                if(m>82):
                    selected1 = elem


                    vill_sel = df.loc[df['District Name'] == selected1]
                

                    for elem in vill_sel['city']:
                        
                        m = fuzz.partial_ratio(elem ,elem1)
                        if(m>82):
                            selected2 = elem
                            if(selected1.strip()<>selected2.strip()):
                                #print "1."+ selected1
                                #print "2."+ selected2
                                writer2.writerow({'Address':elem1,'District Name':selected1,'City/Village':selected2})
                            

                selected1 = ''
                selected2 = ''
                        
        except TypeError:
            elem1
            #print "Oops!" #garbage data
            
