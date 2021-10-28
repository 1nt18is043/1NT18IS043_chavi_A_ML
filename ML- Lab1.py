#!/usr/bin/env python
# coding: utf-8

# In[20]:


print("Hello World!")

a=10
print(a)

a="Chavi Singh"
print(a)

a=10
if a>10:
    print("Greater")
else:
    print("lesser")

a=5
b=5
print(a+b)

a=10
b=10.00
print(a+b)

a=5
b=6
print("a:",a,"b:",b)
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)
print("Hello World!")

a=10
print(a)

a="Chavi Singh"
print(a)

a=10
if a>10:
    print("Greater")
else:
    print("lesser")

a=5
b=5
print(a+b)

a=10
b=10.00
print(a+b)

a=5
b=6
print("a:",a,"b:",b)
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)


# In[19]:


a=5
b=6
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
a=int(input("Enter a number:"))
print(a)
type(a)

for i in range(1,10):
    print(i)


# In[17]:


a=int(input("enter number1:"))
b=int(input("enter number2:"))
c=input("enter operator:")
if c=='+':
    print(a+b)
elif c=='-':
    if(a>b):
        print(a-b)
    else:
        print(b-a)
elif c=='*':
    print(a*b)
elif c=='/':
    if(b==0):
        print("Not Valid")
    else:
        print(int(a/b))
elif c=="%":
    print(int(a%b))
else:
    print("Invalid")


# In[16]:


def find(word):
    words=["Pen","Pencil","Eraser","Book"]
    for l in words:
        if(l.lower()==word.lower()):
            print("Found")
            return
    print("Not Found")
    
find("pencil")


# In[15]:


str1="I am"
str2="Chavi Singh"
print(str1+str2)

str1="abc"
str2="abc"
if str1>str2:
    print(str1,"is greater than",str2)
elif str1<str2:
     print(str1,"is less than",str2)
else:
    print("Both are equal")
   

str1="Chavi Singh"
print(str1[::-1])


# In[14]:


def reverse(word):
    rev=""
    for letter in word:
        rev=letter+rev
    return rev

reversed=reverse("Chavi Singh")
print(reversed)


# In[13]:


a="Josh"
b="josh"
print(bool(a<b))

a=[1,2,3,4,5,6,7,8,9]
x=slice(0,10,2)
print(a[x])


# In[12]:


list=["apple","Orange","Banana","Jackfruit"]
print(list[0:4])

a=[1,2,3,4,5,6,7,8,9]
list=["apple","Orange","Banana","Jackfruit"]
print(a+list)


# In[11]:


def copyingstring(word):
    str=word
    print("Copied string is",str)
copyingstring("Chavi")


# In[8]:


a=[1,2,3,4,5,6,7,8,9]
a.append(10)
a.remove(1)
a.pop()
print(a)


# In[7]:


dict={'abc':1,'efg':2,'hij':3}
print(dict.get("abc"))


# In[6]:


tuple=(1,2,3,4,5)
print(tuple)


# In[5]:


list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)


# In[4]:



dict={'abc':1,'efg':2,'hij':3}
dict['xyz']=4
print(dict)


# In[3]:


# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

#Tuples-Immutable object(No insertion and deletion works)
#list,dictionary-mutable(both insertion and deletion works)

