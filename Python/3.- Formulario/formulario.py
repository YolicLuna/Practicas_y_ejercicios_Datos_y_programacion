import pandas as pd
import sys
import os

# Importamos varias clases de PyQt5 para crear la interfaz gráfica de usuario (GUI).
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
)

# Creamos un DataFrame vacío con las columnas necesarias para almacenar los datos de los empleados.
df = pd.DataFrame(
    columns=['Nombre', 'Apellido', 'Profesion', 'Sueldo', 'Sueldo Neto']
    )

# Creamos una función para configurar y mostrar la aplicación GUI. 
# Esta función se encargará de crear la ventana principal, los campos de entrada, 
# los botones y la tabla para mostrar los datos de los empleados.
def crear_app():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle('Registro de Empleados')
    ventana.resize(800,600)

    # Creamos un diseño vertical para organizar los elementos de la interfaz de manera ordenada.
    layout_principal = QVBoxLayout()
    # Agregamos un espacio vertical al diseño principal para mejorar la apariencia de la interfaz.
    layout_principal.addSpacing(30)

    # Creamos un diseño horizontal para organizar los campos de entrada en una sola fila.
    layout_formulario = QHBoxLayout()

    # Creamos campos de entrada para el nombre, apellido, profesión y sueldo del empleado.
    nombre_input = QLineEdit()
    nombre_input.setFixedHeight(40)
    nombre_input.setPlaceholderText('Nombre')
    layout_formulario.addWidget(nombre_input)

    apellido_input = QLineEdit()
    apellido_input.setFixedHeight(40)
    apellido_input.setPlaceholderText('Apellido')
    layout_formulario.addWidget(apellido_input)

    profesion_input = QLineEdit()
    profesion_input.setFixedHeight(40)
    profesion_input.setPlaceholderText('Profesion')
    layout_formulario.addWidget(profesion_input)

    sueldo_input = QLineEdit()
    sueldo_input.setFixedHeight(40)
    sueldo_input.setPlaceholderText('Sueldo')
    layout_formulario.addWidget(sueldo_input)

    # Agregamos el diseño del formulario al diseño principal para que se muestre en la ventana.
    layout_principal.addLayout(layout_formulario)

    # Creamos otro diseño horizontal para organizar los botones de agregar y exportar en una sola fila.
    layout_botones = QHBoxLayout()

    # Creamos un botón para agregar los datos del empleado a la tabla y al DataFrame.
    boton_agregar = QPushButton('Agregar')
    boton_agregar.setFixedHeight(40)
    layout_botones.addWidget(boton_agregar)

    boton_exportar =QPushButton('Exportar_Excel')
    boton_exportar.setFixedHeight(40)
    layout_botones.addWidget(boton_exportar)

    # Agregamos el diseño de los botones al diseño principal para que se muestre debajo del formulario.
    layout_principal.addLayout(layout_botones)

    # Creamos una tabla para mostrar los datos de los empleados registrados. 
    # Configuramos el número de columnas y las etiquetas de los encabezados.
    tabla = QTableWidget()
    tabla.setColumnCount(5)
    tabla.setHorizontalHeaderLabels(
        ['Nombre', 'Apellido', 'Profesion', 'Sueldo', 'Sueldo Neto']
        )
    tabla.horizontalHeader().setStretchLastSection(True)
    tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # Agregamos la tabla al diseño principal para que se muestre debajo de los botones.
    layout_principal.addWidget(tabla)

    # Establecemos el diseño principal en la ventana y mostramos la ventana al usuario.
    ventana.setLayout(layout_principal)
    ventana.show()

    # Definimos una función para agregar los datos del empleado a la tabla y al DataFrame.
    def agregar_datos():
        nombre = nombre_input.text()
        apellido = apellido_input.text()
        profesion = profesion_input.text()
        sueldo = float(sueldo_input.text())

        # Calculamos el sueldo neto aplicando diferentes descuentos según el rango del sueldo bruto.
        if sueldo > 0 and sueldo <= 100:
            sueldo_neto = sueldo * 0.8
        elif sueldo > 1000 and sueldo <=4000:
            sueldo_neto = sueldo * 0.75
        else:
            sueldo_neto = sueldo * 0.65

        # Creamos un diccionario con los datos del nuevo empleado para agregarlo al DataFrame.
        nueva_fila = {
            'Nombre': nombre,
            'Apellido': apellido,
            'Profesion': profesion,
            'Sueldo': sueldo,
            'Sueldo Neto': sueldo_neto
            }
        
        # Agregamos la nueva fila al DataFrame utilizando el método loc para asignar los valores a la última fila disponible.
        global df
        df.loc[len(df)] = nueva_fila

        # Agregamos una nueva fila a la tabla para mostrar los datos del nuevo empleado.
        fila = tabla.rowCount()
        tabla.insertRow(fila)
        tabla.setItem(fila, 0, QTableWidgetItem(nombre))
        tabla.setItem(fila, 1, QTableWidgetItem(apellido))
        tabla.setItem(fila, 2, QTableWidgetItem(profesion))
        tabla.setItem(fila, 3, QTableWidgetItem(f'{sueldo:.2f}'))
        tabla.setItem(fila, 4, QTableWidgetItem(f'{sueldo_neto:.2f}'))

        # Ajustamos el tamaño de las filas para que se ajusten al contenido y mejoren la apariencia de la tabla.
        tabla.resizeRowsToContents()

        # Limpiamos los campos de entrada después de agregar los datos para que el usuario pueda ingresar nuevos datos fácilmente.
        nombre_input.clear()
        apellido_input.clear()
        profesion_input.clear()
        sueldo_input.clear()

    # Definimos una función para exportar los datos del DataFrame a un archivo Excel.   
    def exportar_excel():
        if os.path.exists('data_empleados.xlsx'):
            os.remove('data_empleados.xlsx')
        
        # Exportamos el DataFrame a un archivo Excel utilizando el método to_excel de pandas.
        df.to_excel('data_empleados.xlsx', index=False, engine='openpyxl')

    # Conectamos las funciones de agregar datos y exportar a los botones correspondientes 
    # para que se ejecuten cuando el usuario haga clic en ellos.
    boton_exportar.clicked.connect(exportar_excel)
    boton_agregar.clicked.connect(agregar_datos)
    sys.exit(app.exec_())

# Llamamos a la función crear_app para iniciar la aplicación GUI.
crear_app()
