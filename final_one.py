from bs4 import BeautifulSoup #beautiful soup- installed 3rd party package
import csv
import re #regular expression
import os
import timeit

start = timeit.default_timer()

def cnr_no_sep(cnr_no,key):#separates and writes CNR Number
    writer.writerow({'File Name': key , 'State':cnr_no[:2] ,'District':cnr_no[2:4],
                     'Sub District':cnr_no[4:6],'CNR Number':cnr_no[7:13],'Year':cnr_no[14:18]})

def cnr_no_na(key):#Called when CNR Number not found
     writer.writerow({'File Name': key , 'State':"NA" ,'District':"NA",
                      'Sub District':"NA",'CNR Number':"NA",'Year':"NA"})

    
def find_add(add_field,word):#Find address information:Village,district etc
        add_field=add_field.lower()
        searchobj3=re.search(word,add_field)
        if(searchobj3):
            m = re.search( word +" (\w+)", add_field)
            if(m): 
                return m.group(1)
            else:
                n = re.search("(\w+) "+word, add_field)
                if(n): 
                    return n.group(1)
        else:
            return None

def find_add_rev(add_field,word):#Find address info in reverse... For information like "...." Nagar
        add_field=add_field.lower()
        searchobj3=re.search(word,add_field)
        if(searchobj3):
            
            m = re.search("(\w+) "+word, add_field)
            if(m):
                return m.group(1)
            else:
                n = re.search(word+" (\w+)", add_field)
                if(n):
                    return n.group(1)
        else:
            return None

        
def write_add(add_field):#write separated address
    village=find_add(add_field,"village")
    if(village==None):village=find_add(add_field,"vill")

    district = find_add(add_field,"district")
    if(district==None):district = find_add(add_field,"distt")
    
    writer3.writerow({'File Name':key,'Address':add_field,'Village':village , 'District':district,'Sub-District': find_add(add_field,"taluk"),
                      'Nagar':find_add_rev(add_field,"nagar"),
                      'House':find_add_rev(add_field,"house"),'Road':find_add_rev(add_field,"road")})#calls find_add() and find_add_rev()
    

def find_pin(add_field):#prints 6 digit pin code in any format
    pin_searchobj1=re.search("\D(\d{3})\D{0,1}(\d{3})\D",add_field)
    pin_searchobj2=re.search("\D(\d{3})\D{0,1}(\d{3})$",add_field)
    if(pin_searchobj1):
        pin = re.sub("\D","",pin_searchobj1.group())#remove spaces and character
        print (pin)
    elif(pin_searchobj2):
        pin = re.sub("\D","",pin_searchobj2.group())#remove spaces and character
        print (pin)

def find_mob(add_field):#prints 10 digit mobno
    mob_searchobj = re.search("(\d{10})",add_field) 
    if(mob_searchobj):
        print (mob_searchobj.group())

def extractInfoPrint(table_name,key,wr):#extracts name,address and advocate information
    all_tables = soup.find_all('span',class_=table_name+"_Advocate_table")
    
    
    for elem in all_tables:
        elem.contents
    list = []
    
    for a in elem.contents:
        
        if(str(a)!="<br/>"):
            list.append(str(a))

    for i in range(0,len(list)): 
        
        list[i]=re.sub("-","",list[i])
        searchobj = re.search("[Aa]ddress",list[i])#searches address string
        if(searchobj):
            list[i]=re.sub("[Aa]ddress", "", list[i])#removes "address" string
        
        searchobj2 = re.search("[Aa]dvocate",list[i])#searches advocate string
        if(searchobj2):
            list[i]=re.sub("[Aa]dvocate", "", list[i])#removes "advocate" string
        
        if(i%3==1):
            add_field=list[i].lower()
            find_pin(add_field)
            find_mob(add_field)
            write_add(add_field)#separates address and writes in a separate field
    k=0
    
    while(k<len(list)):
            #catches an exception:if index out of bounds 
            try:
                knext1 = list[k+1]
            except IndexError:
                knext1 = None
            try:
                knext2 = list[k+2]
            except IndexError:
                knext2 = None
            name=re.sub("\d","",list[k])#removes numbers from names
            name=re.sub("\)","",name)#removes this bracket from names
            wr.writerow({'File Name': key ,'Name':name,'Address':knext1,'Advocate':knext2})
            k=k+3
        
    
files=os.listdir("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python36-32\\htmlFiles\\")#lists all files
file_list=[]
cnr_list=[]
keys=files
#fieldnames for separate csv files
fieldnames = ['File Name', 'State','District','Sub District','CNR Number','Year']#cnr number
fieldnames2 = ['File Name','Name', 'Address', 'Advocate']#petitioner and respondent table
fieldnames3 = ['File Name','Address','Village','District','Sub-District','Nagar','House','Road']#address details

with open('write.csv', 'w', newline='') as csvfile, open('write2.csv','w',newline='') as csvfile2,open('write3.csv','w',newline='') as csvfile3,open('write4.csv','w',newline='') as csvfile4:

    #writers:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer2 = csv.DictWriter(csvfile2,fieldnames=fieldnames2)
    writer3 = csv.DictWriter(csvfile3,fieldnames=fieldnames3)
    writer4 = csv.DictWriter(csvfile4,fieldnames=fieldnames2)
    #writing headers
    writer.writeheader()
    writer2.writeheader()
    writer3.writeheader()
    writer4.writeheader()
    
    for file in files:#accessing each file in the folder
        key = file#stores file name for printing to csv later
        file = "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python36-32\\htmlFiles\\"+file
        cnr_found=0#cnr found flag
        doc = open(file,"r")

        abc = doc.read()

        soup = BeautifulSoup(abc,"html.parser")

        all_tables = soup.find_all('span')#finds all span tags
        
        for elem in all_tables:
            if(elem.string=="CNR Number"):#finds span with "CNR Number" text
                cnr_found=1
                cnr = elem.parent#accesses parent of the span
                cnr=cnr.contents[len(cnr.contents)-1]#observed pattern:last content is CNR Number
                
                #remove unwanted spaces and characters
                cnr = re.sub(":","",cnr)
                cnr = re.sub("\s","",cnr)
                
                cnr_no_sep(cnr,key)#separate CNR Number
        if(cnr_found==0):#if CNR not found
            cnr_no_na(key)
        
        extractInfoPrint("Petitioner",key,writer2)#writes Petitioner table data
        #extractInfoPrint("Respondent",key,writer4)#writes Respondent table data





stop = timeit.default_timer()

print ("TIME TAKEN:",stop - start)#total running time
print("NUMBER OF FILES:",len(files))#total number of files processed

