import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QGridLayout
)

# Se crea la función para construir la calculadora, que incluye la ventana, el diseño, los botones y la caja de texto.
def crear_calculadora():
    # Se crea la ventana principal de la calculadora.
    ventana=QWidget()
    ventana.setWindowTitle('Calculadora')
    ventana.setGeometry(100, 100, 300, 400)
    # Se crea el diseño principal de la ventana, que es un diseño vertical.
    layout_principal=QVBoxLayout()

    # Se crea la caja de texto donde se mostrarán los números y resultados, y se configura para que no sea editable por el usuario.
    caja_texto=QLineEdit()
    caja_texto.setReadOnly(True)
    caja_texto.setStyleSheet('font-size:28px;')
    # Se agrega la caja de texto al diseño principal.
    layout_principal.addWidget(caja_texto)

    # Se crea un diseño de cuadrícula para organizar los botones de la calculadora.
    layout_botones=QGridLayout()
    botones=[
        ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
        ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
        ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
        ('0',3,0), ('.',3,1), ('C',3,2), ('+',3,3),
        ('=',4,0,1,4)
    ]

    # Se crean los botones de la calculadora y se agregan al diseño de cuadrícula. 
    # Cada botón se conecta a la función on_click para manejar los eventos de clic.
    # Se usa un ciclo for para iterar sobre la lista de botones, creando cada botón y agregándolo al diseño en la posición especificada.
    for texto, fila, columna, *detalle in botones:
        boton=QPushButton(texto)
        boton.setStyleSheet('font-size:18px')
        # Se crea la condición para verificar si el botón tiene detalles adicionales (como el botón "=" que ocupa varias columnas) 
        # y se agrega al diseño de cuadrícula en consecuencia.
        if detalle:
            layout_botones.addWidget(boton, fila, columna, *detalle)
        else:
            layout_botones.addWidget(boton, fila, columna)
        # Se conecta el evento de clic del botón a la función on_click, pasando el texto del botón y la caja de texto como argumentos.
        boton.clicked.connect(lambda _, t=texto : on_click(t, caja_texto))

    # Se agrega el diseño de botones al diseño principal y se establece el diseño de la ventana. Finalmente, se muestra la ventana. 
    layout_principal.addLayout(layout_botones)
    ventana.setLayout(layout_principal)
    ventana.show()
    return ventana

# Se crea la función on_click para manejar los eventos de clic en los botones de la calculadora. 
# Esta función toma el texto del botón y la caja de texto como argumentos.
def on_click(texto, caja_texto_objet):
    # Se crea una condición para verificar si el botón presionado es "C" (limpiar), 
    # "=" (calcular el resultado) o cualquier otro botón (número o operador).
    if texto=='C':
        caja_texto_objet.clear()
    elif texto=='=':
        # Se usa la función eval para evaluar la expresión matemática ingresada en la caja de texto.
        try:
            resultado=eval(caja_texto_objet.text())
            caja_texto_objet.setText(str(resultado))
        # Se maneja cualquier excepción que pueda ocurrir durante la evaluación de la expresión, mostrando un mensaje de error en la caja de texto.
        except Exception:
            caja_texto_objet.setText('Error en el calculo')
    # Si el botón presionado es un número o un operador, se agrega su texto a la caja de texto.
    else:
        caja_texto_objet.setText(caja_texto_objet.text()+texto)
    
# Se crea la aplicacion
app = QApplication(sys.argv)
# Se llama a la función crear_calculadora para construir y mostrar la ventana de la calculadora.
ventana = crear_calculadora()
# Por ultimo, se usa exit para el cierre correcto de la aplicación cuando se cierra la ventana de la calculadora.
sys.exit(app.exec_())
