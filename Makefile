CARPETA_GRAMATICA = grammar
GRAMATICA         = Cocosette.g4

SALIDA_DESDE_GRAMATICA = ../src/parser
SALIDA_DESDE_RAIZ      = src/parser

.PHONY: generar validar limpiar interactivo test

generar:
	cd $(CARPETA_GRAMATICA) && antlr4 -Dlanguage=Python3 -visitor -o $(SALIDA_DESDE_GRAMATICA) $(GRAMATICA)

validar:
	python3 src/validar.py ejemplos/validos/*.coco
	python3 src/validar.py ejemplos/corte3/*.coco
	python3 src/validar.py ejemplos/invalidos/*.coco

interactivo:
	python3 src/terminal.py

test:
	python3 test_tabla.py

limpiar:
	find $(SALIDA_DESDE_RAIZ) -type f ! -name '__init__.py' -delete
	rm -rf $(SALIDA_DESDE_RAIZ)/__pycache__
	rm -rf src/__pycache__
