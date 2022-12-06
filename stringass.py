#1
#.lower()
#This method changes all the string characters to lower case.
 
name = "Ilori Joshua"
print(name.lower())

#2
#.upper()
#This method changes all the string characters to upper case.
 
name = "this will change to uppercase"
print(name.upper())
 
#3
#.title()
#This method capitalizes the first letter of each word in a string.
 
sentence = "joshua's essay cover "
print(sentence.title())
 
#4
#.strip()
#This method removes whitespaces from the beginning and end of a string.
 
line = " Helloo joshua  "
print(line.strip())

#5
#.split()
#This method splits a string at a given argument or at spaces by default.
 
line = "written by jia-ayo"
print(line.split())

#6
#.join()
#This method joins an array of strings separated by a delimiter (, in the example below).
 
arr = ["jia-ayo", "is", "a", "writter"]
print(",".join(arr))

#7
#.find()
#This method searches for the first reference of a specified element in a string and returns its index.
 
text = "i am the internet top G"
print(text.find("t"))
 
#8
#.count()
#This method returns the number of times an element occurs in a string.
 
text = "I am joshua. This is joshua."
print(text.count("joshua"))

#9
#.replace()
#This method replaces an element with another in a string.
 
text = "I love python programming language"
print(text.replace("python", "rust"))
 
#10
#.isalpha()
#This method returns True if all the characters in a string are alphabet else, it returns False .
 
text = "joshua"
print(text.isalpha())
text = "jia-ayo"
print(text.isalpha())

