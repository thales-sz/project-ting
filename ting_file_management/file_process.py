import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            data = txt_importer(path_file)
            file = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(data),
                "linhas_do_arquivo": data,
            }
            instance.enqueue(file)
            sys.stdout.write(str(file))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
