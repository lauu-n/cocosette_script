# COCOCSETTE SCRIPT

Cocosette es un lenguaje DSL de datos con una sintaxis de pipelines.

Se desarrolló en Python y utiliza ANTLR4 para generar el lexer, el parser y el visitor.

No utiliza bibliotecas externas como pandas, NumPy, Matplotlib o scikit-learn. 
Las tablas, operaciones estadísticas, gráficos PNG, perceptrones y regresiones se implementan directamente con Python y la biblioteca estándar.

## Ejemplo rápido

```text
ventas = cargar "datos/ventas.csv";

resultado = ventas
    |> seleccionar [ciudad, unidades, precio]
    |> crear total = unidades * precio
    |> ordenar por total desc;

imprimir resultado;

guardar resultado como "salidas/ventas_ordenadas.csv";
```

Ejecutarlo:

```bash
python3 src/main.py ejemplos/corte2/validos/02_operaciones_corte2.coco
```

## ¿Qué permite hacer Cocosette?

Cocosette incluye funciones para:

- Expresiones aritméticas y lógicas.
- Variables y valores booleanos.
- Carga y exportación de archivos CSV.
- Selección y filtrado de columnas.
- Creación de columnas calculadas.
- Ordenamiento y eliminación de duplicados.
- Tratamiento de valores nulos.
- Conversión de tipos.
- Agrupaciones y funciones estadísticas.
- Pipelines encadenados con `|>`.
- Definición y llamada de funciones.
- Bucles `mientras`.
- Regresión lineal y polinomial.
- Perceptrón simple.
- Gráficos de barras, líneas, histogramas y dispersión.
- Ejecución por archivos o desde una terminal interactiva.
- Validación léxica y sintáctica de archivos `.coco`.

## Requisitos

- Python 3.10 o superior.
- Java JDK 11 o superior.
- ANTLR 4.13.2.
- El runtime de ANTLR para Python:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```text
antlr4-python3-runtime==4.12.0
```

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/lauu-n/cocosette_script.git
cd cocosette_script
```

Crea un entorno virtual opcional:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Si modificas la gramática, vuelve a generar el lexer y el parser:

```bash
make generar
```

Este comando ejecuta internamente:

```bash
cd grammar
antlr4 -Dlanguage=Python3 -visitor -o ../src/parser Cocosette.g4
```

## Formas de ejecución

### Ejecutar un archivo `.coco`

Ejecuta un programa completo con el intérprete principal:

```bash
python3 src/main.py ruta/al/archivo.coco
```

Ejemplo:

```bash
python3 src/main.py ejemplos/corte3/validos/01_regresion_lineal.coco
```

El programa:

1. Lee el archivo fuente.
2. Ejecuta el análisis léxico.
3. Ejecuta el análisis sintáctico.
4. Recorre el árbol sintáctico mediante el visitor.
5. Ejecuta las operaciones semánticas.
6. Muestra los resultados en consola.
7. Genera los archivos solicitados, como CSV o PNG.

### Ejecutar la terminal interactiva

```bash
python3 src/terminal.py
```

Aparecerá el prompt:

```text
coco>
```

Ejemplo de uso:

```text
coco> ventas = cargar "datos/ventas.csv";
coco> imprimir ventas;
coco> vars
coco> cocosalir
```

El terminal conserva las variables durante toda la sesión.

### Ejecutar un archivo y continuar interactuando

```bash
python3 src/terminal.py -i ejemplos/corte3/validos/04_graficas_ventas.coco
```

Las variables creadas por el archivo se conservarán cuando se abra el modo interactivo.

### Comandos de la terminal

| Comando | Alias | Descripción |
|---|---|---|
| `cocoayuda` | `help` | Muestra la ayuda |
| `vars` | `variables` | Lista las variables actuales |
| `memoria` | | Muestra el contenido completo de la memoria |
| `limpiar` | `clear` | Limpia la pantalla |
| `reset` | | Elimina todas las variables |
| `correr <archivo>` | `cargar`, `ejecutar` | Ejecuta un archivo `.coco` |
| `cocosalir` | `exit`, `quit` | Termina la terminal |

## Validación de archivos

Para revisar si uno o varios archivos cumplen con la gramática:

```bash
python3 src/validar.py archivo.coco
```

Ejemplo con varios archivos:

```bash
python3 src/validar.py \
  ejemplos/corte3/validos/*.coco \
  ejemplos/corte3/invalidos/*.coco
```

También puedes validar todas las versiones de los tres cortes con Make:

```bash
make validar
```

El validador distingue entre:

- Errores léxicos.
- Errores sintácticos.
- Archivos válidos.
- La forma abreviada del árbol sintáctico generado.

## Ejecución de pruebas

Las pruebas disponibles utilizan el módulo estándar `unittest`:

```bash
python3 test_tabla.py
```

También puedes ejecutar:

```bash
make test
```

## Sintaxis del lenguaje

Todas las sentencias suelen terminar con punto y coma:

```text
x = 10;
imprimir x;
```

Las funciones, bucles y bloques usan llaves:

```text
mientras (x < 10) {
    imprimir x;
    x = x + 1;
}
```

Los comentarios comienzan con `#`:

```text
# Este texto es un comentario
precio = 100;
```

## Variables y expresiones

Cocosette admite enteros, decimales, cadenas y valores booleanos.

```text
entero = 10;
decimal = 3.14;
texto = "Cocosette";
verdad = verdadero;
mentira = falso;
```

Operadores aritméticos:

```text
suma = 10 + 5;
resta = 10 - 5;
multiplicacion = 10 * 5;
division = 10 / 5;
residuo = 10 % 3;
potencia = 2 ^ 8;
negativo = -10;
```

Operadores lógicos y relacionales:

```text
igual = 10 == 10;
diferente = 10 != 5;
menor = 5 < 10;
menor_igual = 5 <= 5;
mayor = 10 > 5;
mayor_igual = 10 >= 10;
ambos = verdadero && verdadero;
alguno = verdadero || falso;
negacion = !falso;
```

## Datos CSV

Carga un archivo:

```text
ventas = cargar "datos/ventas.csv";
imprimir ventas;
```

Las rutas deben escribirse como cadenas:

```text
datos = cargar "datos/casas.csv";
```

Exporta una tabla:

```text
guardar ventas como "salidas/ventas.csv";
```

La carpeta de destino se crea automáticamente si no existe.

## Operaciones sobre tablas

Cocosette utiliza el operador `|>` para encadenar operaciones:

```text
resultado = ventas
    |> seleccionar [ciudad, unidades, precio]
    |> crear total = unidades * precio
    |> filtrar donde total > 100
    |> ordenar por total desc;
```

### Seleccionar columnas

```text
resultado = ventas |> seleccionar [ciudad, precio];
```

### Filtrar filas

```text
resultado = ventas |> filtrar donde precio > 100;
```

Las condiciones pueden contener variables, columnas, paréntesis y operadores:

```text
resultado = ventas
    |> filtrar donde (ciudad == "Bogota" && precio >= 50);
```

### Crear una columna

```text
resultado = ventas |> crear total = unidades * precio;
```

### Ordenar

```text
resultado = ventas |> ordenar por precio asc;
resultado = ventas |> ordenar por precio desc;
```

Si no se indica `asc` o `desc`, se utiliza ascendente.

### Renombrar

```text
resultado = ventas |> renombrar precio como precio_unitario;
```

### Eliminar duplicados

```text
resultado = ventas |> eliminar_duplicados;
```

### Eliminar valores nulos

```text
resultado = ventas |> eliminar_nulos;
```

### Rellenar valores nulos

```text
resultado = ventas |> rellenar_nulos precio con 0;
```

### Convertir tipos

```text
resultado = ventas |> convertir unidades a entero;
resultado = ventas |> convertir precio a decimal;
resultado = ventas |> convertir ciudad a texto;
resultado = ventas |> convertir activo a booleano;
```

Tipos disponibles:

- `entero`
- `decimal`
- `texto`
- `booleano`

## Agrupaciones y resúmenes

Ejemplo:

```text
resumen = ventas
    |> agrupar por [ciudad]
    |> resumir
        total = suma(precio),
        promedio = media(precio),
        registros = contar();
```

La función `contar` puede no recibir una columna.

Funciones disponibles:

| Función | Descripción |
|---|---|
| `suma(columna)` | Suma los valores |
| `media(columna)` | Calcula el promedio |
| `mediana(columna)` | Calcula la mediana |
| `minimo(columna)` | Obtiene el valor mínimo |
| `maximo(columna)` | Obtiene el valor máximo |
| `desviacion_estandar(columna)` | Calcula la desviación estándar |
| `contar()` | Cuenta las filas |

## Funciones definidas por el usuario

Sintaxis:

```text
funcion calcular_iva(precio, tasa) {
    total = precio + (precio * tasa);
    retornar total;
}

resultado = calcular_iva(100, 0.19);
imprimir resultado;
```

Las funciones tienen memoria local y pueden recibir parámetros.

También existen las palabras reservadas alternativas:

```text
def calcular_iva(precio, tasa) { ... }
fn calcular_iva(precio, tasa) { ... }
return total;
```

## Bucles

```text
contador = 1;

mientras (contador <= 5) {
    imprimir contador;
    contador = contador + 1;
}
```

La condición puede escribirse con o sin paréntesis:

```text
mientras contador <= 5 {
    imprimir contador;
}
```

## Machine Learning

Los modelos se implementan directamente en el proyecto, sin pandas ni scikit-learn.

### Regresión lineal

```text
casas = cargar "datos/casas.csv";
modelo = regresion_lineal(casas, "area", "precio", 0.01, 1000);
prediccion = calcular(modelo, 120);
imprimir prediccion;
```

Argumentos opcionales:

- tasa de aprendizaje.
- número de épocas.

### Regresión polinomial

```text
curva = cargar "datos/curva.csv";
modelo = regresion_polinomial(curva, "x", "y");
prediccion = calcular(modelo, 3.5);
imprimir prediccion;
```

### Perceptrón manual

```text
neurona = perceptron(1.0, 1.0, -1.5);
resultado = calcular(neurona, 1, 1);
imprimir resultado;
```

### Perceptrón entrenado

```text
compuerta = cargar "datos/compuerta_and.csv";
neurona = perceptron(compuerta, "x1", "x2", "y", 0.1, 100);
resultado = calcular(neurona, 1, 1);
imprimir resultado;
```

## Gráficos

Los gráficos se generan como imágenes PNG de 800 × 500 píxeles. El motor gráfico está implementado con Python estándar.

### Barras

```text
graficar barras resumen
    x ciudad
    y total
    titulo "Ventas por ciudad"
    guardar como "salidas/ventas.png";
```

### Líneas

```text
graficar lineas ventas
    x fecha
    y total
    titulo "Ventas por fecha"
    guardar como "salidas/lineas.png";
```

### Histograma

```text
graficar histograma ventas
    x precio
    titulo "Distribucion de precios"
    guardar como "salidas/histograma.png";
```

### Dispersión

```text
graficar dispersion casas
    x area
    y precio
    titulo "Area vs precio"
    etiqueta_x "Metros cuadrados"
    etiqueta_y "Precio"
    guardar como "salidas/dispersion.png";
```

Opciones disponibles:

- `titulo "Texto"`
- `etiqueta_x "Texto"`
- `etiqueta_y "Texto"`
- `leyenda "Texto"`
- `guardar como "ruta/imagen.png"`
- `ajuste modelo`
- `por_clase columna`

Ejemplo con ajuste:

```text
casas = cargar "datos/casas.csv";
modelo = regresion_lineal(casas, "area", "precio");

graficar dispersion casas
    x area
    y precio
    ajuste modelo
    titulo "Regresion"
    guardar como "salidas/regresion.png";
```

## Estructura del repositorio

```text
cocosette_script/
├── README.md
├── Makefile
├── requirements.txt
├── test_tabla.py
├── datos/
├── docs/
├── ejemplos/
├── grammar/
├── salidas/
└── src/
```

### Archivos principales

| Ruta | Contenido |
|---|---|
| `README.md` | Documentación general del proyecto |
| `Makefile` | Comandos para generar, validar y probar el proyecto |
| `requirements.txt` | Dependencia principal de ANTLR |
| `test_tabla.py` | Pruebas básicas del motor tabular |

### `datos/`

Contiene los conjuntos de datos usados en los ejemplos:

- `ventas.csv`
- `casas.csv`
- `curva.csv`
- `compuerta_and.csv`

### `docs/`

Documentación técnica y funcional:

- `documento_alcance.md`: alcance y objetivos del lenguaje.
- `conceptos_antlr.md`: explicación de lexer, parser y visitor.
- `manual_usuario.md`: guía de uso de Cocosette.
- `manual_tecnico.md`: arquitectura e implementación.
- `reporte_pruebas.md`: pruebas y resultados.

### `ejemplos/`

Ejemplos separados por cortes académicos:

```text
ejemplos/
├── corte1/
├── corte2/
└── corte3/
```

Cada corte contiene:

- `validos/`: programas que deben ejecutarse correctamente.
- `invalidos/`: ejemplos diseñados para provocar errores.

Los archivos tienen extensión `.coco`.

### `grammar/`

Contiene la gramática principal:

```text
grammar/Cocosette.g4
```

Define:

- Palabras reservadas.
- Identificadores.
- Literales.
- Operadores.
- Sentencias.
- Expresiones.
- Pipelines.
- Operaciones de datos.
- Machine Learning.
- Gráficos.
- Comentarios y espacios.

### `src/`

Contiene el intérprete:

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada para ejecutar archivos |
| `terminal.py` | Terminal interactiva y REPL |
| `visitor.py` | Interpreta y ejecuta el árbol sintáctico |
| `validar.py` | Comprueba errores léxicos y sintácticos |
| `librerias/` | Motores de datos, memoria, ML y gráficos |
| `parser/` | Clases generadas automáticamente por ANTLR |

### `src/librerias/`

| Archivo | Responsabilidad |
|---|---|
| `tabla.py` | Representación de tablas, agrupaciones y operaciones |
| `memoria_ejecucion.py` | Variables y ámbitos locales |
| `ml.py` | Regresión lineal, polinomial y perceptrón |
| `cocograficar.py` | Generación de gráficos y archivos PNG |

### `src/parser/`

Contiene los archivos generados por ANTLR:

- `CocosetteLexer.py`
- `CocosetteParser.py`
- `CocosetteListener.py`
- `CocosetteVisitor.py`
- Archivos `.tokens`
- Archivos `.interp`

Estos archivos normalmente no deben editarse manualmente. Deben regenerarse ejecutando `make generar` después de modificar `grammar/Cocosette.g4`.

### `salidas/`

Directorio destinado a los resultados producidos por Cocosette:

- CSV exportados.
- Gráficos PNG.


## Comandos Make disponibles

| Comando | Acción |
|---|---|
| `make generar` | Genera el lexer y parser desde la gramática |
| `make validar` | Valida los ejemplos válidos e inválidos |
| `make interactivo` | Abre la terminal interactiva |
| `make test` | Ejecuta `test_tabla.py` |
| `make limpiar` | Elimina archivos temporales y cachés |

## Flujo interno de ejecución

```text
Archivo .coco
     │
     ▼
Lexer ANTLR
     │
     ▼
Tokens
     │
     ▼
Parser ANTLR
     │
     ▼
Árbol sintáctico
     │
     ▼
InterpreteVisitor
     │
     ├─ Memoria de variables
     ├─ Tablas
     ├─ Funciones
     ├─ Regresión y ML
     ├─ Operaciones de pipeline
     └─ Gráficos
```

## Gestión de errores

Cocosette puede informar errores en varias etapas:

- Error léxico: carácter o cadena no reconocido.
- Error sintáctico: sentencia con estructura inválida.
- Variable no declarada.
- División por cero.
- Columna inexistente.
- Tipo de dato inválido.
- Modelo no válido.
- Archivo o ruta inexistente.
- Función no definida.
- Número incorrecto de argumentos.

Los mensajes incluyen, cuando corresponde, número de línea y columna.

## Ejemplos incluidos

### Corte 1

Fundamentos del lenguaje:

- Literales.
- Expresiones.
- Asignaciones.
- Tipos.
- Impresión.
- Errores léxicos y sintácticos.

### Corte 2

Manipulación de datos:

- Carga de CSV.
- Selección.
- Filtros.
- Columnas calculadas.
- Pipelines.
- Agrupaciones.
- Exportación.
- Bucles.
- Funciones.

### Corte 3

Modelado y visualización:

- Regresión lineal.
- Regresión polinomial.
- Perceptrón.
- Gráficos.
- Ajustes de modelos.
- Clasificaciones.
- Ejemplos con errores semánticos.

## Limitaciones conocidas

- La implementación no usa pandas ni NumPy.
- Las tablas se representan con estructuras internas propias.
- Los gráficos se generan directamente como PNG.
- El histograma admite una sola columna.
- Los gráficos de dispersión deben usar columnas numéricas.
- La representación gráfica de texto se reduce a una fuente bitmap limitada.
- Los modelos se entrenan con implementaciones sencillas.
- El terminal trabaja en modo línea por línea y conserva una memoria independiente.

## INTEGRANTES
- David Avendaño
- Laura Niño
- Brayan Paredes
