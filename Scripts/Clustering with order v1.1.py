
# coding: utf-8

# In[69]:


import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import csv
import sklearn.preprocessing as normalize


# In[71]:


file=pd.read_excel("RPM-with-limit.xlsx")


# In[72]:


mat = file.as_matrix()
entry_num = len(mat)
col_num = len(mat[0])
print (entry_num,col_num)
list_t = []
for entry in mat:
    counter = 0
    sub_list = []
    for item in entry:
        if counter < 4:
            counter+= 1
        else: 
            sub_list.append(item)
    list_t.append(sub_list)


# In[73]:


normal=normalize.normalize(list_t)
#normalize or else data would be heavily biased towards bigger value variable like GP and MPG


# In[74]:


km = KMeans(n_clusters=10)
km.fit(normal)
labels=km.labels_
list_of_labels = labels.tolist()
list_of_mat = mat.tolist()  

for i in range(0,len(labels)):
    list_of_mat[i].append(labels[i])


# In[64]:





# In[76]:


with open("result-with-restriction.csv", "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(list_of_mat)


# In[118]:


print (list_of_mat[0])
sum_t = []
for i in range(0,10):
    sum_t.append([0,0,0,0,0,0,0,i])


# In[119]:


for elem in list_of_mat:
    sum_t[elem[-1]][0] += 1 #count how many people
    #number of people,GP,MPG,ORPM,DRPM,RPM,WINS,Group
    #               0,1 ,2  ,   3,   4,  5,   6,    7

    sum_t[elem[-1]][1] += elem[4]
    sum_t[elem[-1]][2] += elem[5]
    sum_t[elem[-1]][3] += elem[6]
    sum_t[elem[-1]][4] += elem[7]
    sum_t[elem[-1]][5] += elem[8]
    sum_t[elem[-1]][6] += elem[9]


# In[123]:


print (sum_t[0])


# In[121]:


for elem in sum_t:
    for i in range(1,7):
        elem[i] = elem[i]/elem[0]


# In[127]:


new_rank = sorted(sum_t, key=lambda elem: elem[5])


# In[131]:


print(new_rank)
dict_t = {}
i = 1
for elem in new_rank:
    dict_t[elem[7]]=i
    i = i+1


# In[134]:


for elem in list_of_mat:
    elem.append(dict_t[elem[-1]])


# In[135]:


with open("ordered-result-with-restriction.csv", "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(list_of_mat)

