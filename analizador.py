import requests
# APi-Key por cuenta,
API_KEY = "5ac5758d7316dfaf83261ef82fc13afd38a0bd64a39cc06330e6ab398d866575"
VT_URL = "https://www.virustotal.com/api/v3/urls"

def analizar_url_virustotal(url: str):
    resp = requests.post(
        VT_URL,
        headers={"x-apikey": API_KEY},
        data={"url": url},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()

    analysis_id = data["data"]["id"]

    detalle = requests.get(
        f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
        headers={"x-apikey": API_KEY},
        timeout=10,
    ).json()

    stats = detalle["data"]["attributes"]["stats"]

    return stats


def analizar_url(url: str):
    return analizar_url_virustotal(url)

def imprimir_resultado(resultado):
    # Imprime en consola un resultado devuelto por las funciones del analizador.
    if not isinstance(resultado, dict):
        print(resultado)
        return

    tipo = resultado.get('type')
    if tipo == 'titular':
        print('\n== Resultado (Titular) ==')
        print('Texto:', resultado.get('text'))
        print('Longitud:', resultado.get('length'))
        print('Palabras sospechosas:', resultado.get('suspicious_words'))
        print('Puntuación (0..1):', resultado.get('score'))
    else:
        # Asumimos que es resultado de URL (stats de VirusTotal) o similar
        print('\n== Resultado (URL / Datos) ==')
        try:
            for k, v in resultado.items():
                print(f"{k}: {v}")
        except Exception:
            print(resultado)
