import numpy as np
import json
import time
import requests
import tqdm
import bs4 as bs
from colorama import Fore













"""def read_config():
    with open("checker/config.json", "r") as f:
        return json.load(f)"""

def request(user: str, pbar: tqdm.tqdm = None):
    try:

        print(Fore.LIGHTYELLOW_EX + "\n\n" + "#" * 64 + "\n")
        # Dividir el user del password
        username: str = user.split(":")[0]

        URL_LOGIN: str = f"https://www.roblox.com/user.aspx?username={username}"


        response = requests.get(URL_LOGIN)

        # Si el código de respuesta es 200, entonces guardar el user
        if response.status_code == 200:

            pbar.update(1)
            print(Fore.GREEN + f"Found {user}")
            # Obtener el user id
            user_id = response.url.split("users/")[1].split("/")[0]
            favorites = get_favorite_games(user_id)

            if "https://www.roblox.com/games/4872321990/Islands" in favorites and "https://www.roblox.com/games/920587237/Adopt-Me" in favorites:
                print(Fore.BLUE + f"Found game {user + " | Adopt-me, Islands"}")
                return [user, True, "adopt-me", "islands"]
            elif "https://www.roblox.com/games/920587237/Adopt-Me" in favorites:
                print(Fore.BLUE + f"Found game {user + " | Adopt-me"}")
                return [use, True, "adopt-me"]
            elif "https://www.roblox.com/games/4872321990/Islands" in favorites:
                print(Fore.BLUE + f"Found game {user + " | Islands"}")
                return [user, True, "islands"]
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

def get_favorite_games(user_id: str):

    URL_FAVORITES: str = f"https://www.roblox.com/users/favorites/list-json?assetTypeId=9&itemsPerPage=999&pageNumber=1&userId={user_id}"
    results = np.array([])
    search = ["https://www.roblox.com/games/4872321990/Islands", "https://www.roblox.com/games/920587237/Adopt-Me"]

    favorites: dict = requests.get(URL_FAVORITES).json()

    index: dict = favorites["Data"]["TotalItems"] - 3

    for i in range(index):
        data: dict = favorites["Data"]["Items"][i]["Item"]["AbsoluteUrl"]
        if data in search:
            results = np.append(results, data)
    return results




def main():
    TEXT_FILE: str = f"./text_files/text.txt"
    RESULT_FILE_ISLANDS: str = f"./results/Islands.txt"
    RESULT_FILE_ADOPT_ME: str = f"./results/Adopt-me.txt"
    RESULT_FILE: str = f"./results/All.txt"

    #t1 = time.time()

    # Leer archivo de texto
    with open(TEXT_FILE, "r") as f:
        usernames = f.readlines()

    #t2 = time.time()
    #print(f"Time to read file: {t2 - t1}")

    founded_all = np.array([])
    founded_islands = np.array([])
    founded_adopt_me = np.array([])

    # Buscar si los usuarios existen
    with open(RESULT_FILE_ADOPT_ME, "a") as adopt_me:
        with open(RESULT_FILE_ISLANDS, "a") as islands:
            with open(RESULT_FILE, "a") as f:
                with tqdm.tqdm(total=len(usernames), ncols=64, bar_format='{desc}: {percentage:3.0f}% | {n_fmt}/{total_fmt} [{elapsed}<{remaining} | ', colour='red') as pbar:

                    for user in usernames:
                        req = request(user, pbar)

                        if req is not None:
                            if req[1] == True:
                                if req[2] == "adopt-me":
                                    np.append(founded_adopt_me, req[0])
                                    adopt_me.write(req[0])
                                elif req[2] == "islands":
                                    np.append(founded_islands, req[0])
                                    islands.write(req[0])
                                else:
                                    np.append(founded_all, req[0])
                                    f.write(req[0])


if __name__ == "__main__":
    main()
