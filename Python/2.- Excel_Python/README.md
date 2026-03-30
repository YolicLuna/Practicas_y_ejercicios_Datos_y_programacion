# Transformación de Datos con Python y Pandas

Proyecto de procesamiento y transformación de datos a partir de un archivo Excel utilizando Python y Pandas.
El objetivo es limpiar, transformar y enriquecer los datos para generar un nuevo archivo estructurado listo para análisis.

---

## Tecnologías utilizadas
* Python.
* Pandas.
* OpenPyXL.

---

## Estructura del proyecto

```
excel_python/
│
├── excel_python.py        # Script principal de transformación
├── datos.xlsx            # Archivo de entrada
├── excel_procesado.xlsx  # Archivo de salida generado
├── requirements.txt      # Dependencias del proyecto
```

---

## Cómo ejecutar el proyecto

1. Instala las dependencias:
```bash id="cmd1"
pip install -r requirements.txt
```

2. Ejecuta el script:
```bash id="cmd2"
python excel_python.py
```

---

## Transformaciones realizadas
El script realiza las siguientes operaciones sobre los datos:

### 1. Transformación del ID
Se genera un nuevo ID combinando:
* Primera letra del nombre.
* Última letra del nombre.
* ID numérico original.
Ejemplo:
```
Juan → JN1
```

---

### 2. Formato del nombre
Los nombres se convierten a formato título:
```
juan perez → Juan Perez
```

---

### 3. Normalización de profesión
Todas las profesiones se convierten a mayúsculas:
```
ingeniero → INGENIERO
```

---

### 4. Cálculo de sueldo neto
Se crea una nueva columna `Total`:
```
Total = Sueldo - (Sueldo * 0.2)
```

---

### 5. Creación de índice
Se agrega una columna `Indice`:
* Secuencial (1, 2, 3…).
* Ubicada como primera columna.

---

## Conceptos aplicados
Este proyecto demuestra:
* Manipulación de datos con Pandas.
* Uso de operaciones vectorizadas.
* Limpieza y normalización de datos.
* Creación y reordenamiento de columnas.
* Generación de archivos Excel procesados.
* Uso de `astype`, `str`, `upper`, `title`.

---

## Dependencias
Definidas en `requirements.txt` :
* pandas.
* openpyxl.

---

## Entrada y salida
* Entrada: archivo Excel (`datos.xlsx`).
* Salida: archivo Excel transformado (`excel_procesado.xlsx`).

---

## Enfoque del proyecto

Este proyecto simula un proceso básico de ETL (Extract, Transform, Load), donde:
* **Extract**: lectura de archivo Excel.
* **Transform**: limpieza y transformación de datos.
* **Load**: generación de nuevo archivo procesado.
