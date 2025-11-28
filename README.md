# hackea-fakenews

Proyecto demo: analizador simple para detectar titulares/URLs potencialmente falsos.

Contiene:
- `Main.py` — GUI PyQt5 para analizar una URL (usa VirusTotal API en `analizador.py`).
- `analizador.py` — llamadas a VirusTotal y funciones de análisis.
- `main.py` — versión alternativa (sin GUI) si prefieres CLI.

Cómo ejecutar (Windows PowerShell):

```powershell
C:/Users/isaia/AppData/Local/Programs/Python/Python314/python.exe Main.py
```

Advertencias:
- `analizador.py` contiene una `API_KEY` embebida para VirusTotal. Revisa la cuota/privacidad antes de publicar en repositorios públicos.
