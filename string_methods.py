#strings in python

#couting a particular character or string
text = "happy birthday".count("a") #.count("a") counts the number of time a comes and this can be done for string as well
print(text)

#change the whole text to lower
x = "Happy Birthday"
Upper = x.upper() 
print(Upper)

#change the whole text to upper
Lower = x.lower() 
print(Lower)

#capitalizes the first letter
Capitalize = x.capitalize()
print(Capitalize) 

#capitalizes every word in x
Title = x.title() 
print(Title)

#checking different situation and printing respective answer in true of false
print(x.islower()) #check if x is lower
print(x.isupper()) #check if x is upper
print(x.istitle()) #check if x is title
print(x.isalpha()) #check if x is only character(Note: space is not a character)
print(x.isdigit()) #check if x is only digit
print(x.isalnum()) #check if x is alphanumeric value 

#check index of character(Note take care of cases while using find or index)
print(x.find("Birthday")) 
print(x.index("Birthday"))
#the difference between find and index in if a string doesn't match in find it gives -1 value whereas it'll give error in case of index

#removing a particular string
y = "00000000000Hello World000000000"
print(y.strip("0")) #remove all zero
print(y.lstrip("0")) #remove left zero
print(y.rstrip("0")) #remove right zero

#removing unecessary spaces at the end of the string
Text = "ABC sad     "
print(Text)
#length after stripping out uncessary spaces
print(len(Text))
Text = "ABC sad     ".strip()
print(Text)
#length after stripping out uncessary spaces
print(len(Text))
