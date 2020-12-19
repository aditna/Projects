#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cryptography project


# step 1- which library to use to convert normal text to chiper text 

# step 2-Take input from the user and convert it to chiper text

# step 3-display back the chiper text to user

# step 4-load the key and if the key is the same, based upon the input provided,convert it to normal text

# In[2]:


get_ipython().system('pip install cryptography')


# In[3]:


from cryptography.fernet import Fernet


# In[4]:


def genratePassKey():
    key = Fernet.generate_key()
    print(key)
    print(type(key))
    abc = open("PasswordKey.key",'wb')
    abc.write(key)
    abc.close()


# In[5]:


def getMyKey():
    abc = open("PasswordKey.key",'rb')
    key = abc.read()
    abc.close()
    return key


# In[9]:


genratePassKey()


# In[10]:


getMyKey()


# In[11]:


def getContentFromUser():
    return input("Enter the Content you want to Encrypt in your python Script")


# In[12]:


getContentFromUser()


# In[13]:


def encryptMessage(message_normal):
    key = getMyKey()
    k = Fernet(key)
    encrypted_Message = k.encrypt(message_normal)
    return encrypted_Message


# In[17]:


encryptMessage(b'hai')


# In[18]:


def decryptMessage(message_secret):
    key = getMyKey()
    k = Fernet(key)
    decrypted_Message = k.decrypt(message_secret)
    return decrypted_Message


# In[23]:


decryptMessage(b'gAAAAABf3icKUSFmpP_pU6TalIvFdvXQTEJAzJVjmhWoagE53qo3miKSUmUzSpSpk5Mzu97ABMvpqxuPzqax0oQqSR1kEyfHeQ==')


# In[ ]:




