import streamlit as st
import pandas as pd


def calcular_subtotal(nombre_producto, precio_producto, cantidad_producto):
    subtotal=float(precio_producto)*float(cantidad_producto)
    nueva_fila={
        'Producto':nombre_producto, 
        'Precio':precio_producto, 
        'Cantidad':cantidad_producto,
        'Subtotal': subtotal
        }
    
    st.session_state.table_data=pd.concat(
                [st.session_state.table_data,
                pd.DataFrame([nueva_fila])],
                ignore_index=True
        )

if 'table_data' not in st.session_state:
    st.session_state.table_data=pd.DataFrame(
                        columns=['Producto', 'Precio', 'Cantidad', 'Subtotal']
                        )

st.title('Alimentos congelados RIAZ.')

with st.form('Producto_form'):
    producto_nombre=st.text_input('Ingrese el nombre del producto')
    producto_precio=st.number_input('Ingrese el precio del producto')
    producto_cantidad=st.number_input('Ingrese la cantidad de productos')

    subtotal_button=st.form_submit_button('Comprar Productos')

if subtotal_button:
    calcular_subtotal(producto_nombre, producto_precio, producto_cantidad)

st.dataframe(st.session_state.table_data)

if st.button('Calcular Total'):
    total=(st.session_state.table_data['Precio']
            *st.session_state.table_data['Cantidad']).sum()
    
    st.write('El precio total es: ' + str(total))