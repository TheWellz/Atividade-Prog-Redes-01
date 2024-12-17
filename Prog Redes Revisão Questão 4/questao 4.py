from funcoes import *

# Validação do arquivo origem
arquivoOrigemValido = ''
while arquivoOrigemValido != 'valido':
    nomeArquivoOrigem = input('Digite o caminho completo do arquivo origem (a ser lido): ')
    arquivoOrigemValido, textoArquivoOrigem = valArquivoOrigem(nomeArquivoOrigem)
    print(arquivoOrigemValido)

# Validação da palavra passe
palavraPasseValido = ''
while palavraPasseValido != 'valido':
    palavraPasse = input('Digite a palavra passe: ')
    palavraPasseValido = valPalavraPasse(palavraPasse, textoArquivoOrigem)
    print(palavraPasseValido)

nomeArquivoDestino = input('Digite o caminho completo do arquivo destino (a ser criado/modificado): ')
textoArquivoDestino = ''

for indiceOrigem, letraOrigem in enumerate(textoArquivoOrigem):

    letraPasseIndice = indiceOrigem % len(palavraPasse) # Calculo para gerar o loop das letras da palavra passe
    letraOrigemASCII = ord(letraOrigem)
    letraPasseASCII = ord(palavraPasse[letraPasseIndice])
    resultadoXOR = letraOrigemASCII ^ letraPasseASCII
    textoArquivoDestino += bin(resultadoXOR)[2:] # Passa o resultado do XOR em decimal para binário

# Cria o arquivo (se não existir) ou adiciona o conteúdo (se existir)
with open(nomeArquivoDestino, 'a') as arquivoDestino:
    arquivoDestino.write(textoArquivoDestino + '\n\n')