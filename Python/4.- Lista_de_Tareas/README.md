# Lista de Tareas - Aplicación con PyQt5

Aplicación de escritorio desarrollada en Python con PyQt5 para la gestión de tareas personales.

Permite agregar, eliminar y marcar tareas como completadas, con persistencia de datos en archivo local.

---

## Tecnologías utilizadas

* Python
* PyQt5 (interfaz gráfica)
* Archivos de texto (persistencia de datos)

Dependencias definidas en `requirements.txt`.

---

## Estructura del proyecto

```
Lista_de_Tareas/
│
├── lista_tareas.py
├── tareas.txt
├── requirements.txt
```

---

## Cómo ejecutar el proyecto

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:

```bash
python lista_tareas.py
```

---

## Funcionalidades

* Agregar nuevas tareas
* Eliminar tareas seleccionadas
* Marcar tareas como completadas
* Persistencia de tareas en archivo (`tareas.txt`)
* Cambio visual de tareas completadas (tachado y color gris)

---

## Lógica de funcionamiento

Las tareas se almacenan en un archivo de texto con el siguiente formato:

```
tarea|estado
```

Ejemplo:

```
Crear programa Python|1
Probar programa|0
```

* `1` indica tarea completada
* `0` indica tarea pendiente

Al iniciar la aplicación:

* Se cargan las tareas desde el archivo
* Se reconstruye su estado visual

---

## Conceptos aplicados

* Interfaces gráficas con PyQt5
* Manejo de eventos
* Persistencia de datos en archivos
* Manipulación de listas en GUI (`QListWidget`)
* Control de estado visual
