# import la libreria pandas
import pandas as pd
import numpy as np

#leer el archivo, asignandole a la variable "df"; como no tiene encabezado se añade (, header=None)
other_path="imports-85.data"
df=pd.read_csv(other_path, header=None)

#usamos df.head(n)para leer primeras filas y df.tail(n) para leer las ultimas filas.
#Leer las 5 primeras filas#
print(df.head(5)) 
#leer las 5 ultimas filas
print(df.tail(5))

#Encabezado
#creamos una lista de encabezados, incluyan todas las columnas en orden
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
#remplazamos los encabezados y verificamos el marco de datos
df.columns=headers
print(df.head(10))

#eliminar valores faltantes
#Necesitamos remplazar el simbolo ? con Nan para que dropna() pueda eliminar los valores faltantes.
df1=df.replace('?',np.NaN)
#Podemos eliminar los valores flatantes a lo largo de la columna "precio" asi:
df=df1.dropna(subset=["price"], axis=0)
print(df.head(20))


#encontrar el nombre de las columnas
print(df.columns)

#Guardar
df.to_csv("carrosdatos.csv")



