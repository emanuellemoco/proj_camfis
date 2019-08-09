
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Aplicação 
####################################################
import os 
print(os.getcwd())
print("comecou")

from enlace import *

import time
inicio = time.time()
print("comecou a contar")


# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)
print("abriu com")

def main():
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName) # repare que o metodo construtor recebe um string (nome)
    # Ativa comunicacao
    com.enable()

   

    # Log
    print("-------------------------")
    print("Comunicação inicializada")
    print("  porta : {}".format(com.fisica.name))
    print("-------------------------")

    # Carrega dados
    print ("gerando dados para transmissao :")
  
      #no exemplo estamos gerando uma lista de bytes ou dois bytes concatenados
    
    #exemplo 1
    #ListTxBuffer =list()
    #for x in range(1,10):
    #    ListTxBuffer.append(x)
    #txBuffer = bytes(ListTxBuffer)
    
    #exemplo2 (em byte a soma eh o mesmo que append)

    #mudar essa parte para imagem 
    #txBuffer = bytes([2]) + bytes([100])+ bytes([8])+ bytes("teste", 'utf-8')

    #para imagem
    txBuffer = open ("imagem.jpg",'rb').read()

    txLen    = len(txBuffer)
    print(txLen)

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))
    com.sendData(txBuffer)

    # espera o fim da transmissão
    #while(com.tx.getIsBussy()):
    #    pass
    
    
    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()
    print ("Transmitido       {} bytes ".format(txSize))

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    
    #repare que o tamanho da mensagem a ser lida é conhecida!     
    rxBuffer, nRx = com.getData(txLen)

    #arquivo que mandou
    open("fodasse.jpg",'wb').write(rxBuffer)

    # log
    print ("Lido              {} bytes ".format(nRx))
    
    print (rxBuffer)
  
    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #apos encerrar a comunicacao para o timer
    fim = time.time() 
    print("Tempo: ", (fim-inicio))
  

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
