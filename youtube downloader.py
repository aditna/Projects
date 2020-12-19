#!/usr/bin/env python
# coding: utf-8

# # project 3

# In[11]:


get_ipython().system('pip install pytube')


# In[12]:


from pytube import YouTube


# In[13]:


YouTube('https://youtu.be/ZiioPiJI50c').streams.first().download()


# In[ ]:




