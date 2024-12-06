import json, os
from funcoes import *

arquivoJSON = input('Digite o caminho completo do arquivo json: ')

if os.path.exists(arquivoJSON): # Verifica se o arquivo json informado existe
    with open(arquivoJSON, 'r') as arquivoJsonLeitura:
        lista_json = json.load(arquivoJsonLeitura) # Se existe, lê, carrega o conteúdo e adiciona na lista json
else:
    lista_json = [] # Se não, cria a lista json onde sera adicionado o dicionario com as informações

ipValidado = ''
while not 'valido' in ipValidado:
    ipDecimal = input('Digite o endereço IP: ')
    ipValidado = valIP(ipDecimal)
    print(ipValidado)

CIDRValidado = ''
while not 'valido' in CIDRValidado:
    try:
        mascaraCidrInicial = int(input('Digite a máscara de rede inicial (CIDR): '))
        mascaraCidrFinal = int(input('Digite a máscara de rede final (CIDR): '))
        CIDRValidado = valCIDR(mascaraCidrInicial, mascaraCidrFinal)
        print(CIDRValidado)
    except ValueError:
        print('\nErro: a máscara (CIDR) deve ser um valor numérico.')

for CIDR in range(mascaraCidrInicial, mascaraCidrFinal + 1):
    mascaraCidrAtual = (CIDR)
    mascaraBin = cidr2mascara(mascaraCidrAtual)
    ipBin = ip2bin(ipDecimal)
    ipRedeBin = bit2bitAND(ipBin, mascaraBin)
    ipBcBin = rede2bc(ipRedeBin, mascaraCidrAtual)
    primeiroHost = ipRedeBin[:-1] + '1'
    ultimoHost = ipBcBin[:-1] + '0'
    hostsValidos = (2 ** (32 - mascaraCidrAtual)) - 2

    print(f'\nPara máscara /{mascaraCidrAtual}: ')
    print(f'Endereço de Rede: {bin2dec(ipRedeBin)}')
    print(f'Primeiro Host: {bin2dec(primeiroHost)}')
    print(f'Último Host: {bin2dec(ultimoHost)}')
    print(f'Endereço de Broadcast: {bin2dec(ipBcBin)}')
    print(f'Máscara de Sub-rede: {bin2dec(mascaraBin)}')
    print(f'Máscara de Sub-rede (binário): {mascaraBin} ')
    print(f'Número de Hosts Válidos: {hostsValidos}\n')

    dic_json = {
        'CIDR': '/' + str(mascaraCidrAtual),
        'Endereco de Rede': bin2dec(ipRedeBin),
        'Primeiro Host': bin2dec(primeiroHost),
        'Ultimo Host': bin2dec(ultimoHost),
        'Endereco de Broadcast': bin2dec(ipBcBin),
        'Mascara de Sub-rede': bin2dec(mascaraBin),
        'Mascara de Sub-Rede (binario)': mascaraBin,
        'Hosts Validos': hostsValidos
    }

    lista_json.append(dic_json)

with open(arquivoJSON, 'w') as arquivoJsonEscrita:
    json.dump(lista_json, arquivoJsonEscrita, indent=4) # Salva a lista no arquivo json com 4 espaços de indentação