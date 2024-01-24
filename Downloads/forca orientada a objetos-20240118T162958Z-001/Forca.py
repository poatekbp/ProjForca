import random

class Forca:
    #método construtor da classe Forca
    def __init__(self):
        self.lista = []
        self.palavra = ''
        self.palavra_secreta = ''
        self.tentativas = 1
        self.acertou = False
        self.arquivo = ''
        self.acertos = ''

    #1
    def jogar(self):
        #Imprime informações na tela de início 
        print('===========================================')
        print('\tBEM VINDO AO JOGO DA FORCA')
        print('===========================================')

    #2
    def ler_arquivo(self):
        #Faz a leitura do arquivo e retorna uma lista com as palavras 
        with open('bd.txt') as arquivo:
            lista = []
            lista = arquivo.readlines()
            return lista
        
    #3
    def define_palavra(self, lista):
        #Definindo a palavra aleatoria através da lista 
        palavra = random.choice(lista)
        palavra = palavra.strip()
        return palavra

    #4
    def anonimizar_palavra(self, palavra):
        #Anonimiza palavras, substituindo as letras por traços
        palavra_secreta = ''
        for _ in palavra:
            palavra_secreta += '*'
        print(f"A palavra escolhida aleatoriamente é: {palavra_secreta} ela possui {len(palavra)} caracteres.")
        print("Você terá o dobro de chances de acertar.")
        return palavra_secreta
    
    #5
    def verifica_acerto(self, palavra, acertos, palpite):
    #Verifica os acertos do palpite em relação a palavra
        for indice in range(len(palavra)):
            if palpite == palavra[indice]:
                acertos[indice] = palpite
        print(''.join(acertos))
    