import numpy as np
import json
import time
import requests
import tqdm
import bs4 as bs
from colorama import Fore

import concurrent.futures


def get_favorite_games(user_id: str):
    results = np.array([])
    search = ["https://www.roblox.com/games/4872321990/Islands", "https://www.roblox.com/games/920587237/Adopt-Me"]
    url = f"https://www.roblox.com/users/favorites/list-json?assetTypeId=9&itemsPerPage=999&pageNumber=1&userId={user_id}"


    print(Fore.GREEN + f"Found {user_id}")
    favorites = requests.get(url).json()
    print(favorites)

    index = favorites["Data"]["TotalItems"] - 3
    print(index)

    for i in range(index):
        data = favorites["Data"]["Items"][i]["Item"]["AbsoluteUrl"]
        print(data)
        if data in search:
            print(f"Found: {data}")
            results.append(data)










def read_config():
    with open("checker/config.json", "r") as f:
        return json.load(f)

def request(user: str, pbar: tqdm.tqdm = None):
    try:

        print(Fore.LIGHTYELLOW_EX + "\n\n" + "#" * 64 + "\n")
        # Dividir el user del password
        username = user.split(":")[0]
        url = f"https://www.roblox.com/user.aspx?username={username}"

        response = requests.get(url)

        # Si el código de respuesta es 200, entonces guardar el user
        if response.status_code == 200:
            pbar.update(1)

            # Obtener el user id
            user_id = response.url.split("users/")[1].split("/")[0]
            favorites = get_favorite_games(user_id)

            if "" in favorites and "" in favorites:
                print(Fore.GREEN + f"Found game {user + " | Adopt-me, Islands"}")
                return [user + " | Adopt-me, Islands", True]
            else:
                print(Fore.RED + f"Not found game {user}")
                return [user, False]
        else:
            print(Fore.RED + f"Not found {user}")
            pbar.update(1)
            return None

    except Exception as e:
        print(e)
        return None

def main():
    TEXT_FILE: str = f"./text_files/text.txt"
    RESULT_FILE: str = f"./results/r.txt"

    t1 = time.time()
    # Leer archivo de texto
    with open(TEXT_FILE, "r") as f:
        usernames = f.readlines()
    t2 = time.time()
    print(f"Time to read file: {t2 - t1}")
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


if __name__ == "__main__":
    main()
