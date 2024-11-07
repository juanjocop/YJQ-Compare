# comparador.py
import yaml
import json
from deepdiff import DeepDiff

def cargar_archivo(ruta):
    if ruta.endswith(".yaml") or ruta.endswith(".yml"):
        with open(ruta, 'r') as f:
            return yaml.safe_load(f)
    elif ruta.endswith(".json"):
        with open(ruta, 'r') as f:
            return json.load(f)
    else:
        raise ValueError("Formato de archivo no soportado. Usa JSON o YAML.")

def comparar_archivos(ruta1, ruta2, solo_estructura=False):
    data1 = cargar_archivo(ruta1)
    data2 = cargar_archivo(ruta2)

    diff = DeepDiff(data1, data2, ignore_order=True)
    if solo_estructura:
        diff = {key: val for key, val in diff.items() if key in ['dictionary_item_added', 'dictionary_item_removed']}
    return diff
