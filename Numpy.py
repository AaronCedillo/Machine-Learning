#!/usr/bin/env python
# coding: utf-8

# ##### Numpy

# In[1]:


import numpy as np


# <img src="https://quppler.com/wp-content/uploads/2019/03/python-numpy-array.png">

# In[2]:


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(array))


# In[4]:


print(array.shape)


# In[5]:


print(array[0])
print(array[1])
array[2] = 5
print(array[2])


# In[6]:


print("Acceder al valor de la matriz", array[2, 0]) #[fila, columna]


# $ I^{n \times n} =
# \left( \begin{array}{cccc}
# 1 & 2 & 3 \\
# 4 & 5 & 6 \\
# 7 & 8 & 9 \\
# \end{array} \right) $

# In[7]:


#Un array lleno de ceros
zeros = np.zeros([7, 7])
print(zeros)


# In[8]:


#Crear un array lleno de un valor determinado
eights = np.full([4, 4], 8)
print(eights)


# In[9]:


#Llenar la diagonal principal con '1'
eye = np.eye(9 , 9)
print(eye)


# In[10]:


#Matriz con puros '1'
ones = np.ones((3, 7, 3))
print(ones)


# <img src="https://miro.medium.com/max/1440/1*Ikn1J6siiiCSk4ivYUhdgw.png" height="700" width="700">

# In[11]:


## Arreglo de 4x4 de numeros random
random = np.random.random((4, 4))
print(random)


# ##### Array de indices

# In[12]:


array = np.array([[10, 9, 8], [11, 12, 13], [14, 15, 20], [21, 24, 30]])
print(array)
print(array.shape)


# In[13]:


#Creamos dos arrays con numeros enteros que utilizaremos como indices
cols = np.array([0, 1, 2, 0])
rows = np.arange(4)

print("Valores de columnas -> ", cols)
print("Valores de filas -> ", rows)


# In[14]:


for row, col in zip(rows, cols):
    print('(', row, ',', col, ')')


# In[15]:


print("Valores impresos con los arrays que queremos -> ", array[rows, cols])


# In[16]:


print(array)
array[rows, cols] += 100
array


# In[17]:


#Crear un filtro
filter_array = (array > 15)
filter_array


# In[18]:


#Imprimimos los valores que cumplen la condicion del filtro
new_array_filter = array[filter_array]
new_array_filter


# ##### Slice en Array

# In[19]:


new_array = np.array([[2, 3, 5, 6, 7, 0], [23, 45, 6, 7, 90, 56], [12, 14, 67, 80, 24, 28], [34, 45, 89, 35, 78, 86]])
new_array


# In[20]:


slice = new_array[:2, 1:3]
slice


# In[21]:


slice[0, 0] += 100
slice


# In[22]:


#Al sumar 100 a la posicion (0,0) del slice realmente lo sumamos al original, un slice es un apuntador
new_array


# In[23]:


#Para crear un array nuevo a partir del slice que hicimos
array_slice = np.array(slice)
array_slice


# In[24]:


a = np.array([[2, 4, 5, 6], [8, 9, 0, 6]])
b = np.array([[4, 5, 6, 8], [23, 12, 6, 7]])


# In[25]:


#Operaciones entre arrays
#Resta
print(np.subtract(b,a))


# In[26]:


#Suma
print(np.add(b,a))


# In[27]:


#Multiplicacion
print(np.multiply(a,b))


# In[28]:


#Division
print(np.divide(a,b))


# #### Operaciones Estadisticas basicas

# In[29]:


array_random = np.random.rand(2, 5)
array_random


# In[30]:


#Calcula la media(promedio) de un array
print(array_random.mean())


# In[31]:


#Sacar el promedio fila por fila
#eje 0 = columnas
#eje 1 = filas
print(array_random.mean(axis = 1))


# In[32]:


#Sacamos el promedio columna por columna
print(array_random.mean(axis = 0))


# In[33]:


#Creamos un array de 10 elementos aleatorios
array_disorder = np.random.rand(2, 3)
array_disorder


# In[34]:


#Creamos una copia
order = np.array(array_disorder)
order


# In[35]:


#Ordenamos el arreglo
order.sort()
order


# In[36]:


#Buscando elementos unicos
uniq_array = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
print(np.unique(uniq_array))


# In[37]:


#Operaciones en conjunto
s1 = np.array(['silla', 'mesa', 'lampara'])
s2 = np.array(['silla', 'mesa', 'cajon'])


# In[38]:


#Interseccion, sacamos los puntos iguales de los arrays
print(np.intersect1d(s1, s2))


# In[39]:


#Union en 1d, nos quedamos con elementos unicos de los dos arrays
print(np.union1d(s1, s2))


# In[40]:


#Elementos de s1 que no esten en s2
print(np.setdiff1d(s1, s2))


# In[43]:


#Que elementos de s1 estan en s2
print(np.in1d(s1, s2))


# ### Operaciones frecuentes

# In[44]:


ex1 = np.array([[2, 3], [5, 7]])
print("Dimension ---> ", ex1.shape)
print("Sumamos los elementos de un array ---> ", np.sum(ex1))


# In[45]:


print("Sumamos solo una columna ---> ", np.sum(ex1, axis = 0))
print("Sumamos solo una fila ---> ", np.sum(ex1, axis = 1))


# ### Reformateando un array (IMPORTANTE)

# In[46]:


arr = np.arange(20)
print("Arreglo ---> ", arr)
print("Dimension ---> ", arr.shape)


# In[50]:


reshape_arr = arr.reshape(4, 5)
print(reshape_arr)


# In[51]:


#Transpuesta de un array
reshape_arr.T


# In[52]:


#Where ..... MUY UTIL
mat = np.random.rand(4,4)
mat


# In[53]:


#Le pasamos array de condicion, (array --condicion--, nuevo valor donde se cumpla, nuevo valor donde no se cumpla)

np.where(mat > 0.3, 1, 0)


# In[55]:


#Comprobar si algun elemto del array es verdadero, funciona tanto con numeros como con booleanos

array_bools = np.array([0, 0, 5, 0, 0])
array_bools.any()


# In[56]:


#Comprobar si todos los elementos del array son True

array_true = np.array([1, 1, 1, False])
array_true.all()


# ### Uniendo Data Sets

# In[58]:


###Creamos un array de numeros aleatorios con el metodo --->  np.random.randint(-numero menor-, -numero mayor-, -forma-)
X = np.random.randint(low=2, high=20, size=(2, 2))

print(X)

K = np.random.randint(low=2, high=20, size=(2, 2))

print("\n", K)


# In[59]:


## Unimos 'apilando' verticalmente
np.vstack((K, X))


# In[60]:


## Apilamos horizontalmente
np.hstack((K, X))


# In[61]:


#Podemos unir concatenando
np.concatenate([K, X], axis = 0)


# In[62]:


np.concatenate([K, X], axis = 1)


# ### Propagacion 

# In[ ]:




