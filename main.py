from menumethods import incluir, procura, atualiza, lista, exclui
print('+-------------------------------------------------------------+\n\
|                                                             |\n\
| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |\n\
|                                                             |\n\
|                                                             |\n\
| Versão 1.0 de 12/abril/2024                                 |\n\
|                                                             |\n\
+-------------------------------------------------------------+')
agenda=[]

def menu():
    
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
            procura(agenda)
        case '3':
            atualiza(agenda)
        case '4':
            lista(agenda)
        case '5':
            exclui(agenda)
        case '6':
            print('OBRIGADO POR USAR ESTE PROGRAMA!')
            exit()

if __name__ == '__main__':
    while True:
        menu()