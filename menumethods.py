import os, time

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
    
def procurar(agd):
    cls()
    right_input = False
    while not right_input:
        nome = input("Digite o nome completo do contato: ")
        Lista_decontato = pos(nome, agd)
        achou = Lista_decontato[0]
        posicao = Lista_decontato[1]

        if not achou:
            print("Este contato não existe, tente novamente")
        else:
            print('Aniversario:', agd[posicao][1])
            print('Endereco:', agd[posicao][2])
            print('Telefone:', agd[posicao][3])
            print('Celular:', agd[posicao][4])
            print('e-mail:', agd[posicao][5])
            right_input = True

    return Lista_decontato

def excluir(agd):
    cls()
    print()
    
    right_input = False
    while not right_input:
        nome = input('NomeS: ')
        
        resposta = pos(nome ,agd)
        achou = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Este contato não existe. Por favor, tente novamente.')
        else:
            right_input = True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco:',agd[posicao][2])
    print('Telefone:',agd[posicao][3])
    print('Celular:',agd[posicao][4])
    print('e-mail:',agd[posicao][5])

    resposta = text('Deseja realmente excluir? Insira S ou N','Você deve digitar S ou N',['s','S','n','N'])
    

def text(inputText, mensagem, validate):
    right_input = False
    while not right_input:
        txt = input(inputText)

        if txt not in validate:
            print(mensagem,'- Favor redigitar...')
        else:
            right_input=True

    return txt


def pos(nom,agd):
    ini  =0
    final =len(agd)-1
    
    while ini<=final:
        meio=(ini+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            ini=meio+1
            
    return [False,ini]

def busca(agd):
    cls()
    nome=input('Nome a ser procurado: ')
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
    else:
        print('Nome não encontrado!')
        
def atualiza(agd):
    cls()
    nome=input('Nome a ser atualizado: ')
    resposta=pos(nome,agd)
    achou = resposta[0]
    posicao = resposta[1]
    
    if achou:
        print("O que deseja atualizar?")
        print("[1] Nome")
        print("[2] Aniversário")
        print("[3] Endereço")
        print("[4] Telefone")
        print("[5] Celular")
        print("[6] e-mail")
        opcao = input("Opção: ")
        match opcao:
            case '1':
                agd[posicao][0] = input("Novo nome: ")
            case '2':
                agd[posicao][1] = input("Novo aniversário: ")
            case '3':
                agd[posicao][2] = input("Novo endereço: ")
            case '4':
                agd[posicao][3] = input("Novo telefone: ")
            case '5':
                agd[posicao][4] = input("Novo celular: ")
            case '6':
                agd[posicao][5] = input("Novo e-mail: ")
    else:
        print('Nome não encontrado!')
        
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
