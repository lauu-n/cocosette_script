# Reporte de Pruebas — DSL Cocosette (Corte III)

## 1. Alcance de las Pruebas

El presente reporte consolida las pruebas de validación sintáctica, ejecución semántica y regresión para el tercer corte del lenguaje Cocosette. Se cubren tres grupos de pruebas:
1. **Ejemplos Válidos (`ejemplos/validos/`)**: Pruebas de integración del DSL, bucles, funciones, pipelines y algoritmos de Machine Learning.
2. **Ejemplos de Gráficas (`ejemplos/corte3/`)**: Pruebas de visualización y rasterizado PNG en Python puro.
3. **Casos Inválidos (`ejemplos/invalidos/`)**: Detección de errores léxicos, sintácticos y semánticos con reporte de línea y columna.

Comando de validación automatizada:
```bash
make validar
```

---

## 2. Resultados de Pruebas Positivas (Ejemplos Válidos)

| Archivo | Funcionalidad Evaluada | Resultado |
| :--- | :--- | :--- |
| `01_carga_y_pipeline.coco` | Carga de CSV, selección y filtrado con operadores lógicos (`&&`). | **[VALIDO]** Ejecución exitosa. |
| `02_expresiones_basicas.coco` | Precedencia de operadores aritméticos (`+`, `*`, `^`) y booleanos. | **[VALIDO]** Ejecución exitosa. |
| `03_visualizacion.coco` | Cláusulas de graficar con títulos y destinos personalizados. | **[VALIDO]** Ejecución exitosa. |
| `04_operaciones_corte2.coco` | Transformaciones completas: agrupar, resumir, convertir y ordenar. | **[VALIDO]** Ejecución exitosa. |
| `05_aritmetica_e_impresion.coco` | Operaciones matemáticas con variables locales y sentencias `imprimir`. | **[VALIDO]** Ejecución exitosa. |
| `06_bucle_mientras.coco` | Estructuras de repetición `mientras` con variables acumuladoras. | **[VALIDO]** Ejecución exitosa. |
| `07_funciones.coco` | Definición de funciones, paso de argumentos y retorno de valores. | **[VALIDO]** Ejecución exitosa. |
| `08_regresion_lineal.coco` | Entrenamiento de regresión lineal (OLS) y predicción con `evaluar`. | **[VALIDO]** Ejecución exitosa. |
| `09_regresion_polinomial.coco` | Ajuste polinomial de grado 2 y predicción parabólica. | **[VALIDO]** Ejecución exitosa. |
| `10_perceptron_y_xor.coco` | Perceptrón simple para compuertas lógicas y métrica de precisión. | **[VALIDO]** Ejecución exitosa. |

**Total positivos generales:** 10/10 aprobados exitosamente.

---

## 3. Resultados de Pruebas de Visualización (Corte III)

| Archivo | Tipo de Gráfico | Salida Generada | Resultado |
| :--- | :--- | :--- | :--- |
| `01_graficas.coco` | Dispersión, Líneas y Barras | Archivos PNG en `salidas/` | **[VALIDO]** PNGs generados correctamente. |
| `02_grafica_simple.coco` | Dispersión básica | Archivo PNG en `salidas/` | **[VALIDO]** Rasterizado exitoso. |
| `03_x_y_contextuales.coco` | Tubería con graficación integrada | Archivo PNG en `salidas/` | **[VALIDO]** Sintaxis contextual validada. |

**Total visualización:** 3/3 aprobados exitosamente.

---

## 4. Resultados de Pruebas Negativas (Casos Inválidos)

| Archivo | Tipo de Error | Diagnóstico Esperado y Reportado | Estado |
| :--- | :--- | :--- | :--- |
| `01_error_lexico_cadena_sin_cerrar.coco` | Léxico | Comilla de cierre faltante en cadena de texto. | **[RECHAZADO]** Error léxico capturado con línea y columna. |
| `02_error_sintactico_falta_punto_coma.coco` | Sintáctico | Sentencia sin terminador `;`. | **[RECHAZADO]** Error sintáctico capturado por `ColectorDeErrores`. |
| `03_error_palabra_reservada_como_identificador.coco` | Léxico/Sintáctico | Uso de palabra reservada como nombre de variable. | **[RECHAZADO]** Rechazado por conflicto de tokens. |
| `04_error_semantico_variable_no_declarada.coco` | Semántico | Lectura de variable no definida en la memoria. | **[RECHAZADO]** Error semántico reportado: variable no declarada. |
| `05_error_semantico_division_por_cero.coco` | Semántico | Operación aritmética de división con divisor 0. | **[RECHAZADO]** Capturado: división por cero no permitida. |
| `06_error_semantico_columna_inexistente.coco` | Semántico | Acceso a columna no presente en la tabla. | **[RECHAZADO]** Capturado: columna inválida en pipeline. |

**Total negativos:** 6/6 rechazados correctamente con posición exacta de línea y columna.

---

## 5. Pruebas Unitarias del Motor Tabular (`test_tabla.py`)

Se ejecutó la suite de pruebas unitarias sobre la clase `Tabla` en Python puro:
- **Inferencia de tipos en CSV:** Inferencia correcta de enteros, flotantes y cadenas sin usar pandas.
- **Filtrado relacional:** Evaluación booleana sobre registros tabulares.
- **Columnas calculadas:** Generación de campos aritméticos derivados.
- **Agrupamiento y agregaciones:** Cálculo exacto de suma, media, mediana, varianza y desviación estándar.
- **Persistencia CSV:** Serialización y recuperación íntegra de archivos CSV.
