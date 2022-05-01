

import csv
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('output2.csv')
names = list(data.iloc[:, 0])
count= list(data.iloc[:, 1])
plt.scatter(names, count, color ='maroon')
#plt.xlabel("The test files")
plt.ylabel("Number of times assert occured")
plt.title("Test files with the occurance of assert for test files")
plt.gca().axes.get_xaxis().set_visible(False)


# In[3]:


import csv
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('output3.csv')

file_names = list(data.iloc[:, 1])
count= list(data.iloc[:, 2])
plt.scatter(file_names, count, color ='black')
plt.xlabel("The test files")
plt.ylabel("Number of times debug occured")
plt.title("Test files with the occurance of debug for production files")
plt.gca().axes.get_xaxis().set_visible(False)


# In[14]:


import csv
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('output_32.csv')
#print(data)
file_names = list(data.iloc[:, 1])
count= list(data.iloc[:, 2])
plt.scatter(file_names, count, color ='black')
plt.xlabel("The test files")
plt.ylabel("Number of times assert occured")
plt.title("Test files with the occurance of assert for production files")
plt.gca().axes.get_xaxis().set_visible(False)


# In[17]:


import csv
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('output_driller.csv')
file_names = list(data.iloc[:, 0])
# print(file_names)
count= list(data.iloc[:, 2])
#print(count)
plt.scatter(file_names, count, color ='black')
plt.xlabel("The test files")
plt.ylabel("Operations")
plt.title("The operations performed to the repository")
plt.gca().axes.get_xaxis().set_visible(False)


# In[ ]:




