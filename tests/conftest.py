# Esse arquivo é responsável por configurar o ambiente de teste para o pytest, garantindo que a pasta src seja incluída no caminho do Python.
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))