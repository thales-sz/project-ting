from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = list()
    for index in range(len(instance)):
        file = instance.search(index)
        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line in range(file["qtd_linhas"]):
            if word.lower() in file["linhas_do_arquivo"][line].lower():
                data["ocorrencias"].append({"linha": line + 1})

        if len(data["ocorrencias"]):
            result.append(data)
    return result


def search_by_word(word, instance: Queue):
    """Aqui irá sua implementação"""
