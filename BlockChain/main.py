from block.blockchain import BlockChain
from block.block import Block
from datetime import datetime
from data.datas import Data
from data.tag1 import WithdrawalRecord
from data.tag2 import Storage
from data.tag3 import Transportation

block_chain = BlockChain()
while True:
    print("-------//---------//------" +
          "\n" +
          "Bem vindo ao BlockChain" +
          "\n" + "-------//---------//------"+ "\n")

    entrada = input(("Digite sua opção:" + "\n" + "(A)dicionar um bloco" + "\n" + "(S)sair" + "\n" + "(L)istar blocos" + "\n" + "Opcao>"))
    if entrada.upper() == "A":
        print("Etiqueta 1: " + "\n")
        reg_animal = input("Registro Animal: ")
        volume_animal = float(input("Volume produzido: "))
        data = input("Data de retirada: ")
        hora = input("Hora de retirada: ")

        print("\n" + "Etiqueta 2: " + "\n")
        armazenamento = float(input("Volume de armazenamento: "))
        temperatura = float(input("Temperatura do armazenamento: "))
        ph = float(input("Ph do Leite: "))

        print("\n" + "Etiqueta 3: " + "\n")
        documento_veiculo = input("Documento do Veiculo: ")
        temperatura_veiculo = input("Temperatura do Veiculo: ")
        tempo_transporte = input("Tempo de transporte: ")

        date = datetime.now()
        tag1 = WithdrawalRecord(reg_animal,volume_animal, data, hora)
        tag2 = Storage(armazenamento, temperatura, ph)
        tag3 = Transportation(documento_veiculo, temperatura_veiculo, tempo_transporte)
        info = Data(tag1, tag2, tag3)

        block = Block(len(block_chain.chain), date, getattr(block_chain.get_latest_block(), "hash"), info)
        block_chain.add_block(block)

    elif entrada.upper() == "L":
        print(block_chain.exibe_blocos())
    else:
        break







