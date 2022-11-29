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

##DATA TYPE



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

##RANDOM NUMBER 


python does nott have a random() function to make a random number 

import the random module , and display a random number between 1 and 9

```
import random

print(random.randrange(1, 10))
```


##String

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

##string slice

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

##Modefiy String

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