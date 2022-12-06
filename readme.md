***
label:   a widget used to display text on the scren

button:  abutton that can contain a text and can perform an actiion when clicked

entry:   a text entry widget that allows only a single line of text 

text:    a text entry widget that allows multiple text entry 

frame:   apercentage region used to group relaye widget provide 
***

```
         colum
    (0,0)| (1,0)| (2,0)
    _____ ______ ______
r   (0,1)| (1,1)| (2,1)
o   _____ ______ ______
w   (0,2)| (1,2)| (2,2)
    ______ ______ ______
    (0,3)| (1,3)| (2,3)
```
        
container.columnconfigure(index,weight)
container.rowconfigure(index, weight)

***
Parameter:    Meaning

column:      the column inde xwhere you want to place the widget

row:          the row index where you want to place the widget

rowspan:      set the number of adjacent rows that the widget

columnspan:   set the number of adjacent columns that the widget cn span 

sticky:       if the call is large than a widget , the sticky option specifies 
             which side the widget should stick to and howdistribute any extra 
             space within the cell that is not taken  up by the widget at its original size

padx:         add external padding above and below the widget

pady:        add external padding to the left and right of the weight

ipadx:       widget padx version

ipady:       widget pady version
***

##    DATA TYPE



numeric type:

int = no decimal only whole number 

float = this decimal or sientific number(35e3 e=exponential)

complex= j imagerinary part and normal number are real part

Type Convertion

you can convert from one type to another with int () ,float(), and complex()
```
x=1
y=2.8
z-1j
```

convert from int to float 
```
a = float(x)
```

convert from float to int 
```
b= int(y)
```

convert from int to complex 
```
c= complex(x)
```
NOTE: cant convert from complex to other data type

    ##    RANDOM NUMBER 


python does nott have a random() function to make a random number 

import the random module , and display a random number between 1 and 9

```
import random

print(random.randrange(1, 10))
```


    ##    String

string length

to get the length of  a string, use the len() function

```
a= "hello, python!"
print(len(a))
```
check string

to check if a certaiun phrase or character is present in a string , we can use the keyword in

check if "free" is present in the following text:

```
text = "the best things in life are free"
print("free" in txt)

if "free" in txt:
  print("yes freee present")

if "expensive" not in text:
   print("expensive not available")
```

##    string slice

you can return a range of character by using the slice syntax.

specify the start index 

```
b = "hello word"
print (b[2:5])
```

slice from start 
```
b = "hello word"
print (b[:5])
```

slice to end 

```
b = "hello word"
print (b[2:])
```

##    Modefiy String

uppercase
```
b = "hello word"
print (b.upper())
```
lowercase
```
b = "HELLO word"
print (b.lower())
```

REPLACE A String

```
b = "hello word"
print (b.replace("h" "j"))
```



SPLIT STRING

```
b = "hello word"
print (b.split(",")#returns['hello','world'])
```
*ASSIGMENT*

*10 STRING METHOD AND HOW THEY WORK*

*.lower()*

This method changes all the string characters to lower case.
```
name = "Ashish"
print(name.lower())
#Output: ashish
```
*.upper()*

This method changes all the string characters to upper case.
```
name = "Ashish"
print(name.upper())
#Output: ASHISH
```
*.title()*

This method capitalizes the first letter of each word in a string.
```
sentence = "i am ashish"
print(sentence.title())
#Output: I Am Ashish
```

*.strip()*

This method removes whitespaces from the beginning and end of a string.
```
line = "      Hey!      "
print(line.strip())
#Output: Hey!
```
*.split()*

This method splits a string at a given argument or at spaces by default.
```
line = "This is a blue lion"
print(line.split())
#Output: ["This","is","a","blue","lion"]
```
*.join()*

This method joins an array of strings separated by a delimiter (, in the example below).
```
arr = ["Sky", "is", "red"]
print(",".join(arr))
#Output: Sky,is,red
```
*.find()*

This method searches for the first reference of a specified element in a string and returns its index.
```
text = "The water is green"
print(text.find("t"))
#Output: 6
```
This method functions similarly to index() except that index() method raises an exception if the element is not found in the string.

*.count()*

This method returns the number of times an element occurs in a string.
```
text = "I am Ashish. This is Ashish."
print(text.count("Ashish"))
#Output: 2
```
*.replace()*

This method replaces an element with another in a string.
```
text = "I love Java"

print(text.replace("Java", "Python"))
#Output: I love Python
```
*.isalpha()*

This method returns True if all the characters in a string are alphabet else, it returns False .
```
text = "Python"
print(text.isalpha())
#Output: True
text = "Python2022"
print(text.isalpha())
#Output: False
```

##      PYTON LAMBDA


```
x = lambda a:a + 10
#add 10 to argument a, and return  the result
# x=lambda a is the argument while a +10 is the expression
print(x(5))
#value of arguement was supllied in the print statement

```
multiply argument a with argument b and return the result 
```
x= lambda a, b: a * b
print(x(5, 6))
```
summerixe argument a, b and c and return the result:
```
x = lambda a,b,c : a + b + c
print(x(5,6,2))
```

##     STRING FORMAT

we cannot combine strings and numbers like this :

the format()method takes the passed arguments formats them and places them in the string where the placeholders {}are :

```
age = 40
txt = "my name is jone snow, and i am {}"
print(txt.format(age))


quantity= 3
item_tag_no= 567
price = 49.95

myorder = "i want to pay {} dollars for {} pies of item {}"
print(myorder.format(quantity, item_tag_no, price))
```

## escape characters in python programming

code:   result 
\':     single Quote

\:     backslash is one backlash

\n:     new line

\r:     new line

\t:     tab

\b:     backspace 

## python operetor 
operator are used to perform operation on variables and values for instance

#### types of operator
arthemethic operator

assignment operator

comparrison operator

logical operator

identity operator

membership operator 

bitwise  operator


## python list 

list uses [] list can hold several sata type

#### Acessing list items

it can be accessed by using the index
```
thislist=["apple", "banana", "cherry"]
print(thislist[1])

#negative index starts from the back 

list=["apple", "banana", "cherry"]
print(list[-1])
#output cherry

```
#### changing list item value 

to change item at specific index 
```
thislist = ["apple", "banna", "watermellon"]
thislist[1]= "water"
print(thislist)
```
### methods
insert: this helps to input new value 

.insert()

remove: to remove an object from list

.remove()

clear: this empties the whole list 

.clear()

sort: this arranges the alphabatically or numericly

.sort()

reversort

## Tuple
it is written in ()

thet can not be changed cause they are imutable by nature

but walk around by turning into list to modify to turn bAack into turple

```
x= ("appple", "banna", "cherry")
y = list(x)
y[1] = "fish"

```

## Python Set 

set are used to store multiple item in a single variable

they are written  with {}

duplicate are not allowed in set

they can not be changed but additional items can be added 
