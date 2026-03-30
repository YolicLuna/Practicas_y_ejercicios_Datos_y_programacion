# Registro de Empleados - Aplicación con PyQt5

Aplicación de escritorio desarrollada en Python utilizando PyQt5 para el registro y gestión de empleados.
Permite ingresar datos, visualizar información en una tabla y exportar los registros a un archivo Excel.

---

## Tecnologías utilizadas
* Python.
* PyQt5 (interfaz gráfica).
* Pandas (gestión de datos).
* OpenPyXL (exportación a Excel).

---

## Estructura del proyecto
```id="tree01"
formulario/
│
├── formulario.py        # Aplicación principal
├── data_empleados.xlsx  # Archivo generado (salida)
├── requirements.txt     # Dependencias
```

---

## Cómo ejecutar el proyecto
1. Instala las dependencias:
```bash id="cmd3"
pip install -r requirements.txt
```

2. Ejecuta la aplicación:
```bash id="cmd4"
python formulario.py
```

---

## Funcionalidades
* Registro de empleados con:
  * Nombre.
  * Apellido.
  * Profesión.
  * Sueldo.
* Visualización en tabla interactiva.
* Cálculo automático de sueldo neto.
* Exportación de datos a Excel.
* Limpieza automática de campos tras cada registro.

---

## Lógica de negocio
El cálculo del sueldo neto se realiza según el rango salarial:
* Sueldo entre 0 y 100 → 20% de descuento.
* Sueldo entre 1000 y 4000 → 25% de descuento.
* Otros casos → 35% de descuento.

---

## Conceptos aplicados
Este proyecto demuestra:
* Creación de interfaces gráficas con PyQt5.
* Manejo de layouts (`QVBoxLayout`, `QHBoxLayout`).
* Uso de widgets (`QLineEdit`, `QPushButton`, `QTableWidget`).
* Manejo de eventos (botones y acciones).
* Manipulación de datos con Pandas.
* Sincronización entre GUI y DataFrame.
* Exportación de datos a Excel.

---

## Dependencias
Definidas en `requirements.txt` :
* pandas.
* PyQt5.
* openpyxl.

---

## Funcionamiento interno
El flujo principal del sistema se encuentra en el archivo :
1. El usuario ingresa datos en el formulario.
2. Se calcula el sueldo neto automáticamente.
3. Los datos se almacenan en un DataFrame.
4. Se muestran en la tabla de la interfaz.
5. Opcionalmente se exportan a un archivo Excel.

---

## Enfoque del proyecto

Este proyecto combina:

* Interfaz gráfica (frontend de escritorio).
* Lógica de negocio (cálculos).
* Manejo de datos (tipo mini sistema CRUD).

Simula un sistema básico de gestión de empleados.