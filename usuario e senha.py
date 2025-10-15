
while True:
    usuario = input("Informe o nome de usuário:")
    senha = input("Informe uma senha:")
    if senha == usuario:
        print("Erro! a senha nao pode ser igual ao nome de usuario. Tente novamente")
    else:
        print("Usuário e senha cadastrados com sucesso! Seja Bem-vindo")
        break
