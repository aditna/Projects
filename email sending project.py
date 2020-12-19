#!/usr/bin/env python
# coding: utf-8

# # project 2

# In[1]:


get_ipython().system('pip install emails')


# In[2]:


import emails


# In[27]:


html_text='''<p><span style='font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; background-color: rgb(247, 218, 100);'>Hey Rowdy,</span></p>
<p><span style="font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;"><br></span></p>
<p><span style="font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;">how are you,this is &nbsp;Aditi from letsupgrade,</span></p>
<p><span style="font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;"><br></span></p>
<p><span style="font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;">chief Rowdy at LU!</span></p>
<p><span style="font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;"><br></span></p>
<p><span style="font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;">hope you liked this project</span></p>
<p><br></p>
<p><br></p>
message = emails.html(html = html_text,
subject="Your EMAIL FROM PYTHON SCRIPT",
mail_from=('Rowdy LetsUpgrade', 'aditi@xyz.com'))'''


# In[28]:


mail_via_python = message.send(to='rikoko4981@95ta.com',
    smtp={'host': 'smtp.gmail.com','timeout': 5,'port':587,
    'user':'aditinayak99@gmail.com',
    'password':'*Aditinayak99',
    'tls':True})


# In[32]:


mail_via_python.status_code


# In[36]:


def sendMail(email):
    mail_via_python = message.send(to=email,
    smtp={'host': 'smtp.gmail.com','timeout': 5,'port':587,
    'user':'aditinayak99@gmail.com',
    'password':'*Aditinayak99',
    'tls':True})

    return mail_via_python.status_code


# In[38]:


sendMail("aditinayak2000@gmail.com")


# In[ ]:




