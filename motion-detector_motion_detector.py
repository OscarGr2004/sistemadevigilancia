import time
import os
import subprocess
import sys

# Ruta donde se guarda la imagen en el HOST
# Ajusta esto si tu usuario no es 'oscargr'
HOST_IMAGE = "/home/oscargr/proyecto-vigilancia/data/live_feed.jpg"

print(f"[INFO] Iniciando STREAMING ESTABLE (PIC2)...", flush=True)

def take_photo():
    cmd = [
        "nsenter", "-t", "1", "-m", "-u", "-n", "-i",
        "/usr/bin/rpicam-still", 
        "-o", HOST_IMAGE, 
        "--width", "640", 
        "--height", "480", 
        "-q", "50",       # Calidad media
        "-t", "1",        # Tiempo de captura
        "-n",             # Sin previsualización
        "--immediate"
    ]
    
    try:
        # Timeout de 20s para evitar congelamientos en Pi Zero
        subprocess.run(cmd, check=True, timeout=20)
        return True
    except subprocess.TimeoutExpired:
        print(" [LENTO] ", end="", flush=True)
        return False
    except Exception:
        return False

while True:
    if take_photo():
        print(".", end="", flush=True) 
    else:
        print("x", end="", flush=True)
    
    time.sleep(0.5)