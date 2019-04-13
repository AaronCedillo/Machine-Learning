#!/usr/bin/env python
# coding: utf-8

# ---
# 
# # Ejercicios NumPy
# 
# ## Machine Learning para la industria 2019
# 
# ---

# #### Importa NumPy

# In[1]:


import numpy as np


# #### Crea un arreglo  de 5 ceros

# In[5]:


#Escribe tu respuesta aquí
a = np.zeros(5)
a


# #### Crea un arreglo de 5 unos

# In[4]:


#Escribe tu respuesta aquí


# In[6]:


a = np.ones(5)
a


# #### Crea un arreglo de 5 ochos

# In[8]:


#Escribe tu respuesta aquí


# In[29]:


x = np.arange(5)
np.full_like(x, 8)


# #### Crea un arreglo de enteros del 50 al 99

# In[10]:


#Escribe tu respuesta aquí


# In[32]:


a = np.arange(50, 100, 1)
a


# #### Reajusta el arreglo anterior para que tenga 5 filas

# In[33]:


#Escribe tu respuesta aquí


# In[34]:


a.reshape(5, 10)


# #### Crea un arreglo de números pares de 50 a 100

# In[12]:


#Escribe tu respuesta aquí


# In[39]:


np.arange(50, 102, 2)


# #### Crea una matriz de 5x5 con valores del 0 al 24

# In[24]:


#Escribe tu respuesta aquí


# In[63]:


a = np.arange(25).reshape(5, 5)
a


# #### Crea una matriz identidad de 5x5

# In[28]:


#Escribe tu respuesta aquí


# In[47]:


np.eye(5)


# #### Genera un número aleatorio con NumPy en el intervalo [0,1)

# In[49]:


np.random.rand(1)


# #### Genera un arreglo de 10 números aleatorios tomados de una distribución normal estándar

# In[30]:


#Escribe tu respuesta aquí


# In[50]:


np.random.rand(10)


# #### Crea la siguiente matriz:

# In[36]:


#Escribe tu respuesta aquí


# In[62]:


a = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
a


# #### Crea un arreglo de 10 puntos en el intervalo [1,5] separados a igual distancia entre ellos

# In[41]:


#Escribe tu respuesta aquí


# In[58]:


np.linspace(1, 5, 10)


# ## Selección e indexación en NumPy

# Dada la siguiente matriz, escribe el código necesario para obtener las selecciones que se te piden

# In[80]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[81]:


#Escribe tu respuesta aquí


# In[86]:


mat[2:, 2:]


# In[45]:


#Escribe tu respuesta aquí


# In[89]:


mat[3, 2]


# In[54]:


#Escribe tu respuesta aquí ¡Ojo!


# In[109]:


mat[0:3, 2].reshape(3, 1)


# In[59]:


#Escribe tu respuesta aquí ¡Ojo!


# In[100]:


mat[4]


# In[8]:


#Escribe tu respuesta aquí


# In[112]:


mat[2:, 0:]


# ### Práctica con funciones matemáticas

# #### Suma todos los elementos de la matriz

# In[64]:


#Escribe tu respuesta aquí


# In[117]:


x = np.sum(mat)
x


# #### Obtén el promedio de los valores de la matriz

# In[69]:


#Escribe tu respuesta aquí


# In[129]:


# z = np.prod(mat.shape)
    # x/z
np.mean(mat)    


# #### Obtén la suma de las columnas de la matriz

# In[71]:


#Escribe tu respuesta aquí


# In[177]:


lista = []
for cnt in range(0, 5):    
    x = mat[:, cnt].sum() #mat[:, cnt].sum()
    lista.append(x)
lista


# #### Obtén la suma de las filas de la matriz

# In[178]:


#Escribe tu respuesta aquí


# In[179]:


lista = []
for cnt in range(0, 5):
    x = mat[cnt, :].sum()
    lista.append(x)
lista    


# In[ ]:




