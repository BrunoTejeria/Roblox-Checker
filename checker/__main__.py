import numpy as np
import time
import json
import requests
import colorama

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
  TEXT_FILE = f"./text_files/text"
  if ".txt" not in TEXT_FILE:
    TEXT_FILE += ".txt"

  # Archivo de texto para guardar
  #out = input("Archivo de salida: ")
  RESULT_FILE = f"./results/r.txt"

  # Leer configuracion
  #config = read_config()



  # Leer archivo de texto
  with open(TEXT_FILE, "r") as f:
    text = f.readlines()

    founded = np.array([])

    for user in text:
      # sacar '\n'
      username = user.split(":")[0]
      url = f"https://www.roblox.com/user.aspx?username={username}"
      response = requests.get(url)
      if response.status_code == 200:
        np.append(founded, user)
        print(Fore.GREEN +f"Found {username}")
  with open(RESULT_FILE, "w") as f:
    for user in founded:
      print(user)
      f.write(user)

main()


