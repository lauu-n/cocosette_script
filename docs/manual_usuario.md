# Manual de Usuario — Lenguaje Cocosette (DSL)

Cocosette es un Lenguaje de Dominio Específico (DSL) diseñado para la exploración, transformación, modelado con Machine Learning y visualización de datos tabulares, implementado completamente en Python puro sin dependencias pesadas de terceros.

---

## 1. Requisitos e Instalación

- **Python 3.10 o superior**
- **Runtime de ANTLR4 para Python 3**: `antlr4-python3-runtime`
- **Biblioteca estándar de Python**: (módulos `struct`, `zlib`, `math`, `os`, `sys`). No requiere `numpy`, `pandas`, `matplotlib` ni `scikit-learn`.

Instalación de requisitos:
```bash
pip install -r requirements.txt
```

---

## 2. Modos de Ejecución

Cocosette ofrece tres modalidades principales de ejecución:

### A. Modo Script (Lotes)
Ejecuta un archivo con extensión `.coco` desde la línea de comandos:
```bash
python3 src/main.py ejemplos/validos/01_carga_y_pipeline.coco
```
El intérprete valida la sintaxis, ejecuta el script e imprime el resultado de las sentencias `imprimir`.

### B. Modo Terminal Interactiva (REPL)
Inicia una consola interactiva para evaluar comandos paso a paso:
```bash
python3 src/terminal.py
```
Aparecerá el prompt interactivo:
```text
============================================================
  Cocosette — Terminal interactiva
  DSL para Ciencia de Datos y Visualización
  Escribe 'ayuda' para ver los comandos disponibles
  Escribe 'salir' o Ctrl+D para terminar
============================================================

coco> 
```

### C. Modo Híbrido (Script + REPL)
Ejecuta un script y mantiene la sesión abierta en la terminal interactiva con todas las variables cargadas en memoria:
```bash
python3 src/terminal.py -i ejemplos/corte3/02_grafica_simple.coco
```

---

## 3. Comandos Especiales de la Terminal

Dentro de la terminal interactiva `coco>` están disponibles los siguientes comandos auxiliares:

| Comando | Alias | Descripción |
| :--- | :--- | :--- |
| `ayuda` | `help` | Muestra el resumen de sintaxis y comandos. |
| `vars` | `variables` | Lista las variables definidas y su tipo/resumen. |
| `memoria` | — | Inspecciona el entorno de variables en memoria. |
| `limpiar` | `clear` | Limpia la pantalla de la terminal. |
| `reset` | — | Reinicia la memoria de ejecución (elimina variables). |
| `salir` | `exit`, `quit` | Cierra la sesión interactiva. |

---

## 4. Guía de Sintaxis y Capacidades

### 4.1. Variables y Expresiones
Todas las sentencias deben terminar con punto y coma (`;`).
```text
a = 15;
b = 4.5;
nombre = "Laptop";
activo = verdadero;
resultado = (a * 2) + (b / 1.5);
```

### 4.2. Estructuras de Control y Funciones
Cocosette soporta bucles `mientras` y definición de funciones con ámbito léxico propio:

```text
// Bucle mientras
contador = 1;
mientras (contador <= 3) {
    imprimir contador;
    contador = contador + 1;
}

// Funciones con retorno
funcion calcular_iva(precio, tasa) {
    total = precio + (precio * tasa);
    retornar total;
}

compra = calcular_iva(100, 0.19);
imprimir compra;
```

### 4.3. Manipulación de Datos Tabulares (Pipelines)
Las tablas se procesan mediante el operador de tubería `|>`:

```text
// Carga de datos
ventas = cargar "datos/ventas.csv";

// Pipeline de transformación
filtrado = ventas 
    |> filtrar unidades > 5 && precio >= 1000
    |> crear total = unidades * precio
    |> ordenar por total desc;

// Agrupaciones y agregaciones
resumen = ventas
    |> agrupar por [ciudad]
    |> resumir total_ventas = suma(precio), promedio_unidades = media(unidades);

// Guardar resultado
guardar resumen como "salidas/resumen_ciudades.csv";
```

Operaciones de pipeline disponibles:
- `seleccionar [col1, col2]`
- `filtrar <condicion>`
- `crear <nueva_columna> = <expresion>`
- `ordenar por <columna> [asc | desc]`
- `renombrar <col_actual> a <col_nueva>`
- `eliminar_duplicados`
- `eliminar_nulos`
- `rellenar_nulos <columna> con <valor>`
- `convertir <columna> a entero | decimal | texto | booleano`
- `agrupar por [col1, col2]`
- `resumir <salida> = suma | media | mediana | max | min | desviacion | contar(<col>)`

### 4.4. Visualización Gráfica (Motor PNG Puro)
Generación directa de gráficos rasterizados a archivos `.png`:

```text
// 1. Gráfico de dispersión
graficar dispersion datos con x=area y y=precio titulo="Area vs Precio" guardar="salidas/dispersion.png";

// 2. Gráfico de líneas
graficar lineas datos con x=tiempo y y=valor titulo="Evolucion Temporal" guardar="salidas/lineas.png";

// 3. Gráfico de barras
graficar barras resumen con x=ciudad y y=total_ventas titulo="Ventas por Ciudad" guardar="salidas/barras.png";
```

### 4.5. Modelos de Machine Learning
Cocosette incluye algoritmos supervisados de Machine Learning implementados desde cero:

```text
// 1. Regresión Lineal
casas = cargar "datos/casas.csv";
modelo_lin = regresion_lineal(casas, "area", "precio");
pred_casa = evaluar(modelo_lin, 120);
imprimir pred_casa;

// 2. Regresión Polinomial
curva = cargar "datos/curva.csv";
modelo_poli = regresion_polinomial(curva, "x", "y");
pred_curva = evaluar(modelo_poli, 3.5);
imprimir pred_curva;

// 3. Perceptrón Simple (Entrenamiento supervisado)
compuerta = cargar "datos/compuerta_and.csv";
neurona = perceptron(compuerta, "x1", "x2", "y", 0.1, 50);
acc = precision(neurona, compuerta, "x1", "x2", "y");
imprimir acc;

// 4. Perceptrón con pesos manuales
p_manual = perceptron(1.0, 1.0, -1.5);
salida_and = evaluar(p_manual, 1, 1);
imprimir salida_and;
```
