# ==========================================
# PROYECTO: PIC2 Surveillance System
# AUTOR: Oscar GR (@OscarGr2004)
# FECHA: Noviembre 2025
# DESCRIPCIÓN: Sistema de vigilancia táctico con Docker y RPi Zero 2 W.
# LICENCIA: MIT License
# ==========================================from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
import shutil
from datetime import datetime
import threading

app = Flask(__name__)
CORS(app)

DATA_DIR = "/app/data"
CAPTURES_DIR = os.path.join(DATA_DIR, "evidencia")

if not os.path.exists(CAPTURES_DIR):
    os.makedirs(CAPTURES_DIR)

@app.route('/data/<path:filename>')
def serve_image(filename):
    return send_from_directory(DATA_DIR, filename)

@app.route('/api/snapshot', methods=['POST'])
def snapshot():
    try:
        source = os.path.join(DATA_DIR, "live_feed.jpg")
        
        if not os.path.exists(source):
            return jsonify({"status": "error", "msg": "Sin señal de video"}), 404
            
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"PIC2_EVIDENCIA_{timestamp}.jpg"
        destination = os.path.join(CAPTURES_DIR, filename)
        
        shutil.copy2(source, destination)
        
        return jsonify({"status": "ok", "file": filename})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__ == '__main__':
    print("Iniciando Backend Multihilo...")
    # threaded=True es vital
    app.run(host='0.0.0.0', port=5000, threaded=True)
