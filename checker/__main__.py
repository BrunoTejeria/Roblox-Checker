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
        

        # Si el código de respuesta es 200, entonces guardar el user
        if response.status_code == 200:
            print(Fore.GREEN + f"Found {username}")
            pbar.update(1)
            return user
        else:
          print(Fore.RED + f"Not found {username}")
          pbar.update(1)
          return None
        
    except Exception as e:
        return None

def main():
    TEXT_FILE: str = f"./text_files/text.txt"
    RESULT_FILE: str = f"./results/r.txt"

    # Leer archivo de texto
    with open(TEXT_FILE, "r") as f:
        text = f.readlines()
        usernames = [line.split(":")[0] for line in text]

    founded = []

    # Buscar si los usuarios existen
    with open(RESULT_FILE, "w") as f:
        with tqdm.tqdm(total=len(usernames), ncols=64, bar_format='{desc}: {percentage:3.0f}% | {n_fmt}/{total_fmt} [{elapsed}<{remaining} | ', colour='red') as pbar:

            for user in usernames:
                req = request(user, pbar)
                founded.append(req)
                if req != None:
                    f.write(req + "\n")

            for i in resultados:
                if i is not None:
                    founded.append(i)
            



        print(founded)

if __name__ == "__main__":
    main()
