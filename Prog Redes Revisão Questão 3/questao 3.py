import random , re
from colorama import Fore, Style, init
init()

palavrasLista = []
nomeArquivoPalavras = input('Digite o caminho completo do arquivo de palavras (a ser lido): ')

try:
    with open(nomeArquivoPalavras, 'r') as arquivoPalavras:
        for linha in arquivoPalavras:  # Itera sobre cada linha do arquivo obtendo a palavra
            palavra = linha.strip()  # Remove os espaços em branco e as quebras de linhas
            if 5 <= len(palavra) <= 8 and palavra.isalpha(): # Verifica se tem apenas letras, entre 5 e 8 caracteres
                palavrasLista.append(palavra.lower())

        if not palavrasLista:
            print("\nErro: Nenhuma palavra foi encontrada na lista.")
            exit()

except FileNotFoundError:
    print('\nErro: O arquivo fornecido não foi encontrado.')
    exit()

palavraSorteada = random.choice(palavrasLista)
numTentativas = 0

print(f'A palavra sorteada tem {len(palavraSorteada)} letras')

while numTentativas < 6:
    palavraTentativa = input(f'\nEscolha uma palavra com {len(palavraSorteada)} letras: ').lower()

    if palavraTentativa == palavraSorteada:
        print(f'\nParabéns! Você acertou a palavra: "{palavraSorteada}", em {numTentativas + 1} tentativa(s)')
        break

    if re.match('^[a-z]+$', palavraTentativa): # Verifica se a "palavraTentativa" contem apenas letras
        if len(palavraTentativa) == len(palavraSorteada):
            feedback = ''

            for letraPT, letraPS in zip(palavraTentativa, palavraSorteada): # Itera sobre cada letra da palavra de tentativa e a sorteada
                if letraPT == letraPS:
                    feedback += ('|' + Fore.GREEN + letraPT + Style.RESET_ALL) # Adiciona a letra em verde ao feedback indicando posição correta.
                elif letraPT != letraPS and letraPT in palavraSorteada:
                    feedback += ('|' + Fore.YELLOW + letraPT + Style.RESET_ALL) # Adiciona a letra em amarelo ao feedback indicando que está na palavra numa posição incorreta.
                elif letraPT not in palavraSorteada:
                    feedback += '|' + letraPT # Adiciona a letra sem cor ao feedback indicando que não está na palavra sorteada.

            numTentativas += 1
            print(f'Tentativa numero: {numTentativas}')
            print(feedback + '|')

        else:
            print('Erro: Sua palavra de tentativa tem um tamanho diferente da sorteada.')
    else:
        print('Erro: o input de tentativa deve conter somente letras.')

if numTentativas == 6:
    print(f'\nVocê não acertou em 6 tentativas. A palavra era: "{palavraSorteada}"')
