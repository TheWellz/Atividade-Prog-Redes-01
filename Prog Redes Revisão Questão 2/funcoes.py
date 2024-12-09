from time import time
from hashlib import sha256

def calcularHash(nonce, dataToHash):
    nonceDataCombinada = f"{nonce}{dataToHash}".encode('utf-8')  # Converte o Nonce + Data em string para bytes
    hashHexadecimal = sha256(nonceDataCombinada).hexdigest()  # Calcula o Hash e retorna em hexadecimal
    hashBinario = ''
    for digito in hashHexadecimal:  # Converte cada dígito em hexadecimal para 4 bits em binário
        hashBinario += bin(int(digito, 16))[2:].zfill(4)
    return hashBinario

def findNonce(dataToHash, bitsToBeZero):
    zeroPrefixo = '0' * bitsToBeZero
    nonce = 0
    nonceLimite = 2**32 - 1  # Valor máximo de 4 bytes
    inicio = time()  # Início da contagem

    while nonce <= nonceLimite:
        resultadoHash = calcularHash(nonce, dataToHash)

        if resultadoHash.startswith(zeroPrefixo):  # Verifica se o hash começa com o prefixo de zeros
            fim = time()  # Fim da contagem
            tempoTotal = fim - inicio
            return nonce, tempoTotal
        
        nonce += 1
        
    fim = time()  # Fim da contagem
    tempoTotal = fim - inicio
    return 'Limite de 4 bytes excedido.', tempoTotal