# Reporte de Pruebas — DSL Cocosette (Organizado por Cortes)

## 1. Alcance de las Pruebas

El presente reporte consolida las pruebas de validación sintáctica, ejecución semántica y regresión para los tres cortes académicos del lenguaje Cocosette. Los ejemplos se encuentran organizados estrictamente por corte y clasifican sus casos en **válidos** e **inválidos**:

* **Corte I** (`ejemplos/corte1/`): Especificación léxica y sintáctica, variables, expresiones aritméticas y lógicas, tipos básicos e impresión.
* **Corte II** (`ejemplos/corte2/`): Procesamiento de datos tabulares (`Tabla`), pipelines (`|>`), estructuras de control (`mientras`), funciones de usuario y exportación CSV.
* **Corte III** (`ejemplos/corte3/`): Modelos de Machine Learning (Regresión lineal, polinomial y perceptrón/XOR), evaluación con `calcular`, variables contextuales `x`/`y` y graficación nativa PNG (barras, histograma, dispersión y líneas).

Comando de validación automatizada:
```bash
make validar
```

---

## 2. Corte I — Front-end Léxico/Sintáctico y Expresiones

### Ejemplos Válidos (`ejemplos/corte1/validos/`)
| Archivo | Funcionalidad Evaluada | Resultado |
| :--- | :--- | :--- |
| `01_expresiones_basicas.coco` | Precedencia de operadores aritméticos (`+`, `*`, `^`), booleanos y lógicos (`&&`, `\|\|`, `!`). | **[VALIDO]** Ejecución exitosa. |
| `02_aritmetica_e_impresion.coco` | Operaciones aritméticas completas (`%`, `/`), variables locales y sentencias `imprimir`. | **[VALIDO]** Ejecución exitosa. |
| `03_asignaciones_y_tipos.coco` | Asignación y reasignación de cadenas, enteros, números decimales y booleanos. | **[VALIDO]** Ejecución exitosa. |

### Casos Inválidos (`ejemplos/corte1/invalidos/`)
| Archivo | Tipo de Error | Diagnóstico Capturado | Estado |
| :--- | :--- | :--- | :--- |
| `01_error_lexico_cadena_sin_cerrar.coco` | Léxico | Comilla de cierre faltante en cadena de texto. | **[RECHAZADO]** Error léxico con línea y columna. |
| `02_error_sintactico_falta_punto_coma.coco` | Sintáctico | Sentencia sin terminador obligatorio `;`. | **[RECHAZADO]** Error sintáctico reportado. |
| `03_error_palabra_reservada_como_identificador.coco` | Sintáctico/Léxico | Uso de palabra reservada (`graficar`, `cargar`) como variable. | **[RECHAZADO]** Conflicto de tokens reservado. |

---

## 3. Corte II — Procesamiento Tabular, Pipelines y Control

### Ejemplos Válidos (`ejemplos/corte2/validos/`)
| Archivo | Funcionalidad Evaluada | Resultado |
| :--- | :--- | :--- |
| `01_carga_y_pipeline.coco` | Carga de CSV (`ventas.csv`), proyección (`seleccionar`) y filtrado (`filtrar donde`). | **[VALIDO]** Ejecución exitosa. |
| `02_operaciones_corte2.coco` | Pipeline completo: limpieza, columnas calculadas, ordenamiento, renombrado, agrupamiento, resumen y exportación CSV. | **[VALIDO]** Ejecución exitosa. |
| `03_bucle_mientras.coco` | Estructuras de repetición `mientras` con condición lógica y acumulador. | **[VALIDO]** Ejecución exitosa. |
| `04_funciones.coco` | Definición de funciones (`funcion`), parámetros múltiples y retorno de valores (`retornar`). | **[VALIDO]** Ejecución exitosa. |

### Casos Inválidos (`ejemplos/corte2/invalidos/`)
| Archivo | Tipo de Error | Diagnóstico Capturado | Estado |
| :--- | :--- | :--- | :--- |
| `01_error_semantico_variable_no_declarada.coco` | Semántico | Uso de variable no definida dentro de un pipeline de filtrado. | **[RECHAZADO]** Error semántico en ejecución. |
| `02_error_semantico_division_por_cero.coco` | Semántico | Operación de división con denominador 0. | **[RECHAZADO]** Error semántico de división por cero. |
| `03_error_semantico_columna_inexistente.coco` | Semántico | Proyección de columna que no existe en el archivo CSV. | **[RECHAZADO]** Error semántico de columna inválida. |

---

## 4. Corte III — Machine Learning, Graficación PNG y Contexto

### Ejemplos Válidos (`ejemplos/corte3/validos/`)
| Archivo | Funcionalidad Evaluada | Resultado |
| :--- | :--- | :--- |
| `01_regresion_lineal.coco` | Regresión lineal (The Square Trick / OLS), ecuación aprendida y predicción con `calcular`. | **[VALIDO]** Ejecución exitosa. |
| `02_regresion_polinomial.coco` | Ajuste parabólico de grado 2 (`curva.csv`) y estimación cuadrática con `calcular`. | **[VALIDO]** Ejecución exitosa. |
| `03_perceptron_y_xor.coco` | Perceptrón simple para compuerta AND y Perceptrón Multicapa (MLP) para problema XOR. | **[VALIDO]** Ejecución exitosa. |
| `04_graficas_ventas.coco` | Generación de 4 gráficos nativos en PNG (Barras, Histograma, Dispersión y Líneas). | **[VALIDO]** PNGs generados en `salidas/`. |
| `05_grafica_simple.coco` | Sintaxis compacta de graficación de barras a archivo PNG. | **[VALIDO]** PNG generado en `salidas/`. |
| `06_x_y_contextuales_y_ajuste.coco` | Uso dual de `x` y `y` como identificadores regulares y como ejes de graficación con curva de ajuste. | **[VALIDO]** Ejecución exitosa. |

### Casos Inválidos (`ejemplos/corte3/invalidos/`)
| Archivo | Tipo de Error | Diagnóstico Capturado | Estado |
| :--- | :--- | :--- | :--- |
| `01_error_graficar_variable_no_tabla.coco` | Semántico | Intento de graficar una variable que no es una tabla de datos. | **[RECHAZADO]** Tipo incompatible en graficar. |
| `02_error_ml_calcular_sin_modelo.coco` | Semántico | Llamada a `calcular` con un primer argumento que no es un modelo entrenado. | **[RECHAZADO]** Error semántico en función calcular. |
| `03_error_graficar_ajuste_sin_modelo.coco` | Semántico | Cláusula `ajuste` referenciando una variable que no contiene un modelo. | **[RECHAZADO]** Modelo no entrenado en ajuste. |

---

## 5. Pruebas Unitarias del Motor Tabular (`test_tabla.py`)

Se ejecutó la suite de pruebas unitarias sobre la clase `Tabla` en Python puro:
- **Inferencia de tipos en CSV:** Inferencia correcta de enteros, flotantes y cadenas sin usar pandas.
- **Filtrado relacional:** Evaluación booleana sobre registros tabulares.
- **Columnas calculadas:** Generación de campos aritméticos derivados.
- **Agrupamiento y agregaciones:** Cálculo exacto de suma, media, mediana, varianza y desviación estándar.
- **Persistencia CSV:** Serialización y recuperación íntegra de archivos CSV.
