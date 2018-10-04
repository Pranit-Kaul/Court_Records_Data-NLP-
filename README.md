# Court Records Data Wrangling and Natural Language Processing

BACKGROUND

To verify if a person has a court case by matching his/her Name and Address in the available court records.
However, this data is messy and in unstructured format (i.e. in the form of HTML files) which cannot be leveraged in existing form.

OBJECTIVE

->To extract CNR (Case Name Record) number information.

->To extract address and name information.

->To use the address information to identify subfields of the address

->CNR Number

  Abstraction
  
  Separation
  
->Relations using NLTK

  (e.g To classify father-son/grandfather-grandson relationship from only human readable complex phrases) 
  
->Petitioner and Respondent 
   Information abstraction(Name, Address and Advocate name)
   
   Address separation
     Sub-District, District and City/Village name
     
   Mobile number and Pin code  
->Word Frequency

->Accessing the data set of village names

 
Explanation & Approach

1.CNR Number

 a.Abstraction
 
 b.Separation
 
FILE: final_cnr1.py

Abstraction:-
•All <span>  tags are found in HTML code using BeautifulSoup library and the one with “CNR Number” text is picked.
	
 The CNR number is extracted from it.
 
Separation:-
•The CNR number is separated according to this pattern:
	
![alt text](https://github.com/Pranit-Kaul/Court_Records_Data-NLP-/blob/master/images/CNR.jpg)
  

2.Petitioner and Respondent 
FILE: final_pet1.py
  a.Information abstraction(Name, Address and Advocate name)
  • All <span> tags are found containing the class of the corresponding information table. 
   Eg. The tag containing petitioner information has the class: “Petitioner_Advocate_table”.
  • The content of the tags is analyzed and then the information is assigned to Name, Address and Advocate fields assuming a pattern observed in majority of the files.

b. Address separation
   Sub-District, District and City/Village name
   • Keywords are found by looking at the output of the word frequency file.
     These keywords are observed in the address file to look for patterns.
   • Keywords(“village”, “vill”, “distt” etc.)  are searched in the address fields.
   • The word after the keyword or before the keyword(two separate functions exist for this purpose) is used as the field found depending upon the two factors:-
  Pattern and Availability

3. Using Levenshtein Distance to adjust for numerous spelling errors in addresses .
   e.g New Deli instead of New Delhi in court record
   

  String matching:-
For this task a city/village data of approx 6,00,000 villages and cities in India is used. 
The following results are found to optimise the searching process:
No of districts: ~6000
Average No of villages in a district: 300-400
The search is optimised by first searching all the district names and then only searching those village 
and city names in the data that are in the district(s) matched. It works efficiently for cases with 90% correct
spellings and address fields without keywords. 
   Mobile number and Pin code
Regular expressions are used to find both. 
Mobile number is simply found by searching a 10 digit numeric entry in the data.
Pin code(6 digit) is observed to be in different formats and are handled by multiple regular expressions:
	XXXXXX
	XXX XX

4. Relations using NLTK

Part of speech(POS) tagging functionality of NLTK is used to identify grammar patterns like: “son of”, “daughter of” etc.
A tagged words trees is made and the required content is accessed. A sample tree structure:

![alt text](https://github.com/Pranit-Kaul/Court_Records_Data-NLP-/blob/master/images/nltk.jpg)

 
5. Word Frequency
FILE: final_wordfreq1.py 
APPROACH & EXPLANATION:-
• A corpus(text file: add.txt) is prepared using copying all addresses from the output address excel file.
• The corpus is read and all the words are stored as a list in lower case after removal of special character.
• FreqDist function is used from the NLTK library to count the most frequent words in the corpus. 
  The frequency distribution helps us to analyze the frequent occurring keywords in the addresses. 
  Eg. ‘Village’ and ‘Vill’ occurrence in the sample data files. 

Input File

Input HTML sample  file:
![alt text](https://github.com/Pranit-Kaul/Court_Records_Data-NLP-/blob/master/images/input.jpg)

Output schemas
![alt text](https://github.com/Pranit-Kaul/Court_Records_Data-NLP-/blob/master/images/schema.JPG)


RESOURCES

1. Stackoverflow
2. Kaggle
3. Udacity free courses
4. Book- Natural Language Processing with Python - o’reilly
5. Book – Python for Data Analysis - o’reilly
6. Individual sites of libraries: Pandas, Nltk, Csv, BeautifulSoup.


