import os, time
from main import menu

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def text (solicitacao, mensagem, validate):
    right_input=False
    while not right_input:
        txt=input(solicitacao)

        if txt not in validate:
            print(mensagem,'- Favor redigitar...')
        else:
            right_input=True

    return txt

def chosen(mnu):
    print ()

    opcoesValidas=[]
    pos=0
    while pos<len(mnu):
        print (pos +1,') ',mnu[pos],sep='')
        opcoesValidas.append(str(pos + 1))
        pos += 1

    print()
    return text('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def pos(nom,agd):
    inicio= 0
    final = len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def text(inputText, mensagem, validate):
    right_input = False
    while not right_input:
        txt = input(inputText)

        if txt not in validate:
            print(mensagem,'- Favor redigitar...')
        else:
            right_input=True

    return txt

def incluir(agd):
    try:
        time.sleep(1)
        cls()
        right_input = False
        while not right_input:
            nome = input('\nNome: ')
            resposta = pos(nome,agd)
            achou = resposta[0]
            posicao = resposta[1]
            if achou:
                print ('Este contato já existe. Por favor, tente novamente.')
            else:
                right_input = True
                
        aniversario = input('Aniversário: ')
        endereco = input('Endereço: ')
        telefone = input('Telefone:')
        if not telefone.isdigit():
            raise ValueError('Celular inválido')
        celular = input('Celular: ')
        if not celular.isdigit():
            raise ValueError('Celular inválido')
        email = input('e-mail: ')
        if '@' not in email:
            raise ValueError('Invalid email address')
        if nome == '' or aniversario == '' or endereco == '' or telefone == '' or celular == '' or email == '':
            raise ValueError
        contato=[nome,aniversario,endereco,telefone,celular,email]
        agd.insert(posicao,contato)
        print('Cadastro realizado com sucesso!')
    except ValueError:
        print('Erro ao incluir contato. Tente novamente.')
        incluir(agd)

def lista(agd):
    cls()
    print()
    
    for contato in agd:
        print('Nome:',contato[0])
        print('Aniversário:',contato[1])
        print('Endereço:',contato[2])
        print('Telefone:',contato[3])
        print('Celular:',contato[4])
        print('e-mail:',contato[5])
        print()
        
def busca(agd):
    cls()
    right_input = False
    while not right_input:
        nome = input('Nome a ser procurado: ')
        resposta = pos(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]
        if achou:
            print('Nome:', agd[posicao][0])
            print('Aniversário:', agd[posicao][1])
            print('Endereço:', agd[posicao][2])
            print('Telefone:', agd[posicao][3])
            print('Celular:', agd[posicao][4])
            print('e-mail:', agd[posicao][5])
            right_input = True
        else:
            print('Nome não encontrado!')
        
def atualiza(agd):
    cls()
    nome=input('Nome a ser atualizado: ')
    resposta=pos(nome,agd)
    achou = resposta[0]
    posicao = resposta[1]
    
    if achou:
        while True:
            print("O que deseja atualizar?")
            print("[1] Nome")
            print("[2] Aniversário")
            print("[3] Endereço")
            print("[4] Telefone")
            print("[5] Celular")
            print("[6] E-mail")
            print("[7] Cancelar")
            opcao = input("Opção: ")
            if opcao == '1':
                agd[posicao][0] = input("Novo nome: ")
            elif opcao == '2':
                agd[posicao][1] = input("Novo aniversário: ")
            elif opcao == '3':
                agd[posicao][2] = input("Novo endereço: ")
            elif opcao == '4':
                agd[posicao][3] = input("Novo telefone: ")
            elif opcao == '5':
                agd[posicao][4] = input("Novo celular: ")
            elif opcao == '6':
                agd[posicao][5] = input("Novo e-mail: ")
            elif opcao == '7':
                print('Atualização finalizada!')
                break
            else:
                print('Opção inválida!')
    else:
        print('Nome não encontrado!')
        
def exclui(agd):
    cls()
    print()
    nome=input('Nome a ser excluído: ')
    resposta=pos(nome,agd)
    achou = resposta[0]
    posicao = resposta[1]
    
    if achou:
        print('Nome:',agd[posicao][0])
        print('Aniversário:',agd[posicao][1])
        print('Endereço:',agd[posicao][2])
        print('Telefone:',agd[posicao][3])
        print('Celular:',agd[posicao][4])
        print('e-mail:',agd[posicao][5])
        
        resposta=text('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
        
        if resposta in ['s','S']:
            agd.remove(agd[posicao])
            print('Cadastro excluído com sucesso!')
        else:
            print('Exclusão cancelada!')
    else:
        print('Nome não encontrado!')
