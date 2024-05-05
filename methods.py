
def present():
    print('+-------------------------------------------------------------+\n\
           |                                                             |\n\
           | AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |\n\
           |                                                             |\n\
           |                                                             |\n\
           | Versão 1.0 de 12/abril/2024                                 |\n\
           |                                                             |\n\
           +-------------------------------------------------------------+')

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

def incluir (agd):
    right_input=False
    while not right_input:
        nome=input('\nNome.......: ')

        resposta = pos(nome,agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print('Pessoa já existente - Favor redigitar...')
        else:
            right_input=True
            
    aniversario = input('Aniversário: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    celular = input('Celular: ')
    email = input('e-mail: ')
    
    contato= [nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')
    
    def include(agd):
        right_input = False
        while not right_input:
            nome = input('\nNome.......: ')

            resposta = pos(nome, agd)
            achou = resposta[0]
            posicao = resposta[1]

            if achou:
                print('Pessoa já existente - Favor redigitar...')
            else:
                right_input = True

        aniversario = input('Aniversário: ')
        endereco = input('Endereço: ')
        telefone = input('Telefone: ')
        celular = input('Celular: ')
        email = input('e-mail: ')

        contato = [nome, aniversario, endereco, telefone, celular, email]
        agd.insert(posicao, contato)
        print('Cadastro realizado com sucesso!')
        
def procurar(agd):

    right_input = False
    while not right_input:

        nome = input("Digite o nome completo do contato: ")
        Lista_decontato = pos(nome, agd)
        achou = Lista_decontato [0]
        posicao = Lista_decontato [1]

    if nome not in Lista_decontato:
        print ("Este contato não existe, tente novamente")
    
    else:
    
        print('Aniversario:',agd[posicao][1])
        print('Endereco:',agd[posicao][2])
        print('Telefone:',agd[posicao][3])
        print('Celular:',agd[posicao][4])
        print('e-mail:',agd[posicao][5])
        
        right_input= True

    


    print (procurar(Lista_decontato))
    return Lista_decontato
    print (procurar(Lista_decontato))


def excluir (agd):
    print()
    
    right_input = False
    while not right_input:
        nome = input('Nome.......: ')
        
        resposta = pos(nome ,agd)
        achou = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Este contato não existe. Por favor, tente novamente.')
        else:
            right_input=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco:',agd[posicao][2])
    print('Telefone:',agd[posicao][3])
    print('Celular:',agd[posicao][4])
    print('e-mail:',agd[posicao][5])

    resposta = text('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    

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


def incluir(agd):
    right_input=False
    while not right_input:
        nome=input('\nNome: ')

        resposta = pos(nome,agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Este contato já existe. Por favor, tente novamente.')
        else:
            right_input=True
            
    aniversario= input('Aniversário: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    celular = input('Celular: ')
    email = input('e-mail: ')
    contato=[nome,aniversario,endereco,telefone,celular,email]
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')
    
    
def busca(agd):
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
    nome=input('Nome a ser atualizado: ')
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
        
        aniversario= input('Aniversário: ')
        endereco = input('Endereço: ')
        telefone = input('Telefone: ')
        celular = input('Celular: ')
        email = input('e-mail: ')
        
        agd[posicao]=[nome,aniversario,endereco,telefone,celular,email]
        print('Cadastro atualizado com sucesso!')
    else:
        print('Nome não encontrado!')
        
def lista(agd):
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
