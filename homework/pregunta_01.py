"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
  """
  Construya y retorne un dataframe de Pandas a partir del archivo
  'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

  - El dataframe tiene la misma estructura que el archivo original.
  - Los nombres de las columnas deben ser en minusculas, reemplazando los
    espacios por guiones bajos.
  - Las palabras clave deben estar separadas por coma y con un solo
    espacio entre palabra y palabra.
      
  """

  import pandas as pd
  import re

  # Ruta del archivo
  file_path = "files/input/clusters_report.txt"

  # Leer el archivo línea por línea
  with open(file_path, "r", encoding="utf-8") as f:
      lines = f.readlines()

  # Definir encabezados manualmente
  headers = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]

  # Filtrar líneas útiles (ignorar encabezado decorativo)
  data_lines = lines[4:]  # Ignorar las primeras 4 líneas de encabezado decorativo

  # Combinar líneas de la tabla en registros únicos
  data = []
  current_row = []
  for line in data_lines:
      # Detectar separadores de filas por inicio numérico
      if re.match(r"^\s*\d+\s+", line):
          if current_row:
              data.append(" ".join(current_row))
              current_row = []
      current_row.append(line.strip())
  if current_row:
      data.append(" ".join(current_row))

  # Extraer datos usando expresiones regulares
  rows = []
  for entry in data:
      match = re.match(
          r"^(\d+)\s+(\d+)\s+([\d.,]+)\s+%\s+(.+)$", entry
      )
      if match:
          cluster, cantidad, porcentaje, palabras = match.groups()
          # Limpiar y ajustar las palabras clave
          palabras = re.sub(r"\s+", " ", palabras.strip())  # Normalizar espacios
          palabras = palabras.rstrip(".")  # Eliminar puntos finales
          rows.append([int(cluster), int(cantidad), float(porcentaje.replace(",", ".")), palabras])

  # Crear DataFrame
  df = pd.DataFrame(rows, columns=headers)
  return df



# Llamar a la función y mostrar el resultado
if __name__ == "__main__":
    resultados = pregunta_01()
    print("Resumen del procesamiento:")
    print(resultados)
