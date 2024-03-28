import os 

def limparTerminal():
    #limpando o terminal usando o comando de acordo com o SO
    os.system('cls' if os.name == 'nt' else clear)

def encerraPrograma(): #Função para finalizar o programa
    limparTerminal()
    print('Obrigado por participar!')
    os.exit(0)

limparTerminal() #Limpando o terminal

lista = [] #Define a lista vazia 

while True:
    titulo = 'Lista de compras'
    print(f'{titulo:-^40}') #centralizando o titulo 
    print('\nO que deseja fazer?')
    op = input('[1] Inserir Item\n[2] Apagar item\n[3]Listar todos os itens\n[4]Sair\n') #Menu do sistema

    if op == '4': #opção sair
        encerraPrograma()
        break
    elif op == '1': #Inserindo dados na lista
        limparTerminal()
        novo_item = input("Qual item você deseja adicionar na lista de compras?")
        lista.append(novo_item)
        limparTerminal()
        continue
    elif op == '2': #Opção de apagar item
        limparTerminal()
        for indice, valor in enumerate(lista):
            print(indice, valor)
        print()
        remover_item = input('Digite o indice do item que deseja remover: ')

        try: 
            indice = int(remover_item)
            del lista[indice]
            limparTerminal()
            print(f'Lista de compras atualizada: {lista}\n')
        except (ValueError, IndexError):
            limparTerminal()
            print("Este indice não existe, por favor digite um indice válido!\n")
        continue
    elif op == '3': #opção listar todos os items
        limparTerminal()
        if len(lista) == 0:
            print("Não há items na lista")
        else:
            for i, valor in enumerate(lista):
                print(i, valor)
        print()
        continue
    else:
        limparTerminal()
        print('Opção inválida, por favor selecione uma opção válida')
        continue
    
