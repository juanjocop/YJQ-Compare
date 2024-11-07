# main.py
import argparse
from comparador import comparar_archivos
from output import mostrar_resultado

def main():
    parser = argparse.ArgumentParser(description="Comparador de archivos YAML/JSON")
    parser.add_argument("archivo1", help="Ruta del primer archivo JSON/YAML")
    parser.add_argument("archivo2", help="Ruta del segundo archivo JSON/YAML")
    parser.add_argument("--solo-estructura", action="store_true", help="Compara solo la estructura, ignorando valores")

    args = parser.parse_args()
    resultado = comparar_archivos(args.archivo1, args.archivo2, solo_estructura=args.solo_estructura)
    mostrar_resultado(resultado)

if __name__ == "__main__":
    main()
