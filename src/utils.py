# utils.py

import os

def ensure_export_folder(path="exports"):
    os.makedirs(path, exist_ok=True)