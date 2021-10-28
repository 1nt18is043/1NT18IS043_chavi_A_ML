#!/usr/bin/env python
# coding: utf-8

# In[48]:


def calc(arr):
    n = len(arr)
    sum=0
    for i in arr:
        sum=sum+i
    mean=sum/n
    print("mean:",mean)
    
    arr.sort()
    if n%2!=0:
        index=n//2
        median=arr[index]
    else:
        index=n//2
        median=float((arr[index-1]+arr[index])/2)
    print("median:",median)
    
    mode=0
    freq=[0]*max(arr)
    for i in arr:
        freq[i-1]+=1
    mode=freq.index(max(freq))+1
    print("mode:",mode)
    
    sum=0
    for i in arr:
        sum+=pow(i-mean,2)
    variance=sum/(n-1)
    print("variance:",variance)
    
    std=math.sqrt(variance)
    print("Standard Deviation:",std)
    
calc([1,2,2,1,2])    


# In[9]:


import statistics as st
def mean(arr):
    n = len(arr)
    sum=0
    for i in arr:
        sum=sum+i
    mean=sum/n
    print("mean:",mean)
    print("mean:",st.mean(arr))
    
mean([1,2,3,4,5])


# In[16]:


import statistics as st
def median(arr):
    n = len(arr)
    arr.sort()
    if n%2!=0:
        index=n//2
        median=arr[index]
    else:
        index=n//2
        median=float((arr[index-1]+arr[index])/2)
    print("median:",median)
    print("median:",st.median(arr))
    
median([1,2,3,4,5])


# In[31]:


import statistics as st
def mode(arr):
    n = len(arr)
    mode=0
    freq=[0]*max(arr)
    for i in arr:
        freq[i-1]+=1
    mode=freq.index(max(freq))+1
    print("mode:",mode)
    print("mode:",st.mode(arr))
        
            
mode([1,2,2,1,2])


# In[46]:


import statistics as st
import math
def var(arr):
    n = len(arr)
    sum=0
    mean=st.mean(arr)
    for i in arr:
        sum+=pow(i-mean,2)
    variance=sum/(n-1)
    
    print("variance:",variance)
    print("variance:",st.variance(arr))
    
    std=math.sqrt(variance)
    print("Standard Deviation:",std)
    print("Standard Deviation:",st.stdev(arr))
        
            
var([1,2,2,1,2])

