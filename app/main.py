def copy_file(command: str) -> None:
    parts = command.split()

    # Verifica se o comando está no formato correto
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts

    # Não faz nada se os nomes forem iguais
    if source == destination:
        return

    try:
        # Abre os dois arquivos ao mesmo tempo
        with open(source, "r", encoding="utf-8") as file_in, \
                open(destination, "w", encoding="utf-8") as file_out:

            # Copia o conteúdo
            file_out.write(file_in.read())

    except FileNotFoundError:
        # Caso o arquivo de origem não exista, não faz nada
        pass
