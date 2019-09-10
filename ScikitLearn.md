
### Regresion usando Scikit-Learn
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" height="300" width="300">


```python
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn import preprocessing

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
import numpy as np
```

### Creamos una conexion a la base de datos y leemos la tabla "Player_Attributes"


```python
con = sqlite3.connect('database.sqlite')
# Creamos un dataFrame donde haremos la consulta en SQL
df = pd.read_sql_query("SELECT * FROM Player_Attributes", con)
```


```python
# Mostramos las primeras 15 filas de nuestro dataFrame
df.head(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>player_fifa_api_id</th>
      <th>player_api_id</th>
      <th>date</th>
      <th>overall_rating</th>
      <th>potential</th>
      <th>preferred_foot</th>
      <th>attacking_work_rate</th>
      <th>defensive_work_rate</th>
      <th>crossing</th>
      <th>...</th>
      <th>vision</th>
      <th>penalties</th>
      <th>marking</th>
      <th>standing_tackle</th>
      <th>sliding_tackle</th>
      <th>gk_diving</th>
      <th>gk_handling</th>
      <th>gk_kicking</th>
      <th>gk_positioning</th>
      <th>gk_reflexes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>218353</td>
      <td>505942</td>
      <td>2016-02-18 00:00:00</td>
      <td>67.0</td>
      <td>71.0</td>
      <td>right</td>
      <td>medium</td>
      <td>medium</td>
      <td>49.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>48.0</td>
      <td>65.0</td>
      <td>69.0</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>218353</td>
      <td>505942</td>
      <td>2015-11-19 00:00:00</td>
      <td>67.0</td>
      <td>71.0</td>
      <td>right</td>
      <td>medium</td>
      <td>medium</td>
      <td>49.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>48.0</td>
      <td>65.0</td>
      <td>69.0</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>218353</td>
      <td>505942</td>
      <td>2015-09-21 00:00:00</td>
      <td>62.0</td>
      <td>66.0</td>
      <td>right</td>
      <td>medium</td>
      <td>medium</td>
      <td>49.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>48.0</td>
      <td>65.0</td>
      <td>66.0</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>218353</td>
      <td>505942</td>
      <td>2015-03-20 00:00:00</td>
      <td>61.0</td>
      <td>65.0</td>
      <td>right</td>
      <td>medium</td>
      <td>medium</td>
      <td>48.0</td>
      <td>...</td>
      <td>53.0</td>
      <td>47.0</td>
      <td>62.0</td>
      <td>63.0</td>
      <td>66.0</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>218353</td>
      <td>505942</td>
      <td>2007-02-22 00:00:00</td>
      <td>61.0</td>
      <td>65.0</td>
      <td>right</td>
      <td>medium</td>
      <td>medium</td>
      <td>48.0</td>
      <td>...</td>
      <td>53.0</td>
      <td>47.0</td>
      <td>62.0</td>
      <td>63.0</td>
      <td>66.0</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>189615</td>
      <td>155782</td>
      <td>2016-04-21 00:00:00</td>
      <td>74.0</td>
      <td>76.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>80.0</td>
      <td>...</td>
      <td>66.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>189615</td>
      <td>155782</td>
      <td>2016-04-07 00:00:00</td>
      <td>74.0</td>
      <td>76.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>80.0</td>
      <td>...</td>
      <td>66.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>189615</td>
      <td>155782</td>
      <td>2016-01-07 00:00:00</td>
      <td>73.0</td>
      <td>75.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>79.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>189615</td>
      <td>155782</td>
      <td>2015-12-24 00:00:00</td>
      <td>73.0</td>
      <td>75.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>79.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>189615</td>
      <td>155782</td>
      <td>2015-12-17 00:00:00</td>
      <td>73.0</td>
      <td>75.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>79.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>189615</td>
      <td>155782</td>
      <td>2015-10-16 00:00:00</td>
      <td>73.0</td>
      <td>77.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>79.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>189615</td>
      <td>155782</td>
      <td>2015-09-25 00:00:00</td>
      <td>74.0</td>
      <td>78.0</td>
      <td>left</td>
      <td>high</td>
      <td>medium</td>
      <td>79.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>189615</td>
      <td>155782</td>
      <td>2015-09-21 00:00:00</td>
      <td>73.0</td>
      <td>77.0</td>
      <td>left</td>
      <td>medium</td>
      <td>medium</td>
      <td>79.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>59.0</td>
      <td>76.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>189615</td>
      <td>155782</td>
      <td>2015-01-09 00:00:00</td>
      <td>71.0</td>
      <td>75.0</td>
      <td>left</td>
      <td>medium</td>
      <td>medium</td>
      <td>78.0</td>
      <td>...</td>
      <td>64.0</td>
      <td>58.0</td>
      <td>73.0</td>
      <td>72.0</td>
      <td>72.0</td>
      <td>13.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>189615</td>
      <td>155782</td>
      <td>2014-12-05 00:00:00</td>
      <td>71.0</td>
      <td>77.0</td>
      <td>left</td>
      <td>medium</td>
      <td>medium</td>
      <td>78.0</td>
      <td>...</td>
      <td>64.0</td>
      <td>58.0</td>
      <td>73.0</td>
      <td>72.0</td>
      <td>72.0</td>
      <td>13.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
<p>15 rows × 42 columns</p>
</div>




```python
# Mostramos la forma que tiene nuestro dataSet
df.shape
```




    (183978, 42)




```python
# Mostramos los atributos de cada columna
df.columns
```




    Index(['id', 'player_fifa_api_id', 'player_api_id', 'date', 'overall_rating',
           'potential', 'preferred_foot', 'attacking_work_rate',
           'defensive_work_rate', 'crossing', 'finishing', 'heading_accuracy',
           'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
           'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
           'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
           'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
           'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
           'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
           'gk_reflexes'],
          dtype='object')




```python
df["overall_rating"].head()
```




    0    67.0
    1    67.0
    2    62.0
    3    61.0
    4    61.0
    Name: overall_rating, dtype: float64



### De todas las columnas determinaremos cuales utilizaremos como "features" para alimentar a nuestro modelo
   #### Features: Son las columnas que utilizaremos para el entrenamiento del algoritmo.


```python
# Seleccionamos las caracteristicas importantes que podrian influir en el valor que tiene el jugador, 
 # en este caso seleccionamos unicamente variables numericas, aunque podemos cambiar valores 'string' a numeros
features =[
        'potential', 'crossing', 'finishing', 'heading_accuracy',
        'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
        'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
        'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
        'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
        'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
        'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
        'gk_reflexes']
```

### seleccionamos el target (Variable dependiente)


```python
# Queremos encontrar el valor que tiene el jugador (overall_rating)

target = ['overall_rating']
```

### Limpiemos los datos eliminando filas con variables nan


```python
df = df.dropna()
```

### Separamos las features en X y el target en Y


```python
x = df[features] ## Aqui se aplica el filtro al dataFrame 
y = df[target] ## Esto es lo queremos aprender a obtener
```

### Observemos como luce una fila tipica


```python
x.iloc[3] ## Nos aseguramos de que no existan valores nan (vacios)
```




    potential             65.0
    crossing              48.0
    finishing             43.0
    heading_accuracy      70.0
    short_passing         60.0
    volleys               43.0
    dribbling             50.0
    curve                 44.0
    free_kick_accuracy    38.0
    long_passing          63.0
    ball_control          48.0
    acceleration          60.0
    sprint_speed          64.0
    agility               59.0
    reactions             46.0
    balance               65.0
    shot_power            54.0
    jumping               58.0
    stamina               54.0
    strength              76.0
    long_shots            34.0
    aggression            62.0
    interceptions         40.0
    positioning           44.0
    vision                53.0
    penalties             47.0
    marking               62.0
    standing_tackle       63.0
    sliding_tackle        66.0
    gk_diving              5.0
    gk_handling           10.0
    gk_kicking             9.0
    gk_positioning         7.0
    gk_reflexes            7.0
    Name: 3, dtype: float64




```python
x.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>potential</th>
      <th>crossing</th>
      <th>finishing</th>
      <th>heading_accuracy</th>
      <th>short_passing</th>
      <th>volleys</th>
      <th>dribbling</th>
      <th>curve</th>
      <th>free_kick_accuracy</th>
      <th>long_passing</th>
      <th>...</th>
      <th>vision</th>
      <th>penalties</th>
      <th>marking</th>
      <th>standing_tackle</th>
      <th>sliding_tackle</th>
      <th>gk_diving</th>
      <th>gk_handling</th>
      <th>gk_kicking</th>
      <th>gk_positioning</th>
      <th>gk_reflexes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>71.0</td>
      <td>49.0</td>
      <td>44.0</td>
      <td>71.0</td>
      <td>61.0</td>
      <td>44.0</td>
      <td>51.0</td>
      <td>45.0</td>
      <td>39.0</td>
      <td>64.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>48.0</td>
      <td>65.0</td>
      <td>69.0</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>71.0</td>
      <td>49.0</td>
      <td>44.0</td>
      <td>71.0</td>
      <td>61.0</td>
      <td>44.0</td>
      <td>51.0</td>
      <td>45.0</td>
      <td>39.0</td>
      <td>64.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>48.0</td>
      <td>65.0</td>
      <td>69.0</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>66.0</td>
      <td>49.0</td>
      <td>44.0</td>
      <td>71.0</td>
      <td>61.0</td>
      <td>44.0</td>
      <td>51.0</td>
      <td>45.0</td>
      <td>39.0</td>
      <td>64.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>48.0</td>
      <td>65.0</td>
      <td>66.0</td>
      <td>69.0</td>
      <td>6.0</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>8.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>65.0</td>
      <td>48.0</td>
      <td>43.0</td>
      <td>70.0</td>
      <td>60.0</td>
      <td>43.0</td>
      <td>50.0</td>
      <td>44.0</td>
      <td>38.0</td>
      <td>63.0</td>
      <td>...</td>
      <td>53.0</td>
      <td>47.0</td>
      <td>62.0</td>
      <td>63.0</td>
      <td>66.0</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>65.0</td>
      <td>48.0</td>
      <td>43.0</td>
      <td>70.0</td>
      <td>60.0</td>
      <td>43.0</td>
      <td>50.0</td>
      <td>44.0</td>
      <td>38.0</td>
      <td>63.0</td>
      <td>...</td>
      <td>53.0</td>
      <td>47.0</td>
      <td>62.0</td>
      <td>63.0</td>
      <td>66.0</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>




```python
y.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>overall_rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>67.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>67.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>62.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>61.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>61.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Realizamos una grafica de dispersion
plt.scatter(x['penalties'], y, color='darkgreen', label='Data', alpha=.1)
```




    <matplotlib.collections.PathCollection at 0x7fa95da501d0>




![png](output_20_1.png)


### Separamos los datos en Training y Test Datasets


```python
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=324)
```


```python
scale = preprocessing.StandardScaler()
scale.fit(X_train)
X_train = scale.transform(X_train)
```


```python
X_train.max()
```




    4.9683467491419835



### Creamos una instancia del modelo "LinearRegression" de ScikitLearn


```python
regressor = LinearRegression()
```

### Ajustamos el modelo a los datos de entrenamiento


```python
regressor.fit(X_train, y_train)
```




    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)



### Llevamos a cabo una prediccion utilizando el set de testeo que reservamos para tal fin


```python
X_test = scale.transform(X_test)
y_prediction = regressor.predict(X_test) ### Predecir los resultados con nuestros datos de testeo
y_result = y_prediction - y_test 
y_prediction.shape
```




    (59517, 1)



### Calculamos la Raiz cuadrada del error cuadratico medio


```python
RMSE = sqrt(mean_squared_error(y_true = y_test, y_pred = y_prediction))
regressor.score(X_test, y_test)
```




    -128.6161823155533




```python
print(RMSE)
```

    80.16386405994886



```python
regressor.coef_
```




    array([[ 2.48175418,  0.37435166,  0.2155902 ,  1.14537904,  0.72579619,
             0.08835762, -0.2396529 ,  0.20341906,  0.23070925,  0.08573083,
             2.03147644,  0.08063536,  0.11593773, -0.09744622,  1.92780373,
             0.10753058,  0.27833167,  0.16277628, -0.08089224,  0.73874625,
            -0.25048481,  0.33897633,  0.22293067, -0.18511046, -0.01892236,
             0.21517621,  0.70526674,  0.07880386, -0.61339243,  2.72376613,
             0.51832172, -0.70907673,  0.91420565,  0.43578429]])




```python

```
