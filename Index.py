#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 5 or 3
def summa(N):
    sum = 0
    for i in range(N + 1):
        if ((i % 5) == 0) or ((i % 3) == 0):
            sum = sum + i
    return (sum)


# In[13]:


summa(10)


# # Welcome to Jupyter!

# In[14]:


summa(1000)


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[15]:


# kvadratnoe yravnenie
def kvad(b, c):
    a1 = (-b + (b ** 2 - 4 * c) ** 0.5) / 2
    a2 = (-b - (b ** 2 - 4 * c) ** 0.5) / 2
    return a1, a2


# In[16]:


b = -2
c = 1
print(kvad(b, c))


# In[17]:


b = 100
c = 3
print(kvad(b, c))


# In[19]:


b = 5
c = 40
print(kvad(b, c))


# In[20]:


b = 10^20
c = 40
print(kvad(b, c))

