import numpy as np
import json
import requests
import tqdm
from colorama import Fore

import concurrent.futures

def read_config():
    with open("checker/config.json", "r") as f:
        return json.load(f)

def request(user: str, pbar: tqdm.tqdm = None):
    try:
        # Dividir el user del password
        username = user.split(":")[0]
        url = f"https://www.roblox.com/user.aspx?username={username}"
        response = requests.get(url, timeout=5)
        pbar.update(1)

        # Si el código de respuesta es 200, entonces guardar el user
        if response.status_code == 200:
            print(Fore.GREEN + f"Found {username}")
            return user
        else:
          print(Fore.RED + f"Not found {username}")
          return None
    except Exception as e:
        return None

def hacer_solicitud(args):
    url, pbar = args
    response = requests.get(url)
    # Aquí puedes procesar la respuesta según tus necesidades
    pbar.update(1)
    print(f"Solicitud completada: True | {url}")

def main():
    TEXT_FILE: str = f"./text_files/text.txt"
    RESULT_FILE: str = f"./results/r.txt"

    # Leer archivo de texto
    with open(TEXT_FILE, "r") as f:
        text = f.readlines()
        usernames = [line.split(":")[0] for line in text]

    founded = []

    # Buscar si los usuarios existen
    with tqdm.tqdm(total=len(usernames)) as pbar:
        with concurrent.futures.ThreadPoolExecutor() as exe:
            resultados = list(exe.map(request, usernames))

            for i in resultados:
                if i is not None:
                    founded.append(i)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Utiliza executor.submit para realizar solicitudes en paralelo
            futures = [executor.submit(hacer_solicitud, (url, pbar)) for url in usernames]

            # Espera a que todas las solicitudes se completen
            concurrent.futures.wait(futures)

    print(founded)

    # Escribir users en archivo de salida
    with open(RESULT_FILE, "w") as f:
        for user in founded:
            f.write(user)

if __name__ == "__main__":
    main()
