import pandas as pd

data_personas = pd.read_excel('datos.xlsx')


""" 
1. La columna ID tiene que ser transformada 
a la primera letra del nombre y ls ultima,
concatenadi con su valor numerico.
Ejemplo: JZ1
"""
# Se selecciona la columna Id dentro de los corchetes que es la columna en la que se trabjara.
# Despues, en la primer linea, se obtiene la primer letra del nombre en mayuscula.
# Despues se obtiene la ultima letra del apellido. en mayuscula.
# Por ultimo, se obtiene el numero del Id.
# Los signos + hacen que se concatenen los valores y los \ sirven para poder dividir el codigo en lineas para que sea mas legible.

data_personas['Id'] = data_personas['Nombre'].astype(str).str.upper().str[0] +\
                      data_personas['Nombre'].astype(str).str.upper().str[-1] +\
                      data_personas['Id'].astype(str)



""" 
2. La columna nombre debe tener el nombre y apellido
comenzando con mayuscula.
Ejemplo: Juan Perez.
"""
# Se selecciona la columna Nombre dentro de los corchetes.
# Despues se convierten los datos de la columna en cadenas de texto con astype.
# Por ultimo, se usa title() para convertir en mayusculas todas las iniciales de cada palabra. 

data_personas['Nombre'] = data_personas['Nombre'].astype(str).str.title()


""" 
3. La columna profesor debe estar con todo el texto en mayusculas.
"""
# Con upper(), se combierte en mayusculas todo el texto dentro de las filas de la columna Profesion.

data_personas['Profesion'] = data_personas['Profesion'].astype(str).str.upper()

""" 
4. Crear una nueva columna 'Total' despues de sueldo,
que conndra el sueldo menos el impuesto (20% del sueldo).
Ejemplo: 200 - 40 = 160.
"""
# Se selecciona la columna Total, en este caso, al no existir dicha columna, se crea una nueva al final de la tabla.
# Despues, al sueldo se le resta el resultado de la multiplicacion de sueldo por el 20%, que es 0.2.

data_personas['Total'] = data_personas['Sueldo'] - data_personas['Sueldo']*0.2

"""
5. Crear una nueva columna que se llame Indice,
sera una columna autogenerada numerica y secuencial.
Y se debe ubicar como la primer columna, antes del ID.
Ejemplo: 1-Juan Perez, 5 - Domingo Masias.
"""
# En la primer linea se crea un indice desde con range que comienza desde 1 y va sumando uno hasta terminar cada linea de las columnas existentes.
# En la segunda linea se ordenan las columnas de la manera en que nosotros querramos.

data_personas['Indice'] = range(1, len(data_personas)+1)
data_personas = data_personas [['Indice', 'Id', 'Nombre', 'Profesion', 'Sueldo', 'Total']]

# Se crea el nuevo archivo de excel en donde se guardaran todos los cambios que se realizaron en cada tarea.
data_personas.to_excel('excel_procesado.xlsx', index=False)

# Se imprime en consola la tabla con los cambios hechos.
print(data_personas.head())