import concurrent.futures
import requests

def hacer_solicitud(url, indice):
    response = requests.get(url)
    # Aquí puedes procesar la respuesta según tus necesidades
    print(f"Solicitud {indice + 1} completada: True | {url}")

def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Utiliza executor.submit para realizar solicitudes en paralelo
        futures = [executor.submit(hacer_solicitud, url, i) for i, url in enumerate(urls)]

        # Espera a que todas las solicitudes se completen
        concurrent.futures.wait(futures)

        

if __name__ == "__main__":
    main()
