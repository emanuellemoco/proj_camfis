
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
import sys, math
import time
from tkinter import filedialog
from tkinter import *

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

    #mudar essa parte para imagem mandar imagem 
    #txBuffer = bytes([2]) + bytes([100])+ bytes([8])+ bytes("teste", 'utf-8')

    #para imagem
    

    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)

    txBuffer = open (root.filename,'rb').read()

    txLen    = len(txBuffer)
    print("tamanho")
    print(txLen)

    txLenByte = (txLen).to_bytes(4, byteorder='little') #passando para bytes

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))
    #com.sendData(txLenByte)
    #com.sendData(txBuffer) 
    totalLen = len(txLenByte + txBuffer)
    #print("tamanho total")
    #print(txLenByte)
    print("seila")
    com.sendData(txLenByte + txBuffer) #mandando o tamanho e o txt em byte
   
    inicio = time.time()
    print("comecou a contar")
    
    # espera o fim da transmissão
    #while(com.tx.getIsBussy()):
    #    pass
    

    # Atualiza dados da transmissão
    txSize = com.tx.getStatus()
    print ("Transmitido       {} bytes ".format(txSize))

    # Faz a recepção dos dados
    print ("Recebendo dados .... ")
    print("dasd")
    #repare que o tamanho da mensagem a ser lida é conhecida!     
    rxBuffer, nRx = com.getData()
    print("paroy de rodar aqui")

    #arquivo que mandou
    #open("chegouu.jpg",'wb').write(rxBuffer)
    final =int.from_bytes(rxBuffer,byteorder='little')
    print("FF")
    print(rxBuffer)
   # fim = time.time()
   #tempo= fim - inicio
   #print("o tempo total:{}".format(tempo))
   #taxa=tempo/txLenByte
   #print("a taxa total:{}".format(taxa))

    # log
    print ("Lido              {} bytes ".format(nRx))
    
    print (rxBuffer)
  
    # Encerra comunicação
    print("-------------------------")
    print("Comunicação encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for ex
    # ecutado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
