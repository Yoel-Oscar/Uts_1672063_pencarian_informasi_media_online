#!/usr/bin/env python
# coding: utf-8

# In[175]:


import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('question_philoit.csv')
print('Shape of data',df.shape)
df.head()
df


# In[191]:


row_start = df.index[1706]
row_end = df.index[4927]
pd.to_datetime(df['created_at'])
df.loc[row_start:row_end, 'created_at']



# In[184]:


cols = ['userId', 'id','content', 'created_at']
df_list = df[cols]


# In[185]:


df_list.head(4930)


# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv('hasil_sorting_data.csv')
print('Shape of data',df.shape)
df.head()
df


# In[ ]:




