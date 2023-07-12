import numpy as np
import pandas as pd
arr = np.array(["b", "a"] )
print(arr.dtype)


np.array([1, 2, 3], dtype='S' )
#'i' = integer (entero)
#'b' = booleano
#'f' = flotante
#'M' = datetime
#'O' = objeto
#'S' = string (cadena)
print(arr)

arr= np.array([1.1,2.1,3.1])
print("pre", arr)
nuevo_arr = arr.astype('i')
print(nuevo_arr)

#copy - es copia tal cual
#view - es una vista en tiempo real
#concatenate - uno los arreglos
#arr3 = np.concatenate((arrl, arr2))

arr = np.array([1, 2, 3,4,5])
x = np.where(arr==5)
print(x)
#where - posicion donde esta ese dato

#sort - ordena el arreglo
df = pd.read_csv("Perfil de estudiante.csv")
print(df.to_string() )

#df = pd.read_json("dataset.json")
#print(df.to_string() )
