# herramientas.py - Módulo de utilidades y gestión de datos locales
import json
import os
import subprocess

ARCHIVO_REGISTROS = "registros_apiario.json"

def cargar_registros():
    """Carga la lista de registros de colmenas desde un JSON local."""
    if not os.path.exists(ARCHIVO_REGISTROS):
        return []
    try:
        with open(ARCHIVO_REGISTROS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar registros: {e}")
        return []

def guardar_memoria_local(texto):
    """Guarda un registro o bitácora de decisión en el archivo local."""
    registros = cargar_registros()
    registros.append({"log": texto})
    try:
        with open(ARCHIVO_REGISTROS, "w", encoding="utf-8") as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error al guardar memoria: {e}")

def ver_estado_dispositivo():
    """Consulta la batería del teléfono mediante termux-battery-status si está disponible."""
    try:
        resultado = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True,
            timeout=3
        )
        if resultado.returncode == 0 and resultado.stdout:
            datos = json.loads(resultado.stdout)
            porcentaje = datos.get("percentage", "N/A")
            estado = datos.get("status", "OK")
            return f"Batería: {porcentaje}% ({estado})"
    except Exception:
        pass
    return "Estado Dispositivo: OK (Termux Standby)"
