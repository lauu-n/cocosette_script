# Manual Técnico — Arquitectura e Implementación de Cocosette

Este documento describe la arquitectura interna, diseño de módulos y componentes de bajo nivel del compilador/intérprete del DSL Cocosette.

---

## 1. Arquitectura General del Sistema

El flujo de procesamiento de Cocosette sigue el patrón clásico de compilación e interpretación guiado por árboles de sintaxis abstracta (AST):

```text
Código fuente (.coco) / Comando interactivo (coco>)
                      │
                      ▼
        [CocosetteLexer (ANTLR4)]
                      │ Flujo de Tokens
                      ▼
        [CocosetteParser (ANTLR4)] ◄─── [ColectorDeErrores (ErrorListener)]
                      │ Árbol Sintáctico (AST)
                      ▼
          [InterpreteVisitor]
          ├── MemoriaEjecucion (Variables y ámbitos)
          ├── Tabla (Estructuras de datos y transformaciones)
          ├── ML (Regresión analítica, polinomial y perceptrón)
          └── Cocograficar (Rasterizador binario PNG)
```

### Componentes Principales

| Módulo / Archivo | Rol en el Sistema |
| :--- | :--- |
| `grammar/Cocosette.g4` | Especificación léxica y sintáctica en ANTLR4. |
| `src/main.py` | Entrada CLI para ejecución de scripts en lote con validación sintáctica. |
| `src/terminal.py` | REPL interactivo con manejo de memoria persistente y buffer multilínea. |
| `src/validar.py` | Implementación de `ColectorDeErrores` y validación sintáctica sin visitor. |
| `src/visitor.py` | Intérprete que hereda de `CocosetteVisitor` y ejecuta los nodos del AST. |
| `src/librerias/` (`librerias/`) | Paquete modular que agrupa todas las librerías del dominio. |
| `src/librerias/cocograficar.py` | Motor de gráficos PNG binario puro con algoritmos de rasterizado y fuente bitmap. |
| `src/librerias/ml.py` | Algoritmos de Machine Learning (Regresión OLS, Polinomial y Perceptrón) en Python puro. |
| `src/librerias/tabla.py` | Implementación de datos tabulares, álgebra relacional, conversiones y agregaciones. |
| `src/librerias/memoria_ejecucion.py` | Manejador de entornos de variables con soporte de ámbitos léxicos (scopes). |
| `src/parser/` | Clases del compilador generadas automáticamente por ANTLR4. |

---

## 2. Gramática y Manejo de Errores

### 2.1. Tokens y Reglas Sintácticas
La gramática define operadores aritméticos con precedencia canónica:
- Exponenciación (`^`)
- Multiplicación y División (`*`, `/`, `%`)
- Suma y Resta (`+`, `-`)
- Comparaciones (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Conectores lógicos (`&&`, `||`, `!`)

Para la conversión de tipos en pipelines, se separó el token literal booleano (`COCOBOOLEANO: 'verdadero' | 'falso'`) del token descriptor de tipo (`COCOTIPOBOOL: 'booleano' | 'bool'`), permitiendo sentencias como:
```text
tabla |> convertir estado a booleano;
```

### 2.2. Manejo de Errores (`ColectorDeErrores`)
Hereda de `antlr4.error.ErrorListener.ErrorListener`. Sobrescribe `syntaxError` para recolectar línea, columna y mensaje del error.
Tanto `src/main.py` como `src/terminal.py` eliminan los listeners por defecto (`removeErrorListeners`) e inyectan `ColectorDeErrores` tanto en el lexer como en el parser. Esto previene trazas crudas de Python (*tracebacks*) y permite abortar de forma limpia reportando el fallo exacto al programador.

---

## 3. Motor de Gráficos Binario PNG (`cocograficar.py`)

El módulo `cocograficar.py` es un rasterizador bidimensional puro que no requiere bibliotecas gráficas (`matplotlib`, `Pillow`, `OpenCV`).

### 3.1. Estructura Binaria del Archivo PNG
Escribe directamente los bytes del estándar PNG (RFC 2083):
1. **Firma mágica PNG**: `\x89PNG\r\n\x1a\n` (8 bytes).
2. **Chunk `IHDR`**: Ancho, alto, profundidad de color (8 bits), modo RGB (tipo 2), compresión DEFLATE.
3. **Chunk `IDAT`**:
   - Cada fila de píxeles inicia con un byte de filtro (Filtro 0 = *None*).
   - Los datos RGB se comprimen usando `zlib.compress(raw_data, level=6)`.
4. **Chunk `IEND`**: Marca el fin de la imagen binaria.
Cada chunk incluye su longitud (4 bytes big-endian), tipo (4 bytes ASCII), carga útil y código de redundancia cíclica (`CRC32`).

### 3.2. Algoritmos de Rasterización
- **Líneas (Bresenham)**: Trazado incremental de líneas rectas entre coordenadas enteras $(x_0, y_0)$ y $(x_1, y_1)$ sin operaciones en coma flotante en el bucle principal.
- **Círculos (Punto Medio)**: Rasterización de puntos de dispersión mediante simetría de 8 octantes.
- **Barras y Rectángulos**: Relleno directo de buffers matriciales de píxeles RGB.

### 3.3. Tipografía Bitmap 5×7
Para renderizar texto (títulos de ejes, etiquetas numéricas y leyenda), se implementa una matriz de caracteres de 5 columnas por 7 filas codificada en tuplas hexadecimales. Cada bit encendido representa un píxel activo del carácter, permitiendo escalado entero (factor $2\times$ o $3\times$) sin fuentes del sistema operativo.

---

## 4. Módulo de Machine Learning (`ml.py`)

Implementado con la biblioteca matemática estándar (`math`):

### 4.1. Regresión Lineal Simple
Calcula la pendiente $m$ y el intercepto $b$ mediante la solución analítica de Mínimos Cuadrados Ordinarios (OLS):
$$m = \frac{N \sum xy - \sum x \sum y}{N \sum x^2 - (\sum x)^2}, \quad b = \frac{\sum y - m \sum x}{N}$$
Adicionalmente provee soporte para optimización iterativa por Descenso de Gradiente estocástico/por lotes.

### 4.2. Regresión Polinomial (Grado 2)
Modela relaciones parabólicas $y = a x^2 + b x + c$. Construye las ecuaciones normales del sistema:
$$\begin{pmatrix} \sum x^4 & \sum x^3 & \sum x^2 \\ \sum x^3 & \sum x^2 & \sum x \\ \sum x^2 & \sum x & N \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \begin{pmatrix} \sum x^2 y \\ \sum x y \\ \sum y \end{pmatrix}$$
El sistema se resuelve analíticamente mediante la Regla de Cramer / Eliminación Gaussiana directa sin requerir álgebra lineal de `numpy`.

### 4.3. Perceptrón Simple de Rosenblatt
Clasificador binario lineal con función de activación escalón (Heaviside):
$$\hat{y} = \begin{cases} 1 & \text{si } \sum w_i x_i + b \ge 0 \\ 0 & \text{en caso contrario} \end{cases}$$
Regla de actualización de pesos:
$$w_i \leftarrow w_i + \eta (y - \hat{y}) x_i, \quad b \leftarrow b + \eta (y - \hat{y})$$
Donde $\eta$ es la tasa de aprendizaje.

---

## 5. Estructura de Datos Tabulares (`tabla.py`)

La clase `Tabla` representa un conjunto de datos estructurado en filas y columnas:
- Representación interna: Lista de diccionarios Python (`List[Dict[str, Any]]`) para indexación rápida por nombre de columna.
- Inmutabilidad en transformaciones: Cada operación del pipeline genera una nueva instancia de `Tabla`, preservando los datos de origen contra efectos secundarios no deseados.
- Tipado dinámico e inferencia: Al leer CSV, infiere automáticamente enteros, números de punto flotante y cadenas, permitiendo conversión explícita posterior.
