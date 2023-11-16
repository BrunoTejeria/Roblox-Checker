import numpy as np
import json
import requests
import tqdm
import bs4 as bs
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

        print(Fore.LIGHTYELLOW_EX + "\n\n" + "#" * 64 + "\n")

        # Si el código de respuesta es 200, entonces guardar el user
        if response.status_code == 200:
            pbar.update(1)
            print(Fore.GREEN + f"Found {user}")

            # Buscar si se jugo el juego islands
            soup = bs.BeautifulSoup(response.text, 'html.parser')

            game = soup.find("a", {"href": "/games/4872321990/Islands"})
            if game is None:
                print(Fore.RED + f"Not found game {user}")
                return [user, False]
            else:
                print(Fore.GREEN + f"Found game {user}")
                return [user, True]
        else:
            print(Fore.RED + f"Not found {user}")
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
    with open(RESULT_FILE, "a") as f:
        with tqdm.tqdm(total=len(usernames), ncols=64, bar_format='{desc}: {percentage:3.0f}% | {n_fmt}/{total_fmt} [{elapsed}<{remaining} | ', colour='red') as pbar:

            for user in usernames:
                req = request(user, pbar)
                founded.append(req)
                if req is not None:
                    if req[1] == True:
                        f.write(req + "\n")

        print(founded)

if __name__ == "__main__":
    main()
