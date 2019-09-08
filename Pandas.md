
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



```python

```
