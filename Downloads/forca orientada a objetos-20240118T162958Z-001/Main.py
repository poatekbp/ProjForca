from Forca import Forca
import random

class Main:

    def __init__(self):            
        # Instanciando o objeto Forca
        self.forca = Forca()

    def jogar(self):
        # Chamando a função para jogar
        self.forca.jogar()

if __name__ == "__main__":
    jogo = Main()
    jogo.jogar()
    lista = jogo.forca.ler_arquivo()
    palavra = jogo.forca.define_palavra(lista)
    tentativas = (len(palavra) * 2)
    palavra_secreta = jogo.forca.anonimizar_palavra(palavra)
    acertos = list(palavra_secreta)

    while (jogo.forca.acertou == False or tentativas >= 1):
        
        palpite = input("Informe uma letra: ")
        verificar_acerto = jogo.forca.verifica_acerto(palavra, acertos, palpite)

        if (len(palpite) > len(palavra)):
                palpite = input("Informe uma palavra válida: ")
        
        elif palpite == palavra or acertos == list(palavra):
            acertou = True
            print("Parabéns, você acertou!")
            break
        else: 
            tentativas = tentativas - 1
            if(tentativas > 0):
                print(f"Você ainda tem {tentativas} tentativa(s)!")   
            elif (tentativas == 0):
                print("Você perdeu!")
                print(f"A palavra era {palavra}")
                break     
    
