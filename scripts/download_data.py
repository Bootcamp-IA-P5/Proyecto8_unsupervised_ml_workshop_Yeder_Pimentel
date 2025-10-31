# scripts/download_data.py
"""
Descarga el Mushroom Dataset desde el UCI Repository,
lo guarda en la carpeta ./data/, y lo convierte a un CSV listo para usar.

Uso:
    python scripts/download_data.py
"""

import os
import sys
from pathlib import Path
import pandas as pd

try:
    import requests
except ImportError:
    print("requests no instalado. Instálalo con: pip install requests")
    sys.exit(1)


# --- CONFIGURACIÓN ---
BASE_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/"
FILES = ["agaricus-lepiota.data", "agaricus-lepiota.names", "README"]

# Nombres de columnas según documentación del dataset
COLUMN_NAMES = [
    "class", "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
    "gill-attachment", "gill-spacing", "gill-size", "gill-color",
    "stalk-shape", "stalk-root", "stalk-surface-above-ring",
    "stalk-surface-below-ring", "stalk-color-above-ring",
    "stalk-color-below-ring", "veil-type", "veil-color", "ring-number",
    "ring-type", "spore-print-color", "population", "habitat"
]


def ensure_data_dir(path: Path):
    """Crea la carpeta ./data si no existe."""
    path.mkdir(parents=True, exist_ok=True)


def download_file(url: str, dest: Path):
    """Descarga un archivo de la web y lo guarda en la ruta especificada."""
    print(f"📥 Descargando {url} ...")
    r = requests.get(url, stream=True, timeout=30)
    r.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"✅ Guardado: {dest.name} ({dest.stat().st_size} bytes)")


def convert_to_csv(data_path: Path, csv_path: Path):
    """
    Convierte el archivo agaricus-lepiota.data en un CSV con nombres de columnas.
    """
    print("\n🧠 Convirtiendo agaricus-lepiota.data a mushrooms.csv ...")

    try:
        # Leemos el .data como si fuera un CSV (está separado por comas)
        df = pd.read_csv(data_path, header=None, names=COLUMN_NAMES)
        print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

        # Guardamos como CSV limpio
        df.to_csv(csv_path, index=False)
        print(f"✅ Archivo CSV creado: {csv_path}")
    except Exception as e:
        print(f"❌ Error al convertir a CSV: {e}")


def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    ensure_data_dir(data_dir)

    # --- 1️⃣ Descargar archivos ---
    for fname in FILES:
        url = BASE_URL + fname
        dest = data_dir / fname
        if not dest.exists():
            try:
                download_file(url, dest)
            except Exception as e:
                print(f"⚠️ Error descargando {fname}: {e}")
        else:
            print(f"ℹ️ {fname} ya existe, omitiendo descarga.")

    # --- 2️⃣ Convertir a CSV ---
    data_file = data_dir / "agaricus-lepiota.data"
    csv_file = data_dir / "mushrooms.csv"

    if data_file.exists():
        convert_to_csv(data_file, csv_file)
    else:
        print("❌ No se encontró agaricus-lepiota.data. Descarga fallida o conexión interrumpida.")


if __name__ == "__main__":
    main()
