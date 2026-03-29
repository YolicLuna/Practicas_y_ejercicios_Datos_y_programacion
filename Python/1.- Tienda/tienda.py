import streamlit as st
import pandas as pd

# Se crea una función para calcular el subtotal de cada producto y agregarlo a la tabla de datos.
def calcular_subtotal(nombre_producto, precio_producto, cantidad_producto):
    subtotal=float(precio_producto)*float(cantidad_producto)
    nueva_fila={
        'Producto':nombre_producto, 
        'Precio':precio_producto, 
        'Cantidad':cantidad_producto,
        'Subtotal': subtotal
        }
    # Se agrega la nueva fila a la tabla de datos utilizando pd.concat para evitar el error de append.
    st.session_state.table_data=pd.concat(
                [st.session_state.table_data,
                pd.DataFrame([nueva_fila])],
                ignore_index=True
        )

# Se inicializa la tabla de datos en el estado de sesión si no existe, con las columnas necesarias para almacenar la información de los productos.
if 'table_data' not in st.session_state:
    st.session_state.table_data=pd.DataFrame(
                        columns=['Producto', 'Precio', 'Cantidad', 'Subtotal']
                        )

# Con st.title se muestra el título de la aplicación en la interfaz de usuario.
st.title('Alimentos congelados RIAZ.')

# Se crea un formulario para ingresar los datos del producto, incluyendo el nombre, precio y cantidad. 
# Al enviar el formulario, se llama a la función calcular_subtotal para procesar los datos ingresados.
with st.form('Producto_form'):
    producto_nombre=st.text_input('Ingrese el nombre del producto')
    producto_precio=st.number_input('Ingrese el precio del producto')
    producto_cantidad=st.number_input('Ingrese la cantidad de productos')

    subtotal_button=st.form_submit_button('Comprar Productos')

# Se crea un botón para calcular el subtotal de cada producto ingresado, que llama a la función calcular_subtotal con los datos del producto ingresados en el formulario. 
# El resultado se agrega a la tabla de datos en el estado de sesión.
if subtotal_button:
    calcular_subtotal(producto_nombre, producto_precio, producto_cantidad)

# Se muestra la tabla de datos actualizada con los productos ingresados utilizando st.dataframe.
st.dataframe(st.session_state.table_data)

# Se crea un botón para calcular el total de la compra, que suma los subtotales de todos los productos ingresados en la tabla de datos y muestra el resultado en la interfaz de usuario.
if st.button('Calcular Total'):
    total=(st.session_state.table_data['Precio']
            *st.session_state.table_data['Cantidad']).sum()
    # Se muestra el precio total de la compra utilizando st.write.
    st.write('El precio total es: ' + str(total))