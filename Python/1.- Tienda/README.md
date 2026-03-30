# Tienda - Aplicación con Streamlit

Aplicación web interactiva desarrollada en Python con Streamlit para simular la compra de productos en una tienda de alimentos congelados.
Permite agregar productos, calcular subtotales y obtener el total de la compra en tiempo real.

---

## Tecnologías utilizadas

* Python.
* Streamlit.
* Pandas.

---

## Cómo ejecutar el proyecto
1. Clona el repositorio o descarga los archivos.

2. Instala las dependencias:
```bash
pip install streamlit pandas
```

3. Ejecuta la aplicación:
```bash
streamlit run tienda.py
```

---

## 📌 Funcionalidades
* Agregar productos con nombre, precio y cantidad.
* Cálculo automático de subtotal por producto.
* Visualización de los productos en una tabla dinámica.
* Cálculo del total de la compra.
* Persistencia temporal de datos usando `st.session_state`.

---

##  Conceptos aplicados
Este proyecto, aunque pequeño, demuestra conceptos importantes:
* Manejo de estado en aplicaciones web (`session_state`).
* Uso de formularios en Streamlit (`st.form`).
* Manipulación de datos con Pandas (`DataFrame`, `concat`).
* Separación básica de lógica mediante funciones.
* Interacción usuario-interfaz en tiempo real.
