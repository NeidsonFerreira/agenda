import os
agenda=[]
sair=False
while(sair==False):
    print("Lista de Opções")
    print("1-Novo Contato")
    print("2-Listar Contatos")
    print("3- Editar Contato")
    print("4-Excluir Contato \n")
    opcao=int(input("Digite a Opção Escolhida ....:"))

    if(opcao==1):
        novo_contato=[]
        nome=input("\nDigite o Nome do Contato:")
        novo_contato.append(nome)
        telefone=input("Digite o Telefone do Contato:")
        novo_contato.append(telefone)
        agenda.append(novo_contato)
        os.system('cls')
    if(opcao==2):
        for contato in agenda:
            print("\nNome:",contato[0],"Telefone:",contato[1],"\n")
    
    