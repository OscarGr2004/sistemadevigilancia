# 👁️ PIC2 - Sistema de Vigilancia Táctico

> Sistema de vigilancia modular basado en Docker para Raspberry Pi Zero 2 W, con interfaz estilo HUD Cyberpunk.

![Status](https://img.shields.io/badge/Status-Operational-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Platform](https://img.shields.io/badge/Platform-Raspberry_Pi-red)

## 🚀 Características
- **Arquitectura Dockerizada:** Separación limpia entre Frontend (Nginx), Backend (Flask) y Detector (Python).
- **Zero-Dependency Camera Access:** Uso de `nsenter` para saltar conflictos de GLIBC/NumPy en ARM.
- **Interfaz OSCAR GR:** Diseño UI responsivo con estética hacker/militar.
- **Modo Evidencia:** Captura y almacenamiento de snapshots sin interrumpir el video.
- **Descarga Local:** Bajada directa de evidencia al dispositivo cliente.

## 🛠️ Stack Tecnológico
- **Hardware:** Raspberry Pi Zero 2 W + RPi Camera Module.
- **OS:** Raspberry Pi OS (Bookworm).
- **Backend:** Python 3.9, Flask (Multithreaded).
- **Frontend:** HTML5, CSS3 (Variables), Vanilla JS.
- **Container:** Docker Compose.

## ⚙️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/pic2-surveillance.git](https://github.com/tu-usuario/pic2-surveillance.git)
   cd pic2-surveillance
   ```
Configurar permisos:

```bash
mkdir data
sudo chmod -R 777 data
```
Desplegar:

```bash
sudo docker compose up -d --build
```
📝 Créditos
Desarrollado por Oscar GR.

---

### CARPETA: `motion-detector/`

### 3. Archivo: `motion-detector/Dockerfile`

```dockerfile
FROM python:3.9-slim-bookworm

# Instalar util-linux para tener 'nsenter'
RUN apt-get update && apt-get install -y \
    util-linux \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# No necesitamos librerías pesadas, solo lo básico
COPY motion_detector.py .

CMD ["python", "motion_detector.py"]
```