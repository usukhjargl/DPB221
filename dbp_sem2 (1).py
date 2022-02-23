#!/usr/bin/env python
# coding: utf-8

# In[13]:


#1. Өгөгдсөн утга нь палиндром эсэхийг шалгах функц бич.
def palindrome(n):
    x=n
    r=0
    while(n>0):
        dig=n%10
        r=r*10+dig
        n=n//10
    if(x==r):
        print("Palindrome too")
    else:
        print("Palindrome bish")
n=int(input())
palindrome(n)


# In[14]:


#2. Өгөгдсөн жагсаалтаас том болон жижиг үсгүүдийг тоолох функц бич.
def funct(x):
    up=0
    low=0
    for i in range(len(x)):
        if(x[i]>='a' and x[i]<='z'):
            low+=1
        elif(x[i]>='A' and x[i]<='Z'):
            up+=1
    return [up,low]
x=input()
print(funct(x))


# In[23]:


#3. Жагсаалтын утгуудын үржвэрийг олох функц бич.
def multiple(List) :
    y = 1
    for x in List:
         y = y * x
    return y
list1 = [9, 3, 5, 7]
print(multiple(list1))


# In[35]:


#4. Өгөгдсөн тооны бактерал олох функц бич.
def func(x):
    s = 1
    for i in range(2, x + 1):
        s *= i
    return s
num=int(input())
print(func(num))


# In[37]:


#5. Өгөгдсөн жагсаалтыг урвуу болгох функц бич.
def rev(n):
    list2.reverse()
    return n
list2 = [18, 21, 32, 13, 64, 85]
print(rev(list2))


# In[40]:


#6. Жагсаалтын утгуудын нийлбэрийг олох функц бич.
def sumlist(n):
    s=0
    for i in n:
        s=s+i
    return s
list3 = [18, 21, 32, 13, 64, 85]
print(sumlist(list3))


# In[44]:


#7. Жагсаалтын давхардсан утгуудыг арилгах функц бич.
def makeset(n):
    set1=set(n)
    listx=list(set1)
    return listx
list3 = [21, 21, 32, 13, 13, 85]
print(makeset(list3))


# In[46]:


#8. 3 тооны хамгийн ихийг олдог функц бич.
def maxim(a, b, c):
    list = [a, b, c]
    return max(list)
a = 137
b = 134
c = 132
print(maxim(a, b, c))

