import methods, webbrowser, time
print('+-------------------------------------------------------------+\n\
|                                                             |\n\
| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |\n\
|                                                             |\n\
|                                                             |\n\
| Augusto Gramani Lacerda                                     |\n\
| Cris Oliveira Olímpio                                       |\n\
| Davi Andrade Macedo                                         |\n\
|                                                             |\n\
| Versão 2.0 de 7 de Abril de 2024                            |\n\
|                                                             |\n\
+-------------------------------------------------------------+')
agenda=[]
#skadkaskdf
def menu():
    
    print("Escolha uma opção:")
    print("\n[1] Incluir um contato\n\
[2] Buscar um contato\n\
[3] Atualizar um contato\n\
[4] Listar todos os contatos\n\
[5] Excluir um contato\n\
[6] Sair\n\
[666] Maligno")
    opcao = input("Opção: ")
    match opcao:
        case '1':
            methods.incluir(agenda)
        case '2':
            methods.procura(agenda)
        case '3':
            methods.atualiza(agenda)
        case '4':
            methods.lista(agenda)
        case '5':
            methods.exclui(agenda)
        case '6':
            print('OBRIGADO POR USAR ESTE PROGRAMA!')
            exit()
        case '7':
            webbrowser.open_new("https://bigrat.monster/printer")
        case '666': 
            print("Oi maligno")
            time.sleep(2)
            webbrowser.open_new("https://bigrat.monster/freekr")
            methods.cls()
            menu()

if __name__ == '__main__':
    while True:
        menu()