# Proyectos de Análisis de Datos con Python

Esta sección contiene una colección de proyectos prácticos de análisis de datos, visualización y procesamiento de información utilizando Python y librerías especializadas.

## Propósito de la Carpeta Python_datos

La carpeta `Python_datos` es un espacio dedicado a desarrollar **habilidades en ciencia de datos y análisis exploratorio (EDA)** mediante proyectos prácticos. En esta carpeta se practican:

- **Carga y limpieza de datos** desde múltiples fuentes (CSV, JSON, etc.)
- **Análisis exploratorio de datos (EDA)**
- **Visualización de datos** con librerías como Matplotlib y Seaborn
- **Estadística descriptiva** e inferencial
- **Correlaciones y relaciones** entre variables
- **Interactividad** con widgets para exploración dinámica
- **Procesamiento con Pandas** para transformación y agregación
- **Uso de Jupyter Notebooks** como herramienta principal de trabajo

---

## Proyectos

### 1. **Analisis_CO2/** *(Carpeta)*
**Objetivo:** Análisis exploratorio de emisiones de CO₂ per cápita a nivel mundial y comparativas entre países.

Esta carpeta contiene:
- **analisis_co2.ipynb:** Jupyter Notebook interactivo con múltiples visualizaciones y análisis estadístico
- **co2-emissions-per-capita.csv:** Dataset con datos reales de emisiones de CO₂
- **co2-emissions-per-capita.metadata.json:** Metadatos del dataset
- **readme.md:** Documentación completa del proyecto con insights y procesos
- **requirements.txt:** Dependencias necesarias

**Habilidades practicadas:** Carga CSV, limpieza de datos, análisis exploratorio (EDA), visualización, correlación, widgets interactivos.

---

### 2. **Analisis_serie_temporal/** *(Carpeta)*
**Objetivo:** Análisis de series temporales con datos de divisas, incluyendo suavizado con medias móviles y descomposición estacional.

Esta carpeta contiene:
- **serie_temporal.ipynb:** Jupyter Notebook con descarga de datos de yfinance, cálculo de medias móviles, gráficos de series temporales y descomposición estacional
- **requirements.txt:** Dependencias necesarias (yfinance, pandas, matplotlib, statsmodels)

**Habilidades practicadas:** Descarga de datos financieros, procesamiento de series temporales, cálculo de medias móviles, visualización de tendencias, descomposición estacional.

---

## Requisitos Generales

- Python 3.7 o superior
- Entorno virtual activado (`pythonenv`)
- Jupyter Notebook
- Librerías: pandas, matplotlib, seaborn, numpy, ipywidgets

### Dependencias

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

O instala manualmente:

```bash
pip install pandas matplotlib seaborn jupyter ipywidgets numpy
```

### Para ejecutar un Notebook:

1. Navega a la carpeta del proyecto deseado
2. Activa el entorno virtual:
   ```bash
   # En Windows
   pythonenv\Scripts\Activate.ps1
   ```
3. Abre Jupyter:
   ```bash
   jupyter notebook
   ```
4. Selecciona el archivo `.ipynb` que desees explorar
5. Ejecuta las celdas en orden (Shift + Enter) para ver los resultados y gráficos