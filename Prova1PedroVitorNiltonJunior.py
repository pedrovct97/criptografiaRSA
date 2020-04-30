'''
Prova 1 de Aplicações e Serviços da Web

Pedro Vitor Coelho Teixeira
Nilton Fagundes Junior
'''

from os import system

a = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 1, 10, 6, 12, 11, 9, 5, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

b = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

c = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

d = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

e = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

f = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

g = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

h = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2,  8, 24, 14, 32, 27,  3,  9, 19, 13, 30, 6, 22, 11, 4, 25]

#Função Menu de cifragem
def rModo():
    while True:
        mode = input('[C] Cifrar, [D] Decifrar ou [S] Sair? \n')
        if mode == 'c' or mode == 'C' or mode == 'Cifrar' or mode == 'd' or mode == 'D' or mode == 'Decifrar' or mode == 'S' or mode == 's' or mode == 'Sair':
            return mode
        else:
            print('Error 404, try again!')

#Caso o usuario escolha criptografar por meio da TABELAS1
def tabelaS1():
    chave = input('Insira qual chave você deseja, as opções são a, b, c, d, e, f, g, h: ') #Insere em qual tabela deseja embaralhar seu numero
    dado = str(input('Digite o número que deseja binario em 6 digitos: ')) #digita um numero binario de 6 bits que depois de passar na tabelaS1 vai retornar 4 bits
    #Declara que meu primeiro e ultimo bit do numero inserido serão a informação de qual linha irei utilizar da tabela selecionada
    inicio = dado[0]
    fim = dado[5]
    #Pega os 4 bits do meio que serão minha posição dentro da linha que esta na tabela
    num = int(dado[1:5], 2)

#Se o usuario escolher alguma das chaves informadas ateriormente vai realizar uma operação de percorrer minha tabela.
    #Como o usuario vai ter inserido em qual linha o valor vai se encontrar, ele somente vai percorrer as colunas de acordo com a posicao (decimal) informada pelos 4 bits binários
    if chave == 'a' or chave == 'A':
        if inicio == '0' and fim == '0':
            resultado = a[0][num]
        elif inicio == '0' and fim == '1':
            resultado = a[1][num]
        elif inicio == '1' and fim == '0':
            resultado = a[2][num]
        elif inicio == '1' and fim == '1':
            resultado = a[3][num]

    elif chave == 'b' or chave == 'B':
        if inicio == '0' and fim == '0':
            resultado = b[0][num]
        elif inicio == '0' and fim == '1':
            resultado = b[1][num]
        elif inicio == '1' and fim == '0':
            resultado = b[2][num]
        elif inicio == '1' and fim == '1':
            resultado = b[3][num]

    elif chave == 'c'or chave == 'C':
        if inicio == '0' and fim == '0':
            resultado = c[0][num]
        elif inicio == '0' and fim == '1':
            resultado = c[1][num]
        elif inicio == '1' and fim == '0':
            resultado = c[2][num]
        elif inicio == '1' and fim == '1':
            resultado = c[3][num]

    elif chave == 'd' or chave == 'D':
        if inicio == '0' and fim == '0':
            resultado = d[0][num]
        elif inicio == '0' and fim == '1':
            resultado = d[1][num]
        elif inicio == '1' and fim == '0':
            resultado = d[2][num]
        elif inicio == '1' and fim == '1':
            resultado = d[3][num]

    elif chave == 'e' or chave == 'E':
        if inicio == '0' and fim == '0':
            resultado = e[0][num]
        elif inicio == '0' and fim == '1':
            resultado = e[1][num]
        elif inicio == '1' and fim == '0':
            resultado = e[2][num]
        elif inicio == '1' and fim == '1':
            resultado = e[3][num]

    elif chave == 'f' or chave == 'F':
        if inicio == '0' and fim == '0':
            resultado = f[0][num]
        elif inicio == '0' and fim == '1':
            resultado = f[1][num]
        elif inicio == '1' and fim == '0':
            resultado = f[2][num]
        elif inicio == '1' and fim == '1':
            resultado = f[3][num]

    elif chave == 'g' or chave == 'G':
        if inicio == '0' and fim == '0':
            resultado = g[0][num]
        elif inicio == '0' and fim == '1':
            resultado = g[1][num]
        elif inicio == '1' and fim == '0':
            resultado = g[2][num]
        elif inicio == '1' and fim == '1':
            resultado = g[3][num]

    elif chave == 'h' or chave == 'H':
        if inicio == '0' and fim == '0':
            resultado = h[0][num]
        elif inicio == '0' and fim == '1':
            resultado = h[1][num]
        elif inicio == '1' and fim == '0':
            resultado = h[2][num]
        elif inicio == '1' and fim == '1':
            resultado = h[3][num]
    else:
        print('Voce não digitou uma opção correta!')

    print(resultado)

def tabelaP():
        resultado = ""
        dado = str(input('Digite um número binário com 32 digitos: \n'))
        for i in P:
            nump = dado[i - 2]
            resultado += nump
        print('O valor inserido foi: ', dado, '\nO valor permutado ficou: ', resultado)

#Funcao para descobrir se o valor p que o usuario digitou é primo ou não e porquê
def numPrimo(n):
    tot = 0
    for i in range(1, n + 1):
        if n % i == 0: #Pega somente os valores em que o resto da divisão de (n / i) seja = 0
            print('\033[33m', end='') #Ele printa os numeros que possuem resto da divisao 0 em amarelo
            tot += 1 #me mostra a quantidade de divisores que o numero possui

        else: #Pega todos os outros valores em que a o resto da divisão seja != 0
            print('\033[31m', end='') #Ele printa qualquer numero que o resto da divisao seja != 0 de vermelho

        print('{} '.format(i), end='') #Imprime todos meus numeros

    print('\033[mO numero {} foi divisível {} vezes'.format(n, tot)) #Informa quantas vezes o numero foi divisível

#Mesmo que o 2 seja primo, ele vai solicitar que insira outro pois irá afetar no resultado
    if n == 2 and tot == 2:
        print('Ele é primo! Mas recomendo usar outro, pois se usar o 2 afetará o funcionamento do programa!')
        return False

    elif tot == 2: #Se o o numero tiver somente 2 divisores ele é primo
        print('Ele e primo!\n')
        return True

    else: #Se ele tiver < ou > 2 divisores ele não é primo
        print('Ele nao e primo!\n')
        return False

#Função para cifrar minha mensagem de acordo com os valores encontrados pela funcao RSA
def CifrarRSA(x,n):
    system('cls')
    C = 0
    P = input('Digite uma palavra ou texto a ser cifrado: ')
    print('O texto {} cifrado é:'.format(P))
    for i in P:
        if 'A' <= i <= 'Z':
            C = (ord(i)**x) % n
            print(' {} '.format(C), end='')

        elif 'a' <= i <= 'z':
            C = (ord(i)**x) % n
            print(' {} '.format(C), end='')
#se o character digitado foi um '(space)' ele vai definir como numero inteiro 32 (o python não reconhece o '(space)' para converter em ASCII)
        elif i == ' ':
            C = (32**x) % n
            print(' {} '.format(C), end='')
        else:
            C = i
    print('\n\n')

#Função para decifrar minha mensagem de acordo com os valores encontrados pela funcao RSA e minha chave secreta selecionada
def DecifrarRSA(y,n):
    system('cls')
    P = 0
    C = input('Digite o texto a ser decifrado: ')
    x = C.split() #Como estou digitando uma string, esta funcao vai transformar meu X em um vetor
    x = [int(i) for i in x] #Como eu inseri uma string e meu vetor é de strings, esta funcao vai percorrer o vetor e transformar todos meus dados em inteiro
    print('\nSeu texto decifrado é: ')
    for i in x:
        if i > 1:
            P = (i ** y) % n
            #32 e '(space)' na tabela ASCII
            if P == 32:
                print(chr(P), end='')
            else:
                print('{}'.format(chr(P)), end = '')
        else:
            P = i
    print('\n')

#algoritmo RSA
def RSA():

    print('\nDigite 2 numeros primos para gerar as chaves de criptografia.\nPara um numero ser primo ele deve ser somente divisivel por ELE MESMO ou por 1')
    p = int(input('Insira um numero primo: '))
    q = int(input('Insira outro numero primo: '))
    primo1 = numPrimo(p) #Funcao para descobrir se o primeiro valor p que o usuario digitou é primo ou não
    primo2 = numPrimo(q) #Funcao para descobrir se segundo o valor p que o usuario digitou é primo ou não
    #caso algum dos dois não seja primo, ele vai pedir que insira outro valor e ira efetuar o mesmo procedimento novamente para garantir que os novos sejam primos
    while (primo1 == False or primo2 == False):
        print('\nVoce digitou um valor não primo ou o número 2 que afeta o funcionamento do programa!')

        if primo1 == False:
            print('Para um numero ser primo ele deve ser somente divisivel por ele mesmo ou por 1')
            p = int(input('Digite um numero primo: '))
            primo1 = numPrimo(p)
        if primo2 == False:
            print('Para um numero ser primo ele deve ser somente divisivel por ele mesmo ou por 1')
            q = int(input('Digite um numero primo: '))
            primo2 = numPrimo(q)
        break

    n = p * q
    print('Se n = (p * q) entao n = {}'.format(n))
    z = (p - 1) * (q - 1)
    print('Se z = (p - 1) * (q - 1) entao z = {}'.format(z))
    #Esta parte é para encontrar minhas chaves, como são 2 incognitas eu pensei em colocalas em uma matriz e no momento em que eu percorrer ela por completo
    #a funcao ira me imprimir quais os valores de 'e' e 'd' que multiplicados deem o Z
    while True:
        for e in range(1, z + 2):
            for d in range(1, z + 2):
                if (e * d) == (z + 1):
                    if e > 1 or d > 1:
                        print('Seus valores disponíveis são \033[33mChave pública = {} \033[m& \033[33mChave privada = {}\033[m'.format(e, d))
                    elif e == 1 or d == 1:
                        print('Não foi possível encontrar uma combinacao de chaves pelos numeros primos informados.\nTente novamente do inicio!')
                        break

        break
#De acordo com a tabela apresentada anteriormente o usuario podera seleconar um dos conjuntos para prosseguir
    print('De acordo com a tabela apresentada acima, digite qual vai ser sua chave publica `e` e  chave privada `d` sendo que eles dois devem ser, cada um, numeros primos: ')
    e = int(input('Chave pública: '))
    d = int(input('Chave privada: '))
    while True:
        primoE = numPrimo(e)
        primoD = numPrimo(d)
        if (primoE == False and primoD == False) or (primoE == False and primoD == True) or (primoD == False and primoE == True):
            e = int(input('Digite outra chave pública: '))
            d = int(input('Digite outra chave privada: '))

        elif e == d:
            print('Infelizmente suas chaves não podem ser iguais! Isso facilitaria a invasão e o programa não serviria de nada.')
            e = int(input('Digite outra chave pública: '))
            d = int(input('Digite outra chave privada: '))
        else:
            break
#Menu de criptografia
    while True:
        CDRSA = rModo()
        if CDRSA == 'c' or CDRSA == 'C' or CDRSA == 'Cifrar':
            system('cls')
            cifra = CifrarRSA(e, n)

        elif CDRSA == 'd' or CDRSA == 'D' or CDRSA == 'Decifrar':
            system('cls')
            f = int(input('Digite a chave secreta: '))
            decifra = DecifrarRSA(f, n)

        elif CDRSA == 's' or CDRSA == 'S' or CDRSA == 'Sair':
            break

        else:
            print('Você digitou uma opção não disponível. Tente novamente!')

#Funcao principal
def main():
    while True:
        system('cls')
        #Usuario vai escolher qual tipo de criptografia ele deseja utilizar
        print('Selecione:\n\033[33m1\033[m-Criptografia Simétrica \n\033[33m2\033[m-Criptografia Assimétrica\n\033[33m0\033[m-Sair')
        menu = input('DIGITE A OPCAO DESEJADA: ')
        if menu == '1' or menu == 'Simetrica' or menu == 'simetrica' or menu == 'S' or menu == 's':
            while True:
                funcao = input('Digite qual função deseja: 1- tabelaS1 ou 2- tabelaP ou 0-Sair: ')
                if funcao == '1' or funcao == 'tabelaS1' or funcao == 'TabelaS1':
                    opcao1 = tabelaS1()

                elif funcao == '2' or funcao == 'tabelaP' or funcao == 'TabelaP':
                    opcao2 = tabelaP()

                elif funcao == '0' or funcao == 'Sair' or funcao == 's':
                    break

                else:
                    print('Releia o que estava escrito no início e tente novamente!!!\n')

        elif menu == '2' or menu == 'Assimetrica' or menu == 'assimetrica' or menu == 'a' or menu == 'A':
            assimetrico = RSA()

        elif menu == '0' or menu == 'Sair' or menu == 'sair':
            break

        else:
            print('Voce digitou uma opcao incorreta!\nTente novamente.\n')

main()