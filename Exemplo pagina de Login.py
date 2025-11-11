#Exemplo pagina de login

login = {}

print("======== PAGINA DE LOGIN ========")

while True:
    print("CRIAÇÃO DE CONTA - YMarinhoTech")
    user = input("Crie um nome de usuario:\nsem ultrapassar 16 caracteres\n").strip().lower()
    print()
    if len(user) > 16:
        print("Você não pode ultrapassar 16 caracteres\n")
        continue
    while True:
        password = input("Crie sua senha\ncom 8 ou mais caracteres e menos de 20\n").strip()
        print()
        if len(password) < 8 or len(password) >= 20:
            print("senha tem que ser com 8 ou mais caracteres e menos de 20\n")
            continue
        login[user] = password
        print(login)
        break
    break
while True:
    print("LOGIN - INSTAGRAM 2025")
    login_user = input("Coloque nome de usuario:\n").strip().lower()
    print()
    login_password = input("Coloque sua senha:\n").strip()
    print()
    if login_user in login:
        if login[login_user] == login_password:
            print("Login bem-sucedido! Bem-vindo(a) ao Instagram 2025.\n")
            break
        else:
            print("Senha incorreta. Tente novamente.\n")
    else:
        print("Usuário não encontrado. Tente novamente.\n")

print("Vamos a um novo teste!\npor favor, cadastre novamente o usuario criado recentemente.\n")
while True:
    print("CRIAÇÃO DE CONTA - YMarinhoTech")
    usuario = input("Crie um nome de usuario:\n").strip().lower()
    print()
    if usuario in login:
        print("Cadastro ja existe!")
        break
    elif len(user) > 16:
        print("Você não pode ultrapassar 16 caracteres\n")
        continue

