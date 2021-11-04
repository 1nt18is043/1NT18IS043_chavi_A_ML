#!/usr/bin/env python
# coding: utf-8

# In[22]:


import math
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
    
    maximum=max(arr)
    minimum=min(arr)
    new_array=[]
    for value in arr:
        new_value= (value-minimum)/(maximum-minimum)
        new_array.append(new_value)
    print("Normalized array:",new_array)
    print("Mean after normalization:",st.mean(new_array))
    
    new_list=[]
    for value in arr:
        new_value=(value-mean)/std
        new_list.append(new_value)
        
    print("Standardized array:",new_list)
    print("Normalized array:",new_array)
    print("Mean after normalization:",st.mean(new_list))
    print("Std after normalization:",st.stdev(new_list))
    
        mean=sum/n
    print("mean:",mean)
calc([2,3,1,4,5,6,3,3])    


# In[9]:


import statistics as st
def mean(arr):
    n = len(arr)
    sum=0
    for i in arr:
        sum=sum+i
    mean=sum/n
    print("mean:",mean)new_list=[]
    for value in l:
        new_value=(value-mean)/std
        new_list.append(new_value)
    
    print("mean:",st.mean(arr))
    
mean([1,2,3,4,5])


# In[16]:


import statistics as st
def median(arr):
    n = len(arr)
    arr.sort()
    if n%2!=0:
        index=n//2new_list=[]
    for value in l:
        new_value=(value-mean)/std
        new_list.append(new_value)
    
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
        sum+=pow(i-mean,2)print("mean:",st.mean(arr))
    variance=sum/(n-1)
    
    print("variance:",variance)
    print("variance:",st.variance(arr))
    
    std=math.sqrt(variance)
    print("Standard Deviation:",std)
    print("Standard Deviation:",st.stdev(arr))
        
            
var([1,2,2,1,2])


# In[7]:


import statistics as st
def normalization(l):
    maximum=max(l)
    minimum=min(l)
    new_array=[]
    for value in l:
        new_value= (value-minimum)/(maximum-minimum)
        new_array.append(new_value)
    print("mean:",st.mean(new_array))
    new_list=[]
    for value in l:
        new_value=(value-mean)/std
        new_list.append(new_value)
    
normalization([2,1900,6,450,678,90])


# In[23]:


from sklearn.preprocessing import Normalizer
def normalize():
    x=[[4,1,2,2],[1,3,9,3],[5,7,5,1]]
    transformer=Normalizer().fit(x)
    print(transformer.transform(x))

normalize()


# In[17]:


from sklearn.preprocessing import StandardScaler
data = [[0, 0], [0, 0], [1, 1], [1, 1]]
scaler = StandardScaler()
print(scaler.fit(data))
print(scaler.mean_)
print(scaler.transform(data))


# In[18]:


import math
def standardization(l):
    n = len(l)
    sum=0
    for i in l:new_list=[]
    for value in l:
        new_value=(value-mean)/std
        new_list.append(new_value)
    
        sum=sum+i
    mean=sum/n
    sum=0
    for i in l:
        sum+=pow(i-mean,2)
    variance=sum/(n-1)
    std=math.sqrt(variance)
    new_list=[]
    for value in l:
        new_value=(value-mean)/std
        new_list.append(new_value)
    
    sum=0
    for i in new_list:
         sum=sum+i
    mean=sum/n
    print("mean:",mean)
    print("mean:",st.mean(new_list))
    sum=0
    for i in new_list:
        sum+=pow(i-mean,2)
    variance=sum/(n-1)
    std=math.sqrt(variance)
    print("std:",std)
    print("std:",st.stdev(new_list))
    
standardization([2,3,1,4,5,6,3,3])

