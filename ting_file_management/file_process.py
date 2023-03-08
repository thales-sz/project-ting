import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def file_exists(path_file, instance: Queue):
    for i in range(len(instance)):
        return instance.search(i)["nome_do_arquivo"] == path_file


def process(path_file, instance: Queue):
    if not file_exists(path_file, instance):
        data = txt_importer(path_file)
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
        instance.enqueue(file)
        sys.stdout.write(str(file))


def remove(instance: Queue):
    try:
        file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file} removido com sucesso\n")
    except IndexError:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
