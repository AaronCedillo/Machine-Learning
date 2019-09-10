
### Pandas

<img src="https://pandas.pydata.org/_static/pandas_logo.png">


```python
import pandas as pd
```


```python
# Pandas posee dos estructuras de datos basicas
#... Series
#... DataFrames
```

### Series


```python
# Creamos una serie donde pasamos un arreglo con su indice

ser = pd.Series( data = [100, 'Ninguno', 200, 'Hola'], index = ['Juan', 500, 'Nadie', 200])
ser
```




    Juan         100
    500      Ninguno
    Nadie        200
    200         Hola
    dtype: object




```python
# Obtemos los indices
ser.index
```




    Index(['Juan', 500, 'Nadie', 200], dtype='object')




```python
# Acceder al valor de un indice
ser['Juan']
```




    100




```python
# Con loc
ser.loc['Juan']
```




    100




```python
# A loc le puedo pasar un array y acceder a distintos valores al mismo tiempo
ser.loc[['Juan', 'Nadie']]
```




    Juan     100
    Nadie    200
    dtype: object




```python
# Podemos pasar un array de las posiciones de los valores deseados
ser[[0, 1, 2]]
```




    Juan         100
    500      Ninguno
    Nadie        200
    dtype: object




```python
ser.iloc[[0, 1, 2]]
```




    Juan         100
    500      Ninguno
    Nadie        200
    dtype: object




```python
# Podemos consultar si existe un indice en la serie
"Pablo" in ser
```




    False



### DataFrames
###### Me dio flojera crear un DataFrame, utilizar mejor una base datos, pueden ser facilmente creadas en sql y Python, querìa utilizar una que tenia creada pero no se encontraba en el mismo directorio que este cuaderno, investigar la manera de pasar un DataFrame de Pandas a SQL, y una forma de pasar un CSV a SQL


```python
pip install Flask-SQLAlchemy
```

    Collecting Flask-SQLAlchemy
      Using cached https://files.pythonhosted.org/packages/08/ca/582442cad71504a1514a2f053006c8bb128844133d6076a4df17117545fa/Flask_SQLAlchemy-2.4.0-py2.py3-none-any.whl
    Collecting SQLAlchemy>=0.8.0 (from Flask-SQLAlchemy)
    [?25l  Downloading https://files.pythonhosted.org/packages/fc/49/82d64d705ced344ba458197dadab30cfa745f9650ee22260ac2b275d288c/SQLAlchemy-1.3.8.tar.gz (5.9MB)
    [K     |████████████████████████████████| 5.9MB 558kB/s eta 0:00:01     |████████████████████████████    | 5.2MB 650kB/s eta 0:00:02
    [?25hCollecting Flask>=0.10 (from Flask-SQLAlchemy)
    [?25l  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
    [K     |████████████████████████████████| 102kB 623kB/s ta 0:00:01
    [?25hCollecting itsdangerous>=0.24 (from Flask>=0.10->Flask-SQLAlchemy)
      Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
    Requirement already satisfied: Werkzeug>=0.15 in ./lib/python3.7/site-packages (from Flask>=0.10->Flask-SQLAlchemy) (0.15.4)
    Collecting click>=5.1 (from Flask>=0.10->Flask-SQLAlchemy)
    [?25l  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
    [K     |████████████████████████████████| 81kB 762kB/s eta 0:00:011
    [?25hRequirement already satisfied: Jinja2>=2.10.1 in ./lib/python3.7/site-packages (from Flask>=0.10->Flask-SQLAlchemy) (2.10.1)
    Requirement already satisfied: MarkupSafe>=0.23 in ./lib/python3.7/site-packages (from Jinja2>=2.10.1->Flask>=0.10->Flask-SQLAlchemy) (1.1.1)
    Building wheels for collected packages: SQLAlchemy
      Building wheel for SQLAlchemy (setup.py) ... [?25ldone
    [?25h  Stored in directory: /home/aaroncedillo/.cache/pip/wheels/97/b6/66/de2064d40c920adc2984ff3b8fd4f11494c8ab9e48ba87e8a2
    Successfully built SQLAlchemy
    Installing collected packages: SQLAlchemy, itsdangerous, click, Flask, Flask-SQLAlchemy
    Successfully installed Flask-1.1.1 Flask-SQLAlchemy-2.4.0 SQLAlchemy-1.3.8 click-7.0 itsdangerous-1.1.0
    Note: you may need to restart the kernel to use updated packages.



```python
pip install pymysql
```

    Collecting pymysql
    [?25l  Downloading https://files.pythonhosted.org/packages/ed/39/15045ae46f2a123019aa968dfcba0396c161c20f855f11dea6796bcaae95/PyMySQL-0.9.3-py2.py3-none-any.whl (47kB)
    [K     |████████████████████████████████| 51kB 274kB/s eta 0:00:01     |█████████████▊                  | 20kB 320kB/s eta 0:00:01
    [?25hInstalling collected packages: pymysql
    Successfully installed pymysql-0.9.3
    Note: you may need to restart the kernel to use updated packages.



```python
import sqlite3
from sqlalchemy import create_engine
import pymysql
```


```python
def sql_connection():
 
    try
 
        con = sqlite3.connect('mydatabase.db')
 
        return con
 
    except Error:
 
        print(Error)
 
def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
 
    con.commit()
 
con = sql_connection()
 
sql_table(con)
```


```python
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
sql_insert(con, entities)
```


```python
frame = pd.read_sql("select * FROM employees", con);
frame
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
      <th>name</th>
      <th>salary</th>
      <th>department</th>
      <th>position</th>
      <th>hireDate</th>
      <th>test</th>
      <th>bool</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Andrew</td>
      <td>800.0</td>
      <td>IT</td>
      <td>Tech</td>
      <td>2018-02-06</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Aaron</td>
      <td>10000.0</td>
      <td>Development</td>
      <td>Developer</td>
      <td>2018-08-16</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame['name']
```




    0    Andrew
    1    Aaron 
    Name: name, dtype: object




```python
frame['salary'] > 800
```




    0    False
    1     True
    Name: salary, dtype: bool




```python
# Add a new column to employees table
addColumn = "ALTER TABLE employees ADD COLUMN bool text"
con.execute(addColumn)
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    <ipython-input-77-e012bac45046> in <module>
          1 # Add a new column to employees table
          2 addColumn = "ALTER TABLE employees ADD COLUMN bool bool"
    ----> 3 con.execute(addColumn)
    

    OperationalError: duplicate column name: bool



```python
frame
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
      <th>name</th>
      <th>salary</th>
      <th>department</th>
      <th>position</th>
      <th>hireDate</th>
      <th>test</th>
      <th>bool</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Andrew</td>
      <td>800.0</td>
      <td>IT</td>
      <td>Tech</td>
      <td>2018-02-06</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Aaron</td>
      <td>10000.0</td>
      <td>Development</td>
      <td>Developer</td>
      <td>2018-08-16</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame
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
      <th>name</th>
      <th>salary</th>
      <th>department</th>
      <th>position</th>
      <th>hireDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Andrew</td>
      <td>800.0</td>
      <td>IT</td>
      <td>Tech</td>
      <td>2018-02-06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Aaron</td>
      <td>10000.0</td>
      <td>Development</td>
      <td>Developer</td>
      <td>2018-08-16</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_Frame = pd.read_sql("select * FROM employees", con);
new_Frame
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
      <th>name</th>
      <th>salary</th>
      <th>department</th>
      <th>position</th>
      <th>hireDate</th>
      <th>test</th>
      <th>bool</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Andrew</td>
      <td>800.0</td>
      <td>IT</td>
      <td>Tech</td>
      <td>2018-02-06</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Aaron</td>
      <td>10000.0</td>
      <td>Development</td>
      <td>Developer</td>
      <td>2018-08-16</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = new_Frame['salary'] > 800
data
```




    0    False
    1     True
    Name: salary, dtype: bool




```python
# Agregando valores al DataFrame
new_Frame.loc[[0,1],'bool'] = data
new_Frame
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
      <th>name</th>
      <th>salary</th>
      <th>department</th>
      <th>position</th>
      <th>hireDate</th>
      <th>test</th>
      <th>bool</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Andrew</td>
      <td>800.0</td>
      <td>IT</td>
      <td>Tech</td>
      <td>2018-02-06</td>
      <td>None</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Aaron</td>
      <td>10000.0</td>
      <td>Development</td>
      <td>Developer</td>
      <td>2018-08-16</td>
      <td>None</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# aislar solo a una columna del dataFrame
pop = new_Frame.pop('bool')
pop
```




    0    False
    1     True
    Name: bool, dtype: bool




```python
new_Frame.drop(columns='test')
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
      <th>name</th>
      <th>salary</th>
      <th>department</th>
      <th>position</th>
      <th>hireDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Andrew</td>
      <td>800.0</td>
      <td>IT</td>
      <td>Tech</td>
      <td>2018-02-06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Aaron</td>
      <td>10000.0</td>
      <td>Development</td>
      <td>Developer</td>
      <td>2018-08-16</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Leeremos un archivo CSV (comma-separated values)
file = pd.read_csv("SMSSpamCollection.csv", sep=',')
file.head(15)
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
      <th>ham</th>
      <th>Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ham</td>
      <td>Ok lar... Joking wif u oni...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>spam</td>
      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ham</td>
      <td>U dun say so early hor... U c already then say...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ham</td>
      <td>Nah I don't think he goes to usf, he lives aro...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>spam</td>
      <td>FreeMsg Hey there darling it's been 3 week's n...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ham</td>
      <td>Even my brother is not like to speak with me. ...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>ham</td>
      <td>As per your request 'Melle Melle (Oru Minnamin...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>spam</td>
      <td>WINNER!! As a valued network customer you have...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>spam</td>
      <td>Had your mobile 11 months or more? U R entitle...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ham</td>
      <td>I'm gonna be home soon and i don't want to tal...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>spam</td>
      <td>SIX chances to win CASH! From 100 to 20,000 po...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>spam</td>
      <td>URGENT! You have won a 1 week FREE membership ...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ham</td>
      <td>I've been searching for the right words to tha...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>ham</td>
      <td>I HAVE A DATE ON SUNDAY WITH WILL!!</td>
    </tr>
    <tr>
      <th>14</th>
      <td>spam</td>
      <td>XXXMobileMovieClub: To use your credit, click ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Operando con DataFrames
file.columns
```




    Index(['ham', 'Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...'], dtype='object')




```python
file.shape
```




    (5573, 2)



#### Data Cleaning


```python
file.head()
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
      <th>ham</th>
      <th>Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ham</td>
      <td>Ok lar... Joking wif u oni...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>spam</td>
      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ham</td>
      <td>U dun say so early hor... U c already then say...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ham</td>
      <td>Nah I don't think he goes to usf, he lives aro...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>spam</td>
      <td>FreeMsg Hey there darling it's been 3 week's n...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Buscar valores nulos
file.isnull().anyy()
```




    ham                                                                                                                False
    Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...    False
    dtype: bool




```python
new_file = pd.read_csv("housing.csv", sep=',')
new_file.head(15)
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
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>median_house_value</th>
      <th>ocean_proximity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-122.23</td>
      <td>37.88</td>
      <td>41.0</td>
      <td>880.0</td>
      <td>129.0</td>
      <td>322.0</td>
      <td>126.0</td>
      <td>8.3252</td>
      <td>452600.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-122.22</td>
      <td>37.86</td>
      <td>21.0</td>
      <td>7099.0</td>
      <td>1106.0</td>
      <td>2401.0</td>
      <td>1138.0</td>
      <td>8.3014</td>
      <td>358500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-122.24</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>1467.0</td>
      <td>190.0</td>
      <td>496.0</td>
      <td>177.0</td>
      <td>7.2574</td>
      <td>352100.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-122.25</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>1274.0</td>
      <td>235.0</td>
      <td>558.0</td>
      <td>219.0</td>
      <td>5.6431</td>
      <td>341300.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-122.25</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>1627.0</td>
      <td>280.0</td>
      <td>565.0</td>
      <td>259.0</td>
      <td>3.8462</td>
      <td>342200.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-122.25</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>919.0</td>
      <td>213.0</td>
      <td>413.0</td>
      <td>193.0</td>
      <td>4.0368</td>
      <td>269700.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-122.25</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>2535.0</td>
      <td>489.0</td>
      <td>1094.0</td>
      <td>514.0</td>
      <td>3.6591</td>
      <td>299200.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-122.25</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>3104.0</td>
      <td>687.0</td>
      <td>1157.0</td>
      <td>647.0</td>
      <td>3.1200</td>
      <td>241400.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-122.26</td>
      <td>37.84</td>
      <td>42.0</td>
      <td>2555.0</td>
      <td>665.0</td>
      <td>1206.0</td>
      <td>595.0</td>
      <td>2.0804</td>
      <td>226700.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-122.25</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>3549.0</td>
      <td>707.0</td>
      <td>1551.0</td>
      <td>714.0</td>
      <td>3.6912</td>
      <td>261100.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2202.0</td>
      <td>434.0</td>
      <td>910.0</td>
      <td>402.0</td>
      <td>3.2031</td>
      <td>281500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>11</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>3503.0</td>
      <td>752.0</td>
      <td>1504.0</td>
      <td>734.0</td>
      <td>3.2705</td>
      <td>241800.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2491.0</td>
      <td>474.0</td>
      <td>1098.0</td>
      <td>468.0</td>
      <td>3.0750</td>
      <td>213500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-122.26</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>696.0</td>
      <td>191.0</td>
      <td>345.0</td>
      <td>174.0</td>
      <td>2.6736</td>
      <td>191300.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2643.0</td>
      <td>626.0</td>
      <td>1212.0</td>
      <td>620.0</td>
      <td>1.9167</td>
      <td>159200.0</td>
      <td>NEAR BAY</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_file.isnull().any()
```




    longitude             False
    latitude              False
    housing_median_age    False
    total_rooms           False
    total_bedrooms         True
    population            False
    households            False
    median_income         False
    median_house_value    False
    ocean_proximity       False
    dtype: bool




```python
#En el nuevo set de datos si contamos con valores nulos, contemos los valores del dataSet
count = new_file.shape[0]
print("La cantidad de valores antes de borrar es: ", count)
```

    La cantidad de valores antes de borrar es:  20640



```python
#Eliminamos las filas con valores nulos
new_file = new_file.dropna()
print("La nueva cantidad de valores es: ", count-new_file.shape[0], "filas")
```

    La nueva cantidad de valores es:  207 filas



```python
print("Comprobamos: ", new_file.shape[0])
```

    Comprobamos:  20433


#### Graficar con Pandas


```python
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-dark")
```


```python
new_file = pd.read_csv("housing.csv", sep=',')
new_file.head(15)
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
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>median_house_value</th>
      <th>ocean_proximity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-122.23</td>
      <td>37.88</td>
      <td>41.0</td>
      <td>880.0</td>
      <td>129.0</td>
      <td>322.0</td>
      <td>126.0</td>
      <td>8.3252</td>
      <td>452600.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-122.22</td>
      <td>37.86</td>
      <td>21.0</td>
      <td>7099.0</td>
      <td>1106.0</td>
      <td>2401.0</td>
      <td>1138.0</td>
      <td>8.3014</td>
      <td>358500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-122.24</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>1467.0</td>
      <td>190.0</td>
      <td>496.0</td>
      <td>177.0</td>
      <td>7.2574</td>
      <td>352100.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-122.25</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>1274.0</td>
      <td>235.0</td>
      <td>558.0</td>
      <td>219.0</td>
      <td>5.6431</td>
      <td>341300.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-122.25</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>1627.0</td>
      <td>280.0</td>
      <td>565.0</td>
      <td>259.0</td>
      <td>3.8462</td>
      <td>342200.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-122.25</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>919.0</td>
      <td>213.0</td>
      <td>413.0</td>
      <td>193.0</td>
      <td>4.0368</td>
      <td>269700.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-122.25</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>2535.0</td>
      <td>489.0</td>
      <td>1094.0</td>
      <td>514.0</td>
      <td>3.6591</td>
      <td>299200.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-122.25</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>3104.0</td>
      <td>687.0</td>
      <td>1157.0</td>
      <td>647.0</td>
      <td>3.1200</td>
      <td>241400.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-122.26</td>
      <td>37.84</td>
      <td>42.0</td>
      <td>2555.0</td>
      <td>665.0</td>
      <td>1206.0</td>
      <td>595.0</td>
      <td>2.0804</td>
      <td>226700.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-122.25</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>3549.0</td>
      <td>707.0</td>
      <td>1551.0</td>
      <td>714.0</td>
      <td>3.6912</td>
      <td>261100.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2202.0</td>
      <td>434.0</td>
      <td>910.0</td>
      <td>402.0</td>
      <td>3.2031</td>
      <td>281500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>11</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>3503.0</td>
      <td>752.0</td>
      <td>1504.0</td>
      <td>734.0</td>
      <td>3.2705</td>
      <td>241800.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2491.0</td>
      <td>474.0</td>
      <td>1098.0</td>
      <td>468.0</td>
      <td>3.0750</td>
      <td>213500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-122.26</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>696.0</td>
      <td>191.0</td>
      <td>345.0</td>
      <td>174.0</td>
      <td>2.6736</td>
      <td>191300.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-122.26</td>
      <td>37.85</td>
      <td>52.0</td>
      <td>2643.0</td>
      <td>626.0</td>
      <td>1212.0</td>
      <td>620.0</td>
      <td>1.9167</td>
      <td>159200.0</td>
      <td>NEAR BAY</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_file.hist(bins = 10, column='housing_median_age', width=4, figsize=(6, 6))
```




    array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f16a8016d30>]],
          dtype=object)




![png](output_44_1.png)



```python
new_file.boxplot(column='housing_median_age', figsize=(6, 6))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f16ad535470>




![png](output_45_1.png)


<img src="https://pro.arcgis.com/en/pro-app/help/analysis/geoprocessing/charts/GUID-0E2C3730-C535-40CD-8152-80D794A996A7-web.png">


```python
# Seleccionando columnas en especifico
new_file[['latitude', 'total_rooms']].head()
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
      <th>latitude</th>
      <th>total_rooms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.88</td>
      <td>880.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>37.86</td>
      <td>7099.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>37.85</td>
      <td>1467.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>37.85</td>
      <td>1274.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>37.85</td>
      <td>1627.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#ultimas 10 filas
new_file.tail(10)
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
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>median_house_value</th>
      <th>ocean_proximity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20630</th>
      <td>-121.32</td>
      <td>39.29</td>
      <td>11.0</td>
      <td>2640.0</td>
      <td>505.0</td>
      <td>1257.0</td>
      <td>445.0</td>
      <td>3.5673</td>
      <td>112000.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20631</th>
      <td>-121.40</td>
      <td>39.33</td>
      <td>15.0</td>
      <td>2655.0</td>
      <td>493.0</td>
      <td>1200.0</td>
      <td>432.0</td>
      <td>3.5179</td>
      <td>107200.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20632</th>
      <td>-121.45</td>
      <td>39.26</td>
      <td>15.0</td>
      <td>2319.0</td>
      <td>416.0</td>
      <td>1047.0</td>
      <td>385.0</td>
      <td>3.1250</td>
      <td>115600.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20633</th>
      <td>-121.53</td>
      <td>39.19</td>
      <td>27.0</td>
      <td>2080.0</td>
      <td>412.0</td>
      <td>1082.0</td>
      <td>382.0</td>
      <td>2.5495</td>
      <td>98300.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20634</th>
      <td>-121.56</td>
      <td>39.27</td>
      <td>28.0</td>
      <td>2332.0</td>
      <td>395.0</td>
      <td>1041.0</td>
      <td>344.0</td>
      <td>3.7125</td>
      <td>116800.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>-121.09</td>
      <td>39.48</td>
      <td>25.0</td>
      <td>1665.0</td>
      <td>374.0</td>
      <td>845.0</td>
      <td>330.0</td>
      <td>1.5603</td>
      <td>78100.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>-121.21</td>
      <td>39.49</td>
      <td>18.0</td>
      <td>697.0</td>
      <td>150.0</td>
      <td>356.0</td>
      <td>114.0</td>
      <td>2.5568</td>
      <td>77100.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>-121.22</td>
      <td>39.43</td>
      <td>17.0</td>
      <td>2254.0</td>
      <td>485.0</td>
      <td>1007.0</td>
      <td>433.0</td>
      <td>1.7000</td>
      <td>92300.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>-121.32</td>
      <td>39.43</td>
      <td>18.0</td>
      <td>1860.0</td>
      <td>409.0</td>
      <td>741.0</td>
      <td>349.0</td>
      <td>1.8672</td>
      <td>84700.0</td>
      <td>INLAND</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>-121.24</td>
      <td>39.37</td>
      <td>16.0</td>
      <td>2785.0</td>
      <td>616.0</td>
      <td>1387.0</td>
      <td>530.0</td>
      <td>2.3886</td>
      <td>89400.0</td>
      <td>INLAND</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Contar los valores del mismo valor en alguna columna
new_file_counts = new_file['latitude'].value_counts()
new_file_counts.head(10)
```




    34.06    244
    34.05    236
    34.08    234
    34.07    231
    34.04    221
    34.09    212
    34.02    208
    34.10    203
    34.03    193
    33.93    181
    Name: latitude, dtype: int64



### Seleccionando / Filtrando Filas


```python
data_Filter = new_file['latitude'] >= 30.0
new_file[data_Filter][30:50]
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
      <th>longitude</th>
      <th>latitude</th>
      <th>housing_median_age</th>
      <th>total_rooms</th>
      <th>total_bedrooms</th>
      <th>population</th>
      <th>households</th>
      <th>median_income</th>
      <th>median_house_value</th>
      <th>ocean_proximity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>-122.28</td>
      <td>37.84</td>
      <td>49.0</td>
      <td>1916.0</td>
      <td>447.0</td>
      <td>863.0</td>
      <td>378.0</td>
      <td>1.9274</td>
      <td>122300.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>31</th>
      <td>-122.28</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>2153.0</td>
      <td>481.0</td>
      <td>1168.0</td>
      <td>441.0</td>
      <td>1.9615</td>
      <td>115200.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>32</th>
      <td>-122.27</td>
      <td>37.84</td>
      <td>48.0</td>
      <td>1922.0</td>
      <td>409.0</td>
      <td>1026.0</td>
      <td>335.0</td>
      <td>1.7969</td>
      <td>110400.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>33</th>
      <td>-122.27</td>
      <td>37.83</td>
      <td>49.0</td>
      <td>1655.0</td>
      <td>366.0</td>
      <td>754.0</td>
      <td>329.0</td>
      <td>1.3750</td>
      <td>104900.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>34</th>
      <td>-122.27</td>
      <td>37.83</td>
      <td>51.0</td>
      <td>2665.0</td>
      <td>574.0</td>
      <td>1258.0</td>
      <td>536.0</td>
      <td>2.7303</td>
      <td>109700.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>35</th>
      <td>-122.27</td>
      <td>37.83</td>
      <td>49.0</td>
      <td>1215.0</td>
      <td>282.0</td>
      <td>570.0</td>
      <td>264.0</td>
      <td>1.4861</td>
      <td>97200.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>36</th>
      <td>-122.27</td>
      <td>37.83</td>
      <td>48.0</td>
      <td>1798.0</td>
      <td>432.0</td>
      <td>987.0</td>
      <td>374.0</td>
      <td>1.0972</td>
      <td>104500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>37</th>
      <td>-122.28</td>
      <td>37.83</td>
      <td>52.0</td>
      <td>1511.0</td>
      <td>390.0</td>
      <td>901.0</td>
      <td>403.0</td>
      <td>1.4103</td>
      <td>103900.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>38</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>52.0</td>
      <td>1470.0</td>
      <td>330.0</td>
      <td>689.0</td>
      <td>309.0</td>
      <td>3.4800</td>
      <td>191400.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>39</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>52.0</td>
      <td>2432.0</td>
      <td>715.0</td>
      <td>1377.0</td>
      <td>696.0</td>
      <td>2.5898</td>
      <td>176000.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>40</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>52.0</td>
      <td>1665.0</td>
      <td>419.0</td>
      <td>946.0</td>
      <td>395.0</td>
      <td>2.0978</td>
      <td>155400.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>41</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>51.0</td>
      <td>936.0</td>
      <td>311.0</td>
      <td>517.0</td>
      <td>249.0</td>
      <td>1.2852</td>
      <td>150000.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>42</th>
      <td>-122.26</td>
      <td>37.84</td>
      <td>49.0</td>
      <td>713.0</td>
      <td>202.0</td>
      <td>462.0</td>
      <td>189.0</td>
      <td>1.0250</td>
      <td>118800.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>43</th>
      <td>-122.26</td>
      <td>37.84</td>
      <td>52.0</td>
      <td>950.0</td>
      <td>202.0</td>
      <td>467.0</td>
      <td>198.0</td>
      <td>3.9643</td>
      <td>188800.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>44</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>52.0</td>
      <td>1443.0</td>
      <td>311.0</td>
      <td>660.0</td>
      <td>292.0</td>
      <td>3.0125</td>
      <td>184400.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>45</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>52.0</td>
      <td>1656.0</td>
      <td>420.0</td>
      <td>718.0</td>
      <td>382.0</td>
      <td>2.6768</td>
      <td>182300.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>46</th>
      <td>-122.26</td>
      <td>37.83</td>
      <td>50.0</td>
      <td>1125.0</td>
      <td>322.0</td>
      <td>616.0</td>
      <td>304.0</td>
      <td>2.0260</td>
      <td>142500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>47</th>
      <td>-122.27</td>
      <td>37.82</td>
      <td>43.0</td>
      <td>1007.0</td>
      <td>312.0</td>
      <td>558.0</td>
      <td>253.0</td>
      <td>1.7348</td>
      <td>137500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>48</th>
      <td>-122.26</td>
      <td>37.82</td>
      <td>40.0</td>
      <td>624.0</td>
      <td>195.0</td>
      <td>423.0</td>
      <td>160.0</td>
      <td>0.9506</td>
      <td>187500.0</td>
      <td>NEAR BAY</td>
    </tr>
    <tr>
      <th>49</th>
      <td>-122.27</td>
      <td>37.82</td>
      <td>40.0</td>
      <td>946.0</td>
      <td>375.0</td>
      <td>700.0</td>
      <td>352.0</td>
      <td>1.7750</td>
      <td>112500.0</td>
      <td>NEAR BAY</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_count = new_file[['latitude', 'population']].groupby('latitude').count()
data_count.head(10)
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
      <th>population</th>
    </tr>
    <tr>
      <th>latitude</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32.54</th>
      <td>1</td>
    </tr>
    <tr>
      <th>32.55</th>
      <td>3</td>
    </tr>
    <tr>
      <th>32.56</th>
      <td>10</td>
    </tr>
    <tr>
      <th>32.57</th>
      <td>18</td>
    </tr>
    <tr>
      <th>32.58</th>
      <td>26</td>
    </tr>
    <tr>
      <th>32.59</th>
      <td>11</td>
    </tr>
    <tr>
      <th>32.60</th>
      <td>9</td>
    </tr>
    <tr>
      <th>32.61</th>
      <td>14</td>
    </tr>
    <tr>
      <th>32.62</th>
      <td>13</td>
    </tr>
    <tr>
      <th>32.63</th>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>




```python
 
```
