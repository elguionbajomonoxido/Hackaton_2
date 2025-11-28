import sys
import analizador


def main():
    # Si se pasa la URL como argumento de línea de comandos, la usamos.
    if len(sys.argv) > 1:
        url = sys.argv[1].strip()
    else:
        url = input("Pega la URL a analizar: ").strip()

    if not url:
        print("No ingresaste URL.")
        return

    try:
        resultado = analizador.analizar_url(url)
        analizador.imprimir_resultado(resultado)
    except Exception as e:
        print("Error al analizar la URL:", e)


if __name__ == "__main__":
    main()
