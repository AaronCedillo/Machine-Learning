
### Introduccion a la Regresion Lineal (Simple)

<img src="https://i0.wp.com/live.staticflickr.com/65535/48051791826_8d9e4844f1_c.jpg?resize=800%2C467&ssl=1" height="600" width="600">


```python
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
plt.style.use("seaborn-dark")
```


```python
# Supondremos que 'x' es el dinero invertido y que 'y' son las ganancias

x = np.array([0, 6.5, 13.2, 18.1, 24.9, 28.2, 36.1])
y = np.array([5, 10,    17,   20,   25,   30,   35])
```


```python
plt.figure(figsize=(7,7))
plt.scatter(x, y, s=120)  # (x, y) Puntos a graficar ||| 's' = Tamaño de los puntos graficados
plt.ylim(bottom=0) 
plt.title("Valores")
plt.xlabel("Dinero Invertido")
plt.ylabel("Dinero Ganado")
plt.grid()
plt.show()
```


![png](output_3_0.png)



```python
x2 = np.arange(0, 40)
y2 = 0.8 * x2 + 5 # Son valores random, lo hicimos para demostrar cómo funciona la regresion
print("Valores de inversion: ", x2, "\n")
print("Valores de ganancia ", y2)
```

    Valores de inversion:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
     24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39] 
    
    Valores de ganancia  [ 5.   5.8  6.6  7.4  8.2  9.   9.8 10.6 11.4 12.2 13.  13.8 14.6 15.4
     16.2 17.  17.8 18.6 19.4 20.2 21.  21.8 22.6 23.4 24.2 25.  25.8 26.6
     27.4 28.2 29.  29.8 30.6 31.4 32.2 33.  33.8 34.6 35.4 36.2]



```python
plt.figure(figsize=(7,7))
plt.plot(x2, y2, color="red", label = "Nuestra solucion")
plt.scatter(x, y, s=120)
plt.ylim(bottom=0) 
plt.title("Valores")
plt.xlabel("Valores X")
plt.ylabel("Valores Y")
plt.grid()
plt.show()
```


![png](output_5_0.png)



```python
# Regresion Lineal Polinomial 
    
x_polinomial = np.array([0, 6.5, 13.2, 18.1, 24.9, 28.2, 36.1])
x2_polinomial = np.array([22, 23,  24,   21,   10,   17,    8])

y_polinomial = np.array([5, 10,    17,   20,   25,   30,   35])
```

#### Error Cuadratico Medio

<img src="https://miro.medium.com/max/730/0*MdRLxfy4GbQlv97V." height="500" width="500">


<img src="https://iartificial.net/wp-content/uploads/2018/12/error-regresion-lineal2.png" height="500" width="500">


```python

```
