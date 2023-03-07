import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')
    try:
        data = open(path_file, "r")
        return data.read().split('\n')
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
