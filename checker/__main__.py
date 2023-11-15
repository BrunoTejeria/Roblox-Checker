import numpy as np
import time
import json
import requests
import tqdm
from colorama import (
  Fore
)

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

import concurrent.futures

# La función que quieres ejecutar múltiples veces
def mi_funcion():
    # Aquí puedes poner tu código a ejecutar
    resultado = 42  # Ejemplo, reemplaza esto con tu código
    return resultado





def read_config():
  with open("checker/config.json", "r") as f:
    return json.load(f)

def request(user: str, pbar: tqdm.tqdm = None):
  try:
    # Dividir el user del password
    username = user.split(":")[0]
    url = f"https://www.roblox.com/user.aspx?username={username}"
    response = requests.get(url)
    pbar.update(1)

    # Si el código de respuesta es 200, entonces guardar el user
    if response.status_code == 200:
      print(Fore.GREEN +f"Found {username}")
      return user
  except Exception as e:
    return None

def main():
  TEXT_FILE = f"./text_files/text"
  if ".txt" not in TEXT_FILE:
    TEXT_FILE += ".txt"
  RESULT_FILE = f"./results/r.txt"


  # Leer archivo de texto
  with open(TEXT_FILE, "r") as f:
    text = f.readlines()
    founded = np.array([])

    # Buscar si los usuarios existen
    with tqdm.tqdm(total=len(text)) as pbar:
      with concurrent.futures.ThreadPoolExecutor() as exe:
        resultados = list(exe.map(request, text))
        for i in resultados:
          if i != None:
            founded = np.append(founded, i)


    # Escribir users en archivo de salida
    with open(RESULT_FILE, "w") as f:
      for user in founded:
        f.write(user)

main()


