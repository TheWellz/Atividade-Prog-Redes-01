import time
from tabulate import tabulate
from funcoes import calcularHash, findNonce  # Importa as funções do arquivo auxiliar

dataBitsLista = [
    ('Esse é fácil', [8, 10, 15]),
    ('Texto maior muda o tempo?', [8, 10, 15]),
    ('É possível calcular esse?', [18, 19, 20])
]

cabecalhos = ['Texto a validar', 'Bits em zero', 'Nonce', 'Tempo (em s)']
resultados = []

for dataToHash, bitsToBeZeroLista in dataBitsLista:
    for bitsToBeZero in bitsToBeZeroLista:
        nonce, tempoTotal = findNonce(dataToHash, bitsToBeZero)
        resultados.append([dataToHash, bitsToBeZero, nonce, f"{tempoTotal:.6f}"])

with open('Prog Redes Revisão Questão 2/tabela.txt', 'w', encoding='utf-8') as arquivoTxt:
    arquivoTxt.write(tabulate(resultados, headers=cabecalhos, tablefmt="grid"))

print(tabulate(resultados, headers=cabecalhos, tablefmt="grid"))
