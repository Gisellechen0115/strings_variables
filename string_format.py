#string formatting 字串格式化
'''
so far, to combine strings and non-strings, ypu've converted the non string 
to strings and add them. String formatting provides a more powerful way to 
embed non-strings within strings. String formatting uses a string's format methos 
to substitude a numer of arguments in the strings.
'''
nums =[4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)  #Numers: 4 5 6


#leave them blank, the format items listed are inserted in order.
nums = [4, 5, 6]
msg = "Numbers:{} {} {}".format(nums[0], nums[1], nums[2])
print(msg)  #Numers: 4 5 6
print(msg[0])   #N
print(msg[5])   #s
print(msg[8])   #4


a ='Zero'
b ='One'
c ='Danger'
print('{2}{0[0]}{0[3]}{1[1]}{1[2]}'.format(a,b,c))

#FORMAT可以是變數，也可以是字串也可以是數字
print("{0} {1} {0}".format("abra","cad"))
     
nums= "Numbers:{0}{1}{3}".format(4, 8, 3, 6) 
print(nums)  #Numbers: 4 8 6

#也可以直接把FORMAT寫進變數裡面
a = "{x},{y}".format(x=3, y=12)
print(a)

'''
a = "{0},{1},{x},{y},{2}".format(1, 3, x=5, y=12, 15)
print(a)
SyntaxError:positional argument follows keyword argument
'''

a = "{0},{1},{x},{y},{2}".format(1, 3, 15, x=5, y=12)
print(a)

'''
a = "{0},{1},{x},{y},{2}".format(x=5, y=12)
print(a)  #IndexError: tuple(a structure of data that has several parts) index out of range
'''


name = input("請輸入名子: ")
age = input("請輸入年齡: ")
hi = name + " is {age} year old".format(age = int(age))  #G is 36 year old#字串空格也會留下
hii= name , "is {age} year old".format(age = int(age)) #('F', 'is 36 year old') 
print(hi)
print(hii)


lst = ['a','b','c','g','i','a','a']
lst = "".join(lst)    
print(lst)   #abcgiaa，把list連結一起，用空格
lst = lst.replace("a","i")  #把"a"用"i"取代
lst = list(lst) #再把他們變回LIST
print(lst)  
#上面的寫法再濃縮
lst = ['a','b','c','g','i','a','a']
lst = list("".join(lst).replace("a","i") )
print(lst)  



print('This is a sentence.'.startswith('This'))  #True
print('This is a sentence.'.endswith('sentence')) 
print('AN ALL CAPS Sentence'.lower())  #an all caps sentence(全部變小寫)
print('an All CAPS Sentence'.upper()) #AN ALL CAPS SENTENCE(全部變大寫)
print('this is a sentence.'.capitalize())
print('spam, eggs, ham'.split(','))  #['spam', ' eggs', ' ham'] (分開列成清單)

'''
it sorted the list string elements. You can pick if you want it on 
ascending or descending order. it's descending by default.
它對列表字符串元素進行排序。您可以選擇是按升序還是降序排列。默認情況下它是下降的。
'''

def desc(number):
    return int("".join(sorted(str(number))))
def asc(number):
   # return int("".join(sorted(str(number)),reverse = True)) #與下行答案一樣，但不知問題在哪
    return int("".join(sorted(str(number))[::-1]))
print(desc(53716),asc(53716))
 


txt =[">","<"]
for i in range(1,10):
    str= "@"* i
    print(str.join(txt))
print(".................")
print(str.join(txt))    #>@@@@@@@@@<

'''
the syntax of join() is not ver convertional. In other languages join() is a
 methos of arrays and takes one arguement which is the " glue" between the 
 elements. In python, join() is a methos of strings(the "glue") and take the 
 array/list as argument.
 '''
 
reply= str(input("<prompt>"))
if "GO" in reply.upper():  #這樣不換輸入大寫寫GO，都能讀取到
    print("Let\n's Go")  #Let(換行了 ) 's Go
    print('Let is go')
    
    
    
for i in range(5):
    print(("Hello x").replace("x",str(i)))
print('................')
for i in range(5):
    print("hello", str(i))

