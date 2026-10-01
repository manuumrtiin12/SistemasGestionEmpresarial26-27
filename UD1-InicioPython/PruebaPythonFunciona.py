import sys
from pathlib import Path

empresa = "Librería Norte"
pedidos_pendientes = 4

print("Entorno preparado correctamente")
print(f"Empresa: {empresa}")
print(f"Pedidos pendientes: {pedidos_pendientes}")
print(f"Versión de Python: {sys.version.split()[0]}")
print(f"Intérprete: {sys.executable}")
print(f"Carpeta de trabajo: {Path.cwd()}")

