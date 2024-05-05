from methods import present, incluir, busca, atualiza, lista, exclui
present()

agenda=[]

print ("Escolha uma opção:")
print ("\n[1] Incluir um contato\n\
[2] Buscar um contato\n\
[3] Atualizar um contato\n\
[4] Listar todos os contatos\n\
[5] Excluir um contato\n\
[6] Sair")
opcao = input("Opção: ")
match opcao:
    case '1':
        incluir(agenda)
    case '2':
        busca(agenda)
    case '3':
        atualiza(agenda)
    case '4':
        lista(agenda)
    case '5':
        exclui(agenda)
    case '6':
        print('OBRIGADO POR USAR ESTE PROGRAMA!')
        exit()