#slice is to take out particular text from a string using their indexes
word = "Encyclopedia"
a = word[0] #will print out word at index 0
print(a)

#here [a:b:c] is the format
a = word[0:3:1] #where a is starting index, b is ending index and c is step
print(a)
a = word[0:3:2]
print(a) #it can be matched with previous output

#here [a:b:c] is the format
a = word[:5:1] #where a is blank indicating that string should start form beginning
print(a)

#here [a:b:c] is the format
a = word[::-1] #where -1 is used to reverse the string
print(a)

# this is automated slicing in case of avoiding error and counting long path

word = 'Encyclopedia'
a = word.index("cyc") #getting index of start
b = word.index("dia") #getting index of end

c = word[a:b] #declearing variable for storing the particular index
print(c) #printing sliced data