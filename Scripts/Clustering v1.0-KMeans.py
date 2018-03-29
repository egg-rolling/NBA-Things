
# coding: utf-8

# In[7]:


import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import csv
import sklearn.preprocessing as normalize


# In[8]:


file=pd.read_excel("RPM-March-26.xlsx")


# In[52]:


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


# In[55]:


normal=normalize.normalize(list_t)
#normalize or else data would be heavily biased towards bigger value variable like GP and MPG


# In[59]:


km = KMeans(n_clusters=10)
km.fit(normal)
labels=km.labels_
list_of_labels = labels.tolist()
list_of_mat = mat.tolist()  

for i in range(0,len(labels)):
    list_of_mat[i].append(labels[i])


# In[64]:





# In[68]:


with open("result.csv", "w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(list_of_mat)

