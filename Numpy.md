
##### Numpy


```python
import numpy as np
```


```python
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(array))
```

    <class 'numpy.ndarray'>



```python
print(array.shape)
```

    (3, 3)



```python
print(array[0])
print(array[1])
array[2] = 5
print(array[2])
```

    [1 2 3]
    [4 5 6]
    [5 5 5]



```python
print("Acceder al valor de la matriz", array[2, 0]) #[fila, columna]
```

    Acceder al valor de la matriz 5


$ I^{n \times n} =
\left( \begin{array}{cccc}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{array} \right) $


```python
#Un array lleno de ceros
zeros = np.zeros([7, 7])
print(zeros)
```

    [[0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0.]]



```python
#Crear un array lleno de un valor determinado
eights = np.full([4, 4], 8)
print(eights)
```

    [[8 8 8 8]
     [8 8 8 8]
     [8 8 8 8]
     [8 8 8 8]]



```python
#Llenar la diagonal principal con '1'
eye = np.eye(9 , 9)
print(eye)
```

    [[1. 0. 0. 0. 0. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0. 0. 0. 0. 0.]
     [0. 0. 1. 0. 0. 0. 0. 0. 0.]
     [0. 0. 0. 1. 0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 1. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0. 1. 0. 0. 0.]
     [0. 0. 0. 0. 0. 0. 1. 0. 0.]
     [0. 0. 0. 0. 0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 0. 0. 0. 0. 1.]]



```python
#Matriz con puros '1'
ones = np.ones((3, 7, 3))
print(ones)
```

    [[[1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]]
    
     [[1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]]
    
     [[1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]
      [1. 1. 1.]]]


<img src="https://miro.medium.com/max/1440/1*Ikn1J6siiiCSk4ivYUhdgw.png" height="700" width="700">


```python
## Arreglo de 4x4 de numeros random
random = np.random.random((4, 4))
print(random)
```

    [[0.83984683 0.60079138 0.33774298 0.50453708]
     [0.81702833 0.38622571 0.33197704 0.50978136]
     [0.81637723 0.14071054 0.95931806 0.24018253]
     [0.12393863 0.6971283  0.87837884 0.31220277]]


##### Array de indices


```python
array = np.array([[10, 9, 8], [11, 12, 13], [14, 15, 20], [21, 24, 30]])
print(array)
print(array.shape)
```

    [[10  9  8]
     [11 12 13]
     [14 15 20]
     [21 24 30]]
    (4, 3)



```python
#Creamos dos arrays con numeros enteros que utilizaremos como indices
cols = np.array([0, 1, 2, 0])
rows = np.arange(4)

print("Valores de columnas -> ", cols)
print("Valores de filas -> ", rows)
```

    Valores de columnas ->  [0 1 2 0]
    Valores de filas ->  [0 1 2 3]



```python
for row, col in zip(rows, cols):
    print('(', row, ',', col, ')')
```

    ( 0 , 0 )
    ( 1 , 1 )
    ( 2 , 2 )
    ( 3 , 0 )



```python
print("Valores impresos con los arrays que queremos -> ", array[rows, cols])
```

    Valores impresos con los arrays que queremos ->  [10 12 20 21]



```python
print(array)
array[rows, cols] += 100
array
```

    [[110   9   8]
     [ 11 112  13]
     [ 14  15 120]
     [121  24  30]]





    array([[210,   9,   8],
           [ 11, 212,  13],
           [ 14,  15, 220],
           [221,  24,  30]])




```python
#Crear un filtro
filter_array = (array > 15)
filter_array
```




    array([[ True, False, False],
           [False,  True, False],
           [False, False,  True],
           [ True,  True,  True]])




```python
#Imprimimos los valores que cumplen la condicion del filtro
new_array_filter = array[filter_array]
new_array_filter
```




    array([210, 212, 220, 221,  24,  30])



##### Slice en Array


```python
new_array = np.array([[2, 3, 5, 6, 7, 0], [23, 45, 6, 7, 90, 56], [12, 14, 67, 80, 24, 28], [34, 45, 89, 35, 78, 86]])
new_array
```




    array([[ 2,  3,  5,  6,  7,  0],
           [23, 45,  6,  7, 90, 56],
           [12, 14, 67, 80, 24, 28],
           [34, 45, 89, 35, 78, 86]])




```python
slice = new_array[:2, 1:3]
slice
```




    array([[ 3,  5],
           [45,  6]])




```python
slice[0, 0] += 100
slice
```




    array([[103,   5],
           [ 45,   6]])




```python
#Al sumar 100 a la posicion (0,0) del slice realmente lo sumamos al original, un slice es un apuntador
new_array
```




    array([[  2, 103,   5,   6,   7,   0],
           [ 23,  45,   6,   7,  90,  56],
           [ 12,  14,  67,  80,  24,  28],
           [ 34,  45,  89,  35,  78,  86]])




```python
#Para crear un array nuevo a partir del slice que hicimos
array_slice = np.array(slice)
array_slice
```




    array([[103,   5],
           [ 45,   6]])




```python
a = np.array([[2, 4, 5, 6], [8, 9, 0, 6]])
b = np.array([[4, 5, 6, 8], [23, 12, 6, 7]])
```


```python
#Operaciones entre arrays
#Resta
print(np.subtract(b,a))
```

    [[ 2  1  1  2]
     [15  3  6  1]]



```python
#Suma
print(np.add(b,a))
```

    [[ 6  9 11 14]
     [31 21  6 13]]



```python
#Multiplicacion
print(np.multiply(a,b))
```

    [[  8  20  30  48]
     [184 108   0  42]]



```python
#Division
print(np.divide(a,b))
```

    [[0.5        0.8        0.83333333 0.75      ]
     [0.34782609 0.75       0.         0.85714286]]


#### Operaciones Estadisticas basicas


```python
array_random = np.random.rand(2, 5)
array_random
```




    array([[0.62428642, 0.54693195, 0.23139863, 0.49008528, 0.75376302],
           [0.01545363, 0.34892399, 0.68157835, 0.49513624, 0.247751  ]])




```python
#Calcula la media(promedio) de un array
print(array_random.mean())
```

    0.4435308508896002



```python
#Sacar el promedio fila por fila
#eje 0 = columnas
#eje 1 = filas
print(array_random.mean(axis = 1))
```

    [0.52929306 0.35776864]



```python
#Sacamos el promedio columna por columna
print(array_random.mean(axis = 0))
```

    [0.31987003 0.44792797 0.45648849 0.49261076 0.50075701]



```python
#Creamos un array de 10 elementos aleatorios
array_disorder = np.random.rand(2, 3)
array_disorder
```




    array([[0.37757027, 0.05990777, 0.9476478 ],
           [0.67778561, 0.28369956, 0.27487855]])




```python
#Creamos una copia
order = np.array(array_disorder)
order
```




    array([[0.37757027, 0.05990777, 0.9476478 ],
           [0.67778561, 0.28369956, 0.27487855]])




```python
#Ordenamos el arreglo
order.sort()
order
```




    array([[0.05990777, 0.37757027, 0.9476478 ],
           [0.27487855, 0.28369956, 0.67778561]])




```python
#Buscando elementos unicos
uniq_array = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
print(np.unique(uniq_array))
```

    [1 2 3]



```python
#Operaciones en conjunto
s1 = np.array(['silla', 'mesa', 'lampara'])
s2 = np.array(['silla', 'mesa', 'cajon'])
```


```python
#Interseccion, sacamos los puntos iguales de los arrays
print(np.intersect1d(s1, s2))
```

    ['mesa' 'silla']



```python
#Union en 1d, nos quedamos con elementos unicos de los dos arrays
print(np.union1d(s1, s2))
```

    ['cajon' 'lampara' 'mesa' 'silla']



```python
#Elementos de s1 que no esten en s2
print(np.setdiff1d(s1, s2))
```

    ['lampara']



```python
#Que elementos de s1 estan en s2
print(np.in1d(s1, s2))
```

    [ True  True False]



```python

```
