import numpy as np
import time
import json
import requests

"""def open_file(file: str, mode: str ="r", data: list = None, json: bool = False):
  if mode == "r":
    with open(file, "r") as f:
      return f.readlines()
  elif mode == "w":
    with open(file, "w") as f:
      for line in data:
        f.write(line)
  elif mode == "a":
    with open(file, "a") as f:
      for line in data:
        f.write(line)"""


def read_config():
  with open("checker/config.json", "r") as f:
    return json.load(f)


def main():

  # Archivo de texto para buscar
  #inp = input("Archivo de texto: ")
  TEXT_FILE = f"../text_files/text"
  if ".txt" not in TEXT_FILE:
    TEXT_FILE += ".txt"

  # Archivo de texto para guardar
  #out = input("Archivo de salida: ")
  RESULT_FILE = f"../results/r.txt"

  # Leer configuracion
  config = read_config()

  # Leer archivo de texto
  with open(TEXT_FILE, "r") as f:
    text = f.readlines()
    print(text)


