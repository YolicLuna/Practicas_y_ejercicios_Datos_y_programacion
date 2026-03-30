import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QLineEdit, QMessageBox, QHBoxLayout,
    QListWidgetItem
)
from PyQt5.QtGui import QFont, QBrush, QColor


# Creamos una variable para almacenar el nombre del archivo donde se guardarán las tareas.
archivo = 'tareas.txt'


# Función para cargar las tareas desde el archivo al iniciar la aplicación.
def cargar_tareas():
    # Verificamos si el archivo existe antes de intentar leerlo.
    if os.path.exists(archivo):
        # Abrimos el archivo en modo lectura.
        with open(archivo, 'r', encoding='utf-8') as contenido_archivo:
            # Leemos cada línea del archivo, que representa una tarea, y la separamos en el texto de la tarea y su estado (completada o no).
            for linea in contenido_archivo:
                tarea, estado_tarea = linea.strip().split('|')
                elemento_lista = crar_elemento_lista_widget(
                    tarea, 
                    estado_tarea=='1'
                )
                # Agregamos el elemento de lista a la QListWidget que muestra las tareas.
                lista_tareas.addItem(elemento_lista)


# Función para crear un elemento de lista con el formato adecuado según si la tarea está completada o no.
def crar_elemento_lista_widget(texto, completado = False):
    elemento_lista = QListWidgetItem(texto)
    fuente = QFont()
    fuente.setStrikeOut(completado)
    elemento_lista.setFont(fuente)
    # Si la tarea está completada, cambiamos el color del texto a gris para indicar visualmente que ya fue realizada.
    if completado:
        elemento_lista.setForeground(QBrush(QColor('gray')))
    return elemento_lista


# Función para agregar una nueva tarea a la lista y guardarla en el archivo.
def agregar_tarea():
    # Obtenemos el texto ingresado por el usuario en el QLineEdit y eliminamos los espacios en blanco al inicio y al final.
    texto = tareas_input_text.text().strip()
    # Verificamos que el texto no esté vacío antes de agregar la tarea a la lista.
    if texto:
        elemento_lista = crar_elemento_lista_widget(texto)
        lista_tareas.addItem(elemento_lista)
        tareas_input_text.clear()
        guardar_tareas()
    # Si el usuario intenta agregar una tarea sin escribir nada, mostramos un mensaje de advertencia.
    else:
        QMessageBox.warning(ventana, 'Advertencia', 'Escribe una tarea')


# Función para guardar las tareas actuales en la QListWidget al archivo, incluyendo su estado de completado.
def guardar_tareas():
    # Abrimos el archivo en modo escritura para sobrescribir su contenido con las tareas actuales.
    with open(archivo, 'w', encoding='utf-8') as texto_archivo:
        # Recorremos cada elemento de la QListWidget para obtener su texto y estado de completado, y los escribimos en el archivo separados por un delimitador '|'.
        for elemento_lista_indice in range(lista_tareas.count()):
            elemento_lista = lista_tareas.item(elemento_lista_indice)
            texto = elemento_lista.text()
            # Verificamos si la tarea está completada utilizando el método strikeOut() de la fuente del elemento de lista, y asignamos '1' para completada y '0' para no completada.
            tarea_completada = '1' if elemento_lista.font().strikeOut() else '0'
            # Escribimos el texto de la tarea y su estado en el archivo, separados por un delimitador '|', para poder cargarlos correctamente al iniciar la aplicación.
            texto_archivo.write(f'{texto}|{tarea_completada}\n')


# Función para eliminar la tarea seleccionada en la QListWidget y actualizar el archivo con las tareas restantes.
def eliminar_tarea():
    # Obtenemos el elemento de lista actualmente seleccionado por el usuario en la QListWidget.
    elemento_lista = lista_tareas.currentItem()
    # Verificamos que el usuario haya seleccionado una tarea antes de intentar eliminarla.
    if elemento_lista:
        indice_elemento_lista = lista_tareas.row(elemento_lista)
        lista_tareas.takeItem(indice_elemento_lista)
        guardar_tareas()
    else:
        QMessageBox.warning(ventana, 'Advertencia', 'Selecciona una tarea')

# Función para marcar una tarea como completada o no completada al hacer clic en el botón correspondiente, 
# y actualizar su apariencia y el archivo con su nuevo estado.
def completar_tarea():
    # Obtenemos el elemento de lista actualmente seleccionado por el usuario en la QListWidget.
    elemento_lista = lista_tareas.currentItem()
    # Verificamos que el usuario haya seleccionado una tarea antes de intentar marcarla como completada o no completada.
    if elemento_lista:
        fuente = elemento_lista.font()
        completado = not fuente.strikeOut()
        fuente.setStrikeOut(completado)
        elemento_lista.setFont(fuente)
        # Si la tarea está completada, cambiamos el color del texto a gris para indicar visualmente que ya fue realizada, 
        # de lo contrario, lo dejamos en negro para indicar que aún no se ha completado.
        elemento_lista.setForeground(
            QBrush(QColor('gray')
                   if completado 
                   else QColor('black')
                )
        )
        guardar_tareas()
    else:
        QMessageBox.warning(ventana, 'Advertencia', 'Selecciona una tarea')

# Se crea la aplicación y la ventana principal.
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle('Lista de Tareas')
ventana.setGeometry(100, 100, 400, 500)

# Se crea el diseño principal.
layout_principal = QVBoxLayout()

# Se crea el campo de entrada para las tareas.
tareas_input_text = QLineEdit()
tareas_input_text.setPlaceholderText('Escribe una nueva tarea...')
layout_principal.addWidget(tareas_input_text)

# Se crean los botones para gestionar las tareas.
botones_layout = QHBoxLayout()

btn_agregar = QPushButton('Agregar')
btn_agregar.clicked.connect(agregar_tarea)
botones_layout.addWidget(btn_agregar)

btn_eliminar = QPushButton('Eliminar')
btn_eliminar.clicked.connect(eliminar_tarea)
botones_layout.addWidget(btn_eliminar)

btn_completar = QPushButton('Completar Tarea')
btn_completar.clicked.connect(completar_tarea)
botones_layout.addWidget(btn_completar)

# Se agrega el diseño de los botones al diseño principal.
layout_principal.addLayout(botones_layout)

# Se crea la QListWidget para mostrar las tareas y se agrega al diseño principal.
lista_tareas = QListWidget()
layout_principal.addWidget(lista_tareas)

# Se establece el diseño principal en la ventana.
ventana.setLayout(layout_principal)

# Se cargan las tareas desde el archivo al iniciar la aplicación para mostrar las tareas previamente guardadas.
cargar_tareas()
# Se muestra la ventana y se inicia el bucle de eventos de la aplicación.
ventana.show()
# Se asegura de que la aplicación se cierre correctamente al salir del bucle de eventos.
sys.exit(app.exec_())
