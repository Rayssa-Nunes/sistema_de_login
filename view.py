from controller import ControllerCadastro, ControllerLogin

while True:
    print('=========== [MENU] ==========')
    opcao = int(input('Digite 1 para Cadastrar\nDigite 2 para Logar\nDigite 3 para Sair\n'))
    if opcao == 1:
        nome = input('Nome: ')
        email = input('E-mail: ')
        senha = input('Senha: ')

        resultado = ControllerCadastro.cadastrar(nome, email, senha)
        if resultado == 2:
            print('Digite um nome de tamanho maior.')
        elif resultado == 3:
            print('Digite um e-mail válido.')
        elif resultado == 4:
            print('Digite uma senha com 8 ou mais caracteres.')
        elif resultado == 5:
            print('E-mail já cadastrado.')
        elif resultado == 6:
            print('Erro interno do sistema.')
        elif resultado == 1:
            print('Cadastro realizado com sucesso.')
    elif opcao == 2:
        pass
    elif opcao == 3:
        break
    else:
        print('Digite uma opção válida.')
