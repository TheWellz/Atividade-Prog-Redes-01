import re

# Valida o endereço IP.
def valIP(ipDecimal: str):
    if not re.match('^[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+$', ipDecimal): # Função 'regex' que verifica se a string tem 4 grupos númericos separados por 3 pontos.
        return '\nErro: Formato de IP inválido, insira um valor com essa formatação (X.X.X.X)'
    ipDecimalLista = ipDecimal.split('.')
    if not all(int(numero) >= 0 and int(numero) <= 255 for numero in ipDecimalLista): # Função 'all' retorna True se todos os números estiverem entre 0 e 255.
        return '\nErro: Endereço IP inválido, cada octeto deve estar entre 0 e 255.'
    else:
        return 'valido'

# Valida a mascara (CIDR).
def valCIDR(mascaraCidrInicial: int, mascaraCidrFinal: int):
    if not 0 <= mascaraCidrInicial <= 32 or not 0 <= mascaraCidrFinal <= 32:  # Verifica se o valor CIDR inicial e final estão entre 0 e 32
        return '\nErro: Máscara inválida, o valor da máscara (CIDR) deve estar entre 0 e 32.'     
    if not mascaraCidrInicial <= mascaraCidrFinal:
        return '\nErro: Máscara inválida, a máscara (CIDR) inicial deve ser menor ou igual a final.'
    else:
        return 'valido'

# Converte um endereço IP de decimal para binário.
def ip2bin(ipDecimal: str): # Recebe uma lista com os octetos em base decimal de um IP
    ipDecimalLista = ipDecimal.split('.')
    ipBinario = ''
    for octeto in ipDecimalLista:
        octeto8bit = bin(int(octeto))[2:].zfill(8) # Converte, remove o prefixo "0b" e Preenche com zeros a esquerda até ter 8 bits
        ipBinario += octeto8bit + '.'
    return ipBinario[:-1]

# Converte uma máscara no formato CIDR para uma máscara binária.
def cidr2mascara(mascaraCIDR: str):
    mascaraBinSemPontos = '1' * int(mascaraCIDR) + '0' * (32 - int(mascaraCIDR))
    mascaraBin = ''
    for octeto in range(0, len(mascaraBinSemPontos), 8): # Itera do inicio até 32 bits, pulando em octetos
        mascaraBin += mascaraBinSemPontos[octeto:octeto + 8] + '.' # Formata a mascara adicionando os octetos com ponto
    return mascaraBin[:-1]

# Converte um endereço IP/Mascara de binário para decimal.
def bin2dec(valorBin: str):
    valorBinLista = valorBin.split('.')
    valorDec = ''
    for octeto in valorBinLista:
        octetoDec = int(octeto, 2)
        valorDec += str(octetoDec) + '.'
    return valorDec[:-1]

# Calcula o endereço de rede a partir de um endereço IP binário e uma máscara binária.
def bit2bitAND(ipBin: str, mascaraBin: str):
    ipBinLista = ipBin.split('.')
    mascaraBinLista = mascaraBin.split('.')
    ipRedeBin = ''
    for octetoIP, octetoMascara in zip(ipBinLista, mascaraBinLista): # Percorre cada par de octetos nos valores binarios
        for bitIP, bitMascara in zip(octetoIP, octetoMascara): # Percorre cada par de bits nos octetos
            if bitIP == '1' and bitMascara == '1':
                ipRedeBin += '1'
            else:
                ipRedeBin += '0'
        ipRedeBin += '.'
    return ipRedeBin[:-1]

# Calcula o endereço de broadcast a partir do endereço de rede e a CIDR atual.
def rede2bc(ipRedeBin: str, mascaraCidrAtual: int):
    redeBinLista = ipRedeBin.split('.')
    ipBcSemPonto = ''.join(redeBinLista) # Junta os octetos em uma string com 32 bits
    ipBcBin = ipBcSemPonto[:mascaraCidrAtual] + "1" * (32 - mascaraCidrAtual)
    ipBcBin = ipBcBin[:8] + '.' + ipBcBin[8:16] + '.' + ipBcBin[16:24] + '.' + ipBcBin[24:32]
    return ipBcBin