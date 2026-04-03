# Calculadora con PyQt5

Proyecto de una calculadora interactiva con interfaz gráfica desarrollada utilizando PyQt5. Implementa operaciones matemáticas básicas mediante una interfaz visual intuitiva.

---

## Objetivo
Crear una aplicación de escritorio funcional que:
* Realice operaciones matemáticas básicas.
* Proporcione una interfaz gráfica amigable e intuitiva.
* Maneje errores en cálculos inválidos.
* Permita limpiar el contenido y realizar nuevos cálculos.

---

## Características principales
* Operaciones soportadas: suma (+), resta (-), multiplicación (*), división (/).
* Botón de punto decimal (.) para números decimales.
* Botón "C" para limpiar la pantalla.
* Botón "=" para calcular el resultado.
* Interfaz organizada en cuadrícula (grid layout).
* Manejo de excepciones para cálculos inválidos.
* Pantalla de solo lectura para mostrar números y resultados.

---

## Tecnologías utilizadas
* Python.
* PyQt5.

Dependencias definidas en `requirements.txt`

---

## Cómo funciona

### Estructura de la aplicación
1. **Ventana principal:** Creada con `QWidget`, tamaño de 300x400 píxeles.
2. **Caja de texto:** Muestra números ingresados y resultados de operaciones.
3. **Botones:** Organizados en una cuadrícula 5x4 para fácil acceso.
4. **Event handlers:** Función `on_click()` maneja todos los eventos de clic.

### Funcionalidades
* **Entrada de números y operadores:** Los botones agregan caracteres a la caja de texto.
* **Limpiar (C):** Vacía la caja de texto.
* **Calcular (=):** Evalúa la expresión matemática ingresada usando `eval()`.
* **Manejo de errores:** Muestra "Error en el calculo" si la expresión es inválida.

---

## Conceptos aplicados
* Interfaz gráfica de usuario (GUI).
* Layouts y widgets en PyQt5.
* Eventos y slots.
* Manejo de excepciones.
* Expresiones matemáticas con `eval()`.
* Estilos CSS en Qt.

---

## Cómo ejecutar

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:

```bash
python calculadora.py
```

3. Usar la calculadora:
   * Haz clic en los números y operadores.
   * Presiona "=" para calcular el resultado.
   * Usa "C" para limpiar la pantalla.

---

## Composición de la calculadora

| Fila | Columna 1 | Columna 2 | Columna 3 | Columna 4 |
|------|-----------|-----------|-----------|-----------|
| 1    | 7         | 8         | 9         | /         |
| 2    | 4         | 5         | 6         | *         |
| 3    | 1         | 2         | 3         | -         |
| 4    | 0         | .         | C         | +         |
| 5    | = (ocupa todas las columnas) |

---

## Enfoque del proyecto
Este proyecto se enfoca en:
* Desarrollo de aplicaciones GUI con Python.
* Interacción con usuarios mediante interfaces gráficas.
* Gestión de eventos en aplicaciones de escritorio.
* Validación y manejo de errores en cálculos.
