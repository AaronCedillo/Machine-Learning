
### Clasificacion usando Scikit-Learn

#### Analisis diario de datos meteorologicos
Utilizaremos Scikit-Learn para realizar una clasificacion de datos meteorologicos basado en un arbol de desiciones


```python
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
```

### Creando un DataFrame de Pandas mediante el CSV


```python
data = pd.read_csv('daily_weather.csv')
```


```python
data.columns
```




    Index(['number', 'air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
           'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
           'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am',
           'relative_humidity_3pm'],
          dtype='object')




```python
data.head(15)
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
      <th>number</th>
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>918.060000</td>
      <td>74.822000</td>
      <td>271.100000</td>
      <td>2.080354</td>
      <td>295.400000</td>
      <td>2.863283</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>42.420000</td>
      <td>36.160000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>917.347688</td>
      <td>71.403843</td>
      <td>101.935179</td>
      <td>2.443009</td>
      <td>140.471548</td>
      <td>3.533324</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>24.328697</td>
      <td>19.426597</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>923.040000</td>
      <td>60.638000</td>
      <td>51.000000</td>
      <td>17.067852</td>
      <td>63.700000</td>
      <td>22.100967</td>
      <td>0.00</td>
      <td>20.0</td>
      <td>8.900000</td>
      <td>14.460000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>920.502751</td>
      <td>70.138895</td>
      <td>198.832133</td>
      <td>4.337363</td>
      <td>211.203341</td>
      <td>5.190045</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>12.189102</td>
      <td>12.742547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>921.160000</td>
      <td>44.294000</td>
      <td>277.800000</td>
      <td>1.856660</td>
      <td>136.500000</td>
      <td>2.863283</td>
      <td>8.90</td>
      <td>14730.0</td>
      <td>92.410000</td>
      <td>76.740000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>915.300000</td>
      <td>78.404000</td>
      <td>182.800000</td>
      <td>9.932014</td>
      <td>189.000000</td>
      <td>10.983375</td>
      <td>0.02</td>
      <td>170.0</td>
      <td>35.130000</td>
      <td>33.930000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>915.598868</td>
      <td>70.043304</td>
      <td>177.875407</td>
      <td>3.745587</td>
      <td>186.606696</td>
      <td>4.589632</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>10.657422</td>
      <td>21.385657</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>918.070000</td>
      <td>51.710000</td>
      <td>242.400000</td>
      <td>2.527742</td>
      <td>271.600000</td>
      <td>3.646212</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>80.470000</td>
      <td>74.920000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>920.080000</td>
      <td>80.582000</td>
      <td>40.700000</td>
      <td>4.518619</td>
      <td>63.000000</td>
      <td>5.883152</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>29.580000</td>
      <td>24.030000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>915.010000</td>
      <td>47.498000</td>
      <td>163.100000</td>
      <td>4.943637</td>
      <td>195.900000</td>
      <td>6.576604</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>88.600000</td>
      <td>68.050000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>919.650000</td>
      <td>77.036000</td>
      <td>70.600000</td>
      <td>3.825167</td>
      <td>85.500000</td>
      <td>4.764682</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>22.070000</td>
      <td>32.130000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>915.640000</td>
      <td>45.716000</td>
      <td>241.600000</td>
      <td>5.860783</td>
      <td>265.800000</td>
      <td>8.030615</td>
      <td>0.55</td>
      <td>1770.0</td>
      <td>90.560000</td>
      <td>79.090000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>917.390000</td>
      <td>49.784000</td>
      <td>204.100000</td>
      <td>1.275056</td>
      <td>211.800000</td>
      <td>2.013246</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>73.150000</td>
      <td>58.430000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>920.820000</td>
      <td>62.438000</td>
      <td>213.600000</td>
      <td>2.617220</td>
      <td>165.700000</td>
      <td>3.310671</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>43.640000</td>
      <td>27.990000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>911.000000</td>
      <td>86.432000</td>
      <td>202.900000</td>
      <td>1.207948</td>
      <td>162.900000</td>
      <td>1.677705</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>15.190000</td>
      <td>24.370000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.tail(10)
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
      <th>number</th>
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1085</th>
      <td>1085</td>
      <td>914.84</td>
      <td>47.354</td>
      <td>190.9</td>
      <td>3.713320</td>
      <td>204.4</td>
      <td>4.652835</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>92.30</td>
      <td>88.16</td>
    </tr>
    <tr>
      <th>1086</th>
      <td>1086</td>
      <td>921.26</td>
      <td>52.646</td>
      <td>261.9</td>
      <td>2.035615</td>
      <td>260.5</td>
      <td>3.042238</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>91.11</td>
      <td>81.89</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>1087</td>
      <td>914.00</td>
      <td>66.650</td>
      <td>173.8</td>
      <td>8.366156</td>
      <td>181.0</td>
      <td>9.439887</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>30.92</td>
      <td>47.34</td>
    </tr>
    <tr>
      <th>1088</th>
      <td>1088</td>
      <td>912.90</td>
      <td>71.870</td>
      <td>129.2</td>
      <td>1.431642</td>
      <td>160.0</td>
      <td>2.057985</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>51.84</td>
      <td>55.49</td>
    </tr>
    <tr>
      <th>1089</th>
      <td>1089</td>
      <td>915.00</td>
      <td>55.040</td>
      <td>191.8</td>
      <td>5.368656</td>
      <td>220.9</td>
      <td>7.068730</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>73.55</td>
      <td>69.67</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>1090</td>
      <td>918.90</td>
      <td>63.104</td>
      <td>192.9</td>
      <td>3.869906</td>
      <td>207.3</td>
      <td>5.212070</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>26.02</td>
      <td>38.18</td>
    </tr>
    <tr>
      <th>1091</th>
      <td>1091</td>
      <td>918.71</td>
      <td>49.568</td>
      <td>241.6</td>
      <td>1.811921</td>
      <td>227.4</td>
      <td>2.371156</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>90.35</td>
      <td>73.34</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>1092</td>
      <td>916.60</td>
      <td>71.096</td>
      <td>189.3</td>
      <td>3.064608</td>
      <td>200.8</td>
      <td>3.892276</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>45.59</td>
      <td>52.31</td>
    </tr>
    <tr>
      <th>1093</th>
      <td>1093</td>
      <td>912.60</td>
      <td>58.406</td>
      <td>172.7</td>
      <td>3.825167</td>
      <td>189.1</td>
      <td>4.764682</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>64.84</td>
      <td>58.28</td>
    </tr>
    <tr>
      <th>1094</th>
      <td>1094</td>
      <td>921.53</td>
      <td>77.702</td>
      <td>97.1</td>
      <td>3.265932</td>
      <td>125.9</td>
      <td>4.451511</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>14.56</td>
      <td>15.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data.isnull().any(axis=1)]
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
      <th>number</th>
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>917.890000</td>
      <td>NaN</td>
      <td>169.200000</td>
      <td>2.192201</td>
      <td>196.800000</td>
      <td>2.930391</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>48.990000</td>
      <td>51.190000</td>
    </tr>
    <tr>
      <th>111</th>
      <td>111</td>
      <td>915.290000</td>
      <td>58.820000</td>
      <td>182.600000</td>
      <td>15.613841</td>
      <td>189.000000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>21.500000</td>
      <td>29.690000</td>
    </tr>
    <tr>
      <th>177</th>
      <td>177</td>
      <td>915.900000</td>
      <td>NaN</td>
      <td>183.300000</td>
      <td>4.719943</td>
      <td>189.900000</td>
      <td>5.346287</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>29.260000</td>
      <td>46.500000</td>
    </tr>
    <tr>
      <th>262</th>
      <td>262</td>
      <td>923.596607</td>
      <td>58.380598</td>
      <td>47.737753</td>
      <td>10.636273</td>
      <td>67.145843</td>
      <td>13.671423</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>17.990876</td>
      <td>16.461685</td>
    </tr>
    <tr>
      <th>277</th>
      <td>277</td>
      <td>920.480000</td>
      <td>62.600000</td>
      <td>194.400000</td>
      <td>2.751436</td>
      <td>NaN</td>
      <td>3.869906</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>52.580000</td>
      <td>54.030000</td>
    </tr>
    <tr>
      <th>334</th>
      <td>334</td>
      <td>916.230000</td>
      <td>75.740000</td>
      <td>149.100000</td>
      <td>2.751436</td>
      <td>187.500000</td>
      <td>4.183078</td>
      <td>NaN</td>
      <td>1480.000000</td>
      <td>31.880000</td>
      <td>32.900000</td>
    </tr>
    <tr>
      <th>358</th>
      <td>358</td>
      <td>917.440000</td>
      <td>58.514000</td>
      <td>55.100000</td>
      <td>10.021491</td>
      <td>NaN</td>
      <td>12.705819</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>13.880000</td>
      <td>25.930000</td>
    </tr>
    <tr>
      <th>361</th>
      <td>361</td>
      <td>920.444946</td>
      <td>65.801845</td>
      <td>49.823346</td>
      <td>21.520177</td>
      <td>61.886944</td>
      <td>25.549112</td>
      <td>NaN</td>
      <td>40.364018</td>
      <td>12.278715</td>
      <td>7.618649</td>
    </tr>
    <tr>
      <th>381</th>
      <td>381</td>
      <td>918.480000</td>
      <td>66.542000</td>
      <td>90.900000</td>
      <td>3.467257</td>
      <td>89.400000</td>
      <td>4.406772</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>20.640000</td>
      <td>14.350000</td>
    </tr>
    <tr>
      <th>409</th>
      <td>409</td>
      <td>NaN</td>
      <td>67.853833</td>
      <td>65.880616</td>
      <td>4.328594</td>
      <td>78.570923</td>
      <td>5.216734</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>18.487385</td>
      <td>20.356594</td>
    </tr>
    <tr>
      <th>517</th>
      <td>517</td>
      <td>920.570000</td>
      <td>53.600000</td>
      <td>100.100000</td>
      <td>4.697574</td>
      <td>NaN</td>
      <td>6.285801</td>
      <td>4.712</td>
      <td>14842.000000</td>
      <td>79.880000</td>
      <td>84.530000</td>
    </tr>
    <tr>
      <th>519</th>
      <td>519</td>
      <td>916.250000</td>
      <td>55.670000</td>
      <td>176.400000</td>
      <td>6.666081</td>
      <td>188.200000</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>72.550000</td>
      <td>74.390000</td>
    </tr>
    <tr>
      <th>546</th>
      <td>546</td>
      <td>NaN</td>
      <td>42.746000</td>
      <td>251.100000</td>
      <td>12.929513</td>
      <td>274.400000</td>
      <td>17.604718</td>
      <td>14.627</td>
      <td>7825.000000</td>
      <td>87.870000</td>
      <td>70.770000</td>
    </tr>
    <tr>
      <th>620</th>
      <td>620</td>
      <td>921.200000</td>
      <td>56.786000</td>
      <td>192.300000</td>
      <td>9.551734</td>
      <td>201.400000</td>
      <td>11.005745</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>59.790000</td>
      <td>77.750000</td>
    </tr>
    <tr>
      <th>625</th>
      <td>625</td>
      <td>912.400000</td>
      <td>50.774000</td>
      <td>171.600000</td>
      <td>NaN</td>
      <td>181.400000</td>
      <td>4.831790</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>86.840000</td>
      <td>64.740000</td>
    </tr>
    <tr>
      <th>656</th>
      <td>656</td>
      <td>920.830000</td>
      <td>66.344000</td>
      <td>NaN</td>
      <td>15.457255</td>
      <td>189.400000</td>
      <td>16.486248</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>23.770000</td>
      <td>51.630000</td>
    </tr>
    <tr>
      <th>670</th>
      <td>670</td>
      <td>910.920000</td>
      <td>48.362000</td>
      <td>156.500000</td>
      <td>NaN</td>
      <td>177.500000</td>
      <td>16.128337</td>
      <td>4.970</td>
      <td>10560.000000</td>
      <td>80.560000</td>
      <td>88.220000</td>
    </tr>
    <tr>
      <th>672</th>
      <td>672</td>
      <td>922.448945</td>
      <td>72.863773</td>
      <td>NaN</td>
      <td>3.682370</td>
      <td>214.196160</td>
      <td>4.849450</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>16.753670</td>
      <td>17.804720</td>
    </tr>
    <tr>
      <th>705</th>
      <td>705</td>
      <td>911.900000</td>
      <td>59.072000</td>
      <td>199.800000</td>
      <td>1.275056</td>
      <td>239.500000</td>
      <td>1.834291</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>77.630000</td>
      <td>59.130000</td>
    </tr>
    <tr>
      <th>731</th>
      <td>731</td>
      <td>922.970166</td>
      <td>51.391847</td>
      <td>33.810942</td>
      <td>NaN</td>
      <td>59.290089</td>
      <td>11.111555</td>
      <td>0.000</td>
      <td>4.735034</td>
      <td>34.807753</td>
      <td>18.418179</td>
    </tr>
    <tr>
      <th>737</th>
      <td>737</td>
      <td>917.895130</td>
      <td>76.804690</td>
      <td>104.771020</td>
      <td>1.632705</td>
      <td>97.178763</td>
      <td>NaN</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>13.771311</td>
      <td>16.792455</td>
    </tr>
    <tr>
      <th>788</th>
      <td>788</td>
      <td>917.923442</td>
      <td>73.249717</td>
      <td>42.101739</td>
      <td>4.132698</td>
      <td>64.284969</td>
      <td>5.345258</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>6.939692</td>
      <td>18.793825</td>
    </tr>
    <tr>
      <th>840</th>
      <td>840</td>
      <td>918.043767</td>
      <td>NaN</td>
      <td>181.774042</td>
      <td>0.964376</td>
      <td>185.618601</td>
      <td>1.570007</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>11.911222</td>
      <td>18.154358</td>
    </tr>
    <tr>
      <th>848</th>
      <td>848</td>
      <td>915.250000</td>
      <td>37.562000</td>
      <td>246.500000</td>
      <td>11.587349</td>
      <td>258.700000</td>
      <td>NaN</td>
      <td>3.171</td>
      <td>2891.000000</td>
      <td>91.000000</td>
      <td>90.780000</td>
    </tr>
    <tr>
      <th>861</th>
      <td>861</td>
      <td>919.065408</td>
      <td>NaN</td>
      <td>172.303728</td>
      <td>2.639600</td>
      <td>193.058141</td>
      <td>3.326949</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>12.497839</td>
      <td>13.438518</td>
    </tr>
    <tr>
      <th>869</th>
      <td>869</td>
      <td>NaN</td>
      <td>45.104000</td>
      <td>259.000000</td>
      <td>3.265932</td>
      <td>275.000000</td>
      <td>4.026492</td>
      <td>0.000</td>
      <td>80.000000</td>
      <td>85.270000</td>
      <td>90.260000</td>
    </tr>
    <tr>
      <th>998</th>
      <td>998</td>
      <td>914.140000</td>
      <td>71.240000</td>
      <td>NaN</td>
      <td>1.722444</td>
      <td>232.900000</td>
      <td>2.326418</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>24.200000</td>
      <td>41.380000</td>
    </tr>
    <tr>
      <th>1031</th>
      <td>1031</td>
      <td>922.669195</td>
      <td>NaN</td>
      <td>47.946284</td>
      <td>7.969686</td>
      <td>65.770066</td>
      <td>10.262337</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>18.920805</td>
      <td>19.641841</td>
    </tr>
    <tr>
      <th>1035</th>
      <td>1035</td>
      <td>919.670000</td>
      <td>77.576000</td>
      <td>171.800000</td>
      <td>6.554234</td>
      <td>191.000000</td>
      <td>8.164831</td>
      <td>0.000</td>
      <td>NaN</td>
      <td>56.860000</td>
      <td>50.650000</td>
    </tr>
    <tr>
      <th>1063</th>
      <td>1063</td>
      <td>917.300185</td>
      <td>65.790001</td>
      <td>NaN</td>
      <td>1.879553</td>
      <td>222.498226</td>
      <td>2.692862</td>
      <td>0.000</td>
      <td>0.000000</td>
      <td>14.972668</td>
      <td>20.966267</td>
    </tr>
    <tr>
      <th>1066</th>
      <td>1066</td>
      <td>919.564869</td>
      <td>73.726732</td>
      <td>68.704694</td>
      <td>3.551777</td>
      <td>102.571616</td>
      <td>4.861315</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>11.657314</td>
      <td>17.331823</td>
    </tr>
  </tbody>
</table>
</div>



#### Limpieza de datos


```python
# Borraremos la columna 'number', no nos servira en nuestro analisis
del data['number']
```


```python
data.head()
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
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>918.060000</td>
      <td>74.822000</td>
      <td>271.100000</td>
      <td>2.080354</td>
      <td>295.400000</td>
      <td>2.863283</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>42.420000</td>
      <td>36.160000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>917.347688</td>
      <td>71.403843</td>
      <td>101.935179</td>
      <td>2.443009</td>
      <td>140.471548</td>
      <td>3.533324</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>24.328697</td>
      <td>19.426597</td>
    </tr>
    <tr>
      <th>2</th>
      <td>923.040000</td>
      <td>60.638000</td>
      <td>51.000000</td>
      <td>17.067852</td>
      <td>63.700000</td>
      <td>22.100967</td>
      <td>0.0</td>
      <td>20.0</td>
      <td>8.900000</td>
      <td>14.460000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>920.502751</td>
      <td>70.138895</td>
      <td>198.832133</td>
      <td>4.337363</td>
      <td>211.203341</td>
      <td>5.190045</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>12.189102</td>
      <td>12.742547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>921.160000</td>
      <td>44.294000</td>
      <td>277.800000</td>
      <td>1.856660</td>
      <td>136.500000</td>
      <td>2.863283</td>
      <td>8.9</td>
      <td>14730.0</td>
      <td>92.410000</td>
      <td>76.740000</td>
    </tr>
  </tbody>
</table>
</div>



#### Eliminando valores nulos


```python
before_rows = data.shape[0]
print("antes de la limpieza --> ", before_rows)
```

    antes de la limpieza -->  1095



```python
data = data.dropna()
```


```python
after_rows = data.shape[0]
print("despues de la limpieza --> ", after_rows)
```

    despues de la limpieza -->  1064


#### Apliquemos clasificacion
Binarizamos relative_humidity_3pm a 0 y 1


```python
clean_data = data.copy() # Generamos un nuevo dataFrame
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] > 24.99)*1
print(clean_data['high_humidity_label'])
```

    0       1
    1       0
    2       0
    3       0
    4       1
    5       1
    6       0
    7       1
    8       0
    9       1
    10      1
    11      1
    12      1
    13      1
    14      0
    15      0
    17      0
    18      1
    19      0
    20      0
    21      1
    22      0
    23      1
    24      0
    25      1
    26      1
    27      1
    28      1
    29      1
    30      1
           ..
    1064    1
    1065    1
    1067    1
    1068    1
    1069    1
    1070    1
    1071    1
    1072    0
    1073    1
    1074    1
    1075    0
    1076    0
    1077    1
    1078    0
    1079    1
    1080    0
    1081    0
    1082    1
    1083    1
    1084    1
    1085    1
    1086    1
    1087    1
    1088    1
    1089    1
    1090    1
    1091    1
    1092    1
    1093    1
    1094    0
    Name: high_humidity_label, Length: 1064, dtype: int64


#### El obetivo lo guardamos en 'y'


```python
y = clean_data[['high_humidity_label']].copy()
```


```python
clean_data['relative_humidity_3pm'].head()
```




    0    36.160000
    1    19.426597
    2    14.460000
    3    12.742547
    4    76.740000
    Name: relative_humidity_3pm, dtype: float64




```python
y.head(10)
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
      <th>high_humidity_label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### Usaremos las señales de los sensores de 9am como caracteristicas para predecir la humedad a las 3pm


```python
data.head()
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
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
      <th>relative_humidity_9am</th>
      <th>relative_humidity_3pm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>918.060000</td>
      <td>74.822000</td>
      <td>271.100000</td>
      <td>2.080354</td>
      <td>295.400000</td>
      <td>2.863283</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>42.420000</td>
      <td>36.160000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>917.347688</td>
      <td>71.403843</td>
      <td>101.935179</td>
      <td>2.443009</td>
      <td>140.471548</td>
      <td>3.533324</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>24.328697</td>
      <td>19.426597</td>
    </tr>
    <tr>
      <th>2</th>
      <td>923.040000</td>
      <td>60.638000</td>
      <td>51.000000</td>
      <td>17.067852</td>
      <td>63.700000</td>
      <td>22.100967</td>
      <td>0.0</td>
      <td>20.0</td>
      <td>8.900000</td>
      <td>14.460000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>920.502751</td>
      <td>70.138895</td>
      <td>198.832133</td>
      <td>4.337363</td>
      <td>211.203341</td>
      <td>5.190045</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>12.189102</td>
      <td>12.742547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>921.160000</td>
      <td>44.294000</td>
      <td>277.800000</td>
      <td>1.856660</td>
      <td>136.500000</td>
      <td>2.863283</td>
      <td>8.9</td>
      <td>14730.0</td>
      <td>92.410000</td>
      <td>76.740000</td>
    </tr>
  </tbody>
</table>
</div>




```python
morning_features = ['air_pressure_9am','air_temp_9am', 'avg_wind_direction_9am',
       'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
       'rain_accumulation_9am', 'rain_duration_9am']
```


```python
X = clean_data[morning_features].copy()
```


```python
X.columns
```




    Index(['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
           'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
           'rain_accumulation_9am', 'rain_duration_9am'],
          dtype='object')




```python
y.columns
```




    Index(['high_humidity_label'], dtype='object')



#### Realizamos la particion de nuestro set de datos, en datos de entrenamiento y prueba

### REMINDER:
En la ***Fase de entrenamiento*** el algoritmo de entrenamiento utiliza los datos de entrenamiento para ajustar los parametros del modelo para minimizar los errores. Al final de esta fase obtienes el modelo entrenado.

En la ***Fase de prueba*** el modelo entrenado se aplica a los datos de prueba, los datos de prueba estan separados de los datos de entrenamiento y el modelo no los ha visto anteriormente. Luego se evalua el modelo sobre como se comportan los datos de prueba. 


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
```

#### Ajustamos


```python
# Creamos el clasificador
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)

# Le paso los valores a entrenar 
humidity_classifier.fit(X_train, y_train)
```




    DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                max_features=None, max_leaf_nodes=10,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, presort=False, random_state=0,
                splitter='best')




```python
type(humidity_classifier)
```




    sklearn.tree.tree.DecisionTreeClassifier



#### Predict on Test set


```python
prediction = humidity_classifier.predict(X_test)
X_test
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
      <th>air_pressure_9am</th>
      <th>air_temp_9am</th>
      <th>avg_wind_direction_9am</th>
      <th>avg_wind_speed_9am</th>
      <th>max_wind_direction_9am</th>
      <th>max_wind_speed_9am</th>
      <th>rain_accumulation_9am</th>
      <th>rain_duration_9am</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>456</th>
      <td>918.800000</td>
      <td>80.384000</td>
      <td>189.600000</td>
      <td>1.767183</td>
      <td>80.300000</td>
      <td>2.773806</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>845</th>
      <td>921.613373</td>
      <td>68.658973</td>
      <td>70.703555</td>
      <td>2.248932</td>
      <td>96.844701</td>
      <td>3.043049</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>693</th>
      <td>917.900000</td>
      <td>76.802000</td>
      <td>154.100000</td>
      <td>2.550112</td>
      <td>199.400000</td>
      <td>3.400149</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>259</th>
      <td>914.830000</td>
      <td>74.570000</td>
      <td>175.500000</td>
      <td>1.409272</td>
      <td>153.800000</td>
      <td>2.236940</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>723</th>
      <td>917.010000</td>
      <td>51.836000</td>
      <td>130.200000</td>
      <td>1.610597</td>
      <td>159.900000</td>
      <td>2.348787</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>224</th>
      <td>918.710000</td>
      <td>40.460000</td>
      <td>214.500000</td>
      <td>16.128337</td>
      <td>222.400000</td>
      <td>18.275800</td>
      <td>0.000000</td>
      <td>40.000000</td>
    </tr>
    <tr>
      <th>300</th>
      <td>915.600000</td>
      <td>77.918000</td>
      <td>35.100000</td>
      <td>3.511996</td>
      <td>50.200000</td>
      <td>4.451511</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>442</th>
      <td>920.957021</td>
      <td>65.236957</td>
      <td>75.121302</td>
      <td>3.891117</td>
      <td>92.484731</td>
      <td>5.187467</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>585</th>
      <td>916.250000</td>
      <td>79.754000</td>
      <td>48.600000</td>
      <td>1.073731</td>
      <td>99.800000</td>
      <td>1.588227</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1057</th>
      <td>915.910000</td>
      <td>63.986000</td>
      <td>17.400000</td>
      <td>3.825167</td>
      <td>37.800000</td>
      <td>5.010746</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>770</th>
      <td>921.050000</td>
      <td>61.448000</td>
      <td>189.000000</td>
      <td>8.791174</td>
      <td>197.300000</td>
      <td>10.289924</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>81</th>
      <td>917.460000</td>
      <td>58.298000</td>
      <td>182.300000</td>
      <td>5.905522</td>
      <td>190.300000</td>
      <td>6.934514</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>150</th>
      <td>923.187783</td>
      <td>56.532744</td>
      <td>50.093694</td>
      <td>7.695571</td>
      <td>56.997958</td>
      <td>9.427236</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>493</th>
      <td>913.630000</td>
      <td>45.356000</td>
      <td>185.600000</td>
      <td>9.641211</td>
      <td>197.200000</td>
      <td>11.743935</td>
      <td>0.090000</td>
      <td>540.000000</td>
    </tr>
    <tr>
      <th>321</th>
      <td>921.910250</td>
      <td>53.602094</td>
      <td>47.630372</td>
      <td>12.127612</td>
      <td>65.797900</td>
      <td>15.605819</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>39</th>
      <td>921.969951</td>
      <td>60.955342</td>
      <td>164.621486</td>
      <td>1.664442</td>
      <td>195.779968</td>
      <td>2.367181</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>430</th>
      <td>914.106588</td>
      <td>73.767246</td>
      <td>219.063027</td>
      <td>1.503157</td>
      <td>124.809922</td>
      <td>2.218642</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>109</th>
      <td>923.620000</td>
      <td>62.600000</td>
      <td>63.700000</td>
      <td>4.943637</td>
      <td>75.500000</td>
      <td>6.062107</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1005</th>
      <td>919.460000</td>
      <td>71.816000</td>
      <td>56.700000</td>
      <td>8.813544</td>
      <td>74.600000</td>
      <td>11.162331</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>496</th>
      <td>919.980664</td>
      <td>64.092099</td>
      <td>51.971412</td>
      <td>22.091733</td>
      <td>73.351957</td>
      <td>27.535060</td>
      <td>0.023571</td>
      <td>125.107948</td>
    </tr>
    <tr>
      <th>472</th>
      <td>914.610000</td>
      <td>49.442000</td>
      <td>178.900000</td>
      <td>6.285801</td>
      <td>190.200000</td>
      <td>7.516118</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>720</th>
      <td>913.700000</td>
      <td>98.906000</td>
      <td>192.700000</td>
      <td>2.125093</td>
      <td>53.400000</td>
      <td>3.355410</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>888</th>
      <td>915.820000</td>
      <td>62.492000</td>
      <td>45.300000</td>
      <td>8.567480</td>
      <td>65.300000</td>
      <td>11.139961</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>269</th>
      <td>920.527759</td>
      <td>60.433369</td>
      <td>55.193833</td>
      <td>12.482793</td>
      <td>73.427852</td>
      <td>15.318982</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>32</th>
      <td>918.700000</td>
      <td>76.226000</td>
      <td>184.600000</td>
      <td>4.093600</td>
      <td>194.900000</td>
      <td>4.742313</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>465</th>
      <td>915.640000</td>
      <td>66.470000</td>
      <td>181.500000</td>
      <td>9.372779</td>
      <td>187.400000</td>
      <td>10.200446</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>236</th>
      <td>922.180000</td>
      <td>42.476000</td>
      <td>195.400000</td>
      <td>7.135839</td>
      <td>208.500000</td>
      <td>8.455633</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>148</th>
      <td>916.550000</td>
      <td>57.956000</td>
      <td>174.400000</td>
      <td>3.131716</td>
      <td>195.000000</td>
      <td>4.071231</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>263</th>
      <td>915.101901</td>
      <td>73.211670</td>
      <td>210.438988</td>
      <td>1.359570</td>
      <td>126.306814</td>
      <td>1.988785</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>250</th>
      <td>917.600000</td>
      <td>74.930000</td>
      <td>63.900000</td>
      <td>11.654457</td>
      <td>84.700000</td>
      <td>15.099345</td>
      <td>0.000000</td>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>506</th>
      <td>917.290000</td>
      <td>78.206000</td>
      <td>51.500000</td>
      <td>7.180577</td>
      <td>68.000000</td>
      <td>9.193823</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>894</th>
      <td>915.104853</td>
      <td>80.661032</td>
      <td>214.407657</td>
      <td>1.535364</td>
      <td>116.843001</td>
      <td>2.411888</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>186</th>
      <td>916.500000</td>
      <td>71.042000</td>
      <td>102.300000</td>
      <td>2.415895</td>
      <td>49.100000</td>
      <td>3.221194</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1082</th>
      <td>916.130000</td>
      <td>50.108000</td>
      <td>211.400000</td>
      <td>2.550112</td>
      <td>231.800000</td>
      <td>3.534365</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>971</th>
      <td>919.700000</td>
      <td>73.814000</td>
      <td>227.000000</td>
      <td>1.409272</td>
      <td>255.400000</td>
      <td>1.901399</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>577</th>
      <td>920.075591</td>
      <td>69.348750</td>
      <td>45.669981</td>
      <td>21.108390</td>
      <td>63.638273</td>
      <td>26.659596</td>
      <td>0.001194</td>
      <td>34.150095</td>
    </tr>
    <tr>
      <th>12</th>
      <td>917.390000</td>
      <td>49.784000</td>
      <td>204.100000</td>
      <td>1.275056</td>
      <td>211.800000</td>
      <td>2.013246</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>142</th>
      <td>921.186223</td>
      <td>71.203823</td>
      <td>214.248938</td>
      <td>1.690793</td>
      <td>173.388878</td>
      <td>2.673681</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>676</th>
      <td>914.154389</td>
      <td>81.510250</td>
      <td>125.453294</td>
      <td>2.651554</td>
      <td>141.837044</td>
      <td>3.416937</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>451</th>
      <td>918.360000</td>
      <td>56.714000</td>
      <td>49.800000</td>
      <td>1.409272</td>
      <td>85.800000</td>
      <td>2.013246</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>301</th>
      <td>913.340000</td>
      <td>57.218000</td>
      <td>215.000000</td>
      <td>3.713320</td>
      <td>224.400000</td>
      <td>4.473880</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>844</th>
      <td>921.400000</td>
      <td>75.236000</td>
      <td>60.900000</td>
      <td>4.026492</td>
      <td>76.000000</td>
      <td>4.921268</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>354</th>
      <td>922.821310</td>
      <td>67.813301</td>
      <td>55.757658</td>
      <td>9.555245</td>
      <td>68.857279</td>
      <td>11.558892</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>647</th>
      <td>918.846598</td>
      <td>74.938013</td>
      <td>185.395861</td>
      <td>3.063336</td>
      <td>189.244246</td>
      <td>3.831911</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>313</th>
      <td>916.542733</td>
      <td>76.532726</td>
      <td>174.008328</td>
      <td>3.729839</td>
      <td>184.930254</td>
      <td>4.719943</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>316</th>
      <td>917.930000</td>
      <td>48.056000</td>
      <td>258.200000</td>
      <td>2.684328</td>
      <td>287.600000</td>
      <td>3.892276</td>
      <td>0.000000</td>
      <td>40.000000</td>
    </tr>
    <tr>
      <th>419</th>
      <td>918.300000</td>
      <td>64.886000</td>
      <td>140.600000</td>
      <td>3.758059</td>
      <td>90.600000</td>
      <td>4.809421</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>740</th>
      <td>917.210000</td>
      <td>82.742000</td>
      <td>171.600000</td>
      <td>2.773806</td>
      <td>204.300000</td>
      <td>3.623843</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>687</th>
      <td>912.390000</td>
      <td>41.522000</td>
      <td>35.300000</td>
      <td>3.847537</td>
      <td>50.500000</td>
      <td>4.563358</td>
      <td>6.025000</td>
      <td>14342.000000</td>
    </tr>
    <tr>
      <th>237</th>
      <td>923.552179</td>
      <td>71.092290</td>
      <td>197.674723</td>
      <td>3.942864</td>
      <td>210.822424</td>
      <td>5.165807</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>337</th>
      <td>924.720000</td>
      <td>63.518000</td>
      <td>29.700000</td>
      <td>1.364533</td>
      <td>47.700000</td>
      <td>1.811921</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>146</th>
      <td>924.722875</td>
      <td>61.128083</td>
      <td>40.673436</td>
      <td>8.576565</td>
      <td>65.429827</td>
      <td>11.448650</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>821</th>
      <td>915.900000</td>
      <td>69.134000</td>
      <td>115.200000</td>
      <td>1.990877</td>
      <td>110.300000</td>
      <td>2.773806</td>
      <td>0.000000</td>
      <td>20.000000</td>
    </tr>
    <tr>
      <th>630</th>
      <td>921.763402</td>
      <td>66.022467</td>
      <td>73.176502</td>
      <td>2.851265</td>
      <td>93.433414</td>
      <td>3.797461</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>983</th>
      <td>921.500000</td>
      <td>62.996000</td>
      <td>74.600000</td>
      <td>5.279178</td>
      <td>90.300000</td>
      <td>6.420018</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>46</th>
      <td>917.900000</td>
      <td>65.660000</td>
      <td>183.700000</td>
      <td>6.062107</td>
      <td>188.500000</td>
      <td>6.509495</td>
      <td>0.021000</td>
      <td>319.000000</td>
    </tr>
    <tr>
      <th>116</th>
      <td>919.561333</td>
      <td>69.165521</td>
      <td>137.144876</td>
      <td>1.382894</td>
      <td>123.019031</td>
      <td>2.031607</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>799</th>
      <td>917.650000</td>
      <td>82.436000</td>
      <td>108.000000</td>
      <td>2.214571</td>
      <td>62.800000</td>
      <td>2.840914</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>350</th>
      <td>917.120000</td>
      <td>45.896000</td>
      <td>179.200000</td>
      <td>3.400149</td>
      <td>195.000000</td>
      <td>3.981753</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>279</th>
      <td>915.710000</td>
      <td>86.342000</td>
      <td>234.300000</td>
      <td>1.744813</td>
      <td>125.500000</td>
      <td>2.505373</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
<p>352 rows × 8 columns</p>
</div>




```python
prediction[:20]
```




    array([0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0])




```python
y_test[:20]
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
      <th>high_humidity_label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>456</th>
      <td>0</td>
    </tr>
    <tr>
      <th>845</th>
      <td>0</td>
    </tr>
    <tr>
      <th>693</th>
      <td>1</td>
    </tr>
    <tr>
      <th>259</th>
      <td>1</td>
    </tr>
    <tr>
      <th>723</th>
      <td>1</td>
    </tr>
    <tr>
      <th>224</th>
      <td>1</td>
    </tr>
    <tr>
      <th>300</th>
      <td>1</td>
    </tr>
    <tr>
      <th>442</th>
      <td>0</td>
    </tr>
    <tr>
      <th>585</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1057</th>
      <td>1</td>
    </tr>
    <tr>
      <th>770</th>
      <td>1</td>
    </tr>
    <tr>
      <th>81</th>
      <td>1</td>
    </tr>
    <tr>
      <th>150</th>
      <td>0</td>
    </tr>
    <tr>
      <th>493</th>
      <td>1</td>
    </tr>
    <tr>
      <th>321</th>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>0</td>
    </tr>
    <tr>
      <th>109</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1005</th>
      <td>0</td>
    </tr>
    <tr>
      <th>496</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



#### Medimos la presicion


```python
accuracy_score(y_true = y_test, y_pred = prediction)
```




    0.8153409090909091


