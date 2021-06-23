#string “ “ or ‘’
#Output a string containing a single quote
print('I\'m happy')
print("I\'m happy")
print("\"hi\"")
 
#newline \n create multi-line putput
print('One\nTwo\nThree')

print('One\tTwo\tThree') #with a tab space

print('''this is a multiline text''')  #same line
print('''this 
      is
          a
            multiline 
                    text''')
print("""this is a multiline text""") #same line
print("""this 
is
a
multiline
text""")

#Concatenation
"""Concatenation strings in Python can be added,using a process called 
concatenation, which can be done on any two strings"""

print("giselle" + "chen") #gisellechen
print("giselle","chen")  #giselle chen 
print("2" + "2")  #must be ""#22
print("1.0"+"1.0") #1.01.0

#sring Operations
"""
str + int = error
str * str = error
str + str = strstr
str * int = int *str = strstrstr....int multiple 
str * float = error
"""
print("Love"*3)
print("Love\n"*3)
print("Love\nU"*3)
print("Love\nU"*3+"me")
print("U"+"Love\nU"*3+"me")
print("U"+"Love\nU"*3+"Love")
print(4*'2')

#variabls
'''字母、字串、底線、數字結尾都可以'''
x = "str"
print(x*20) # = str * int

# input
''' to  get input from the user in Python, you can use the intuitively named 
input function. The inout fuction prompts the user for input, and returns what 
they enter as a string'''

name = input("Enter your name: ")
print('hello\t'+ name)  #Hello name
print('hello'+ name)    #Helloname

#IN-Place Operators
'''
In-place operators aloow you to write code like "x=x+3" more concisely,
as "x +=3". The same thin g is possible with other operators such as -,*,/ and % as well
And it can be used on the strings too.
'''

y = 2
print(y)
y +=2   #y=y+, +=5中間不能空格
print(y)
y*=2   #y=y*2
y/=2  #y=y/2
y//=22  #y=y//2

z ="spam"
print(z)
z +="egg"


#walrus operator
'''
it aloows you assign values to variables within an expression, including 
variables that do not exist yet.
Let's suppose we take an integer from the user, assign it to a variable num
and output.
'''
name = input('Enter your name:')
print ("I'm",name,"!") #,會產生空格
print ("I'm" + name+"!") #+會連在一起
print ("I'm" , name+"!")
 

