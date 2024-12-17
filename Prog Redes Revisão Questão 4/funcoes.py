import re

def valArquivoOrigem(nomeArquivoOrigem):
    try:
        with open(nomeArquivoOrigem, 'r') as arquivo:
            textoArquivoOrigem = arquivo.read()
            if textoArquivoOrigem:
                return 'valido', textoArquivoOrigem
            else:
                return 'Erro: O arquivo origem está vazio.', None
    except FileNotFoundError:
        return 'Erro: O arquivo origem fornecido não foi encontrado.', None

def valPalavraPasse(palavraPasse, textoArquivoOrigem):
    # Verifica se "palavraPasse" contém apenas letras e não está vazia
    if not re.match('^[a-z]+$', palavraPasse):
        return 'Erro: A palavra passe deve conter somente letras e não pode estar vazia.'
    # Verifica se o tamanho da palavra passe é menor ou igual ao conteúdo do arquivo origem
    if len(palavraPasse) > len(textoArquivoOrigem):
        return 'Erro: O tamanho da palavra passe deve ser menor ou igual ao conteúdo do arquivo origem.'
    return 'valido'