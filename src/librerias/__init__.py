"""Librerias de soporte para el DSL Cocosette.

Contiene los modulos de dominio:
- cocograficar: Motor de rasterizacion grafica PNG en Python puro.
- ml: Modelos de Machine Learning (Regresion Lineal, Polinomial, Perceptron).
- tabla: Estructura tabular de datos y operaciones relacionales.
- memoria_ejecucion: Gestion de entornos de variables y ambitos lexicos.
"""

from .cocograficar import graficar
from .tabla import Tabla, AgrupacionTabla
from .memoria_ejecucion import MemoriaEjecucion
from . import ml

__all__ = ["graficar", "Tabla", "AgrupacionTabla", "MemoriaEjecucion", "ml"]
