print("Bem-vindo!")
print("Este é um CRUD.")
ans = input("Deseja continuar? \n[1] Sim \n[2] Não")
if (ans == "n" or ans == "N"):
    print("Abortando...")   
    exit()
elif (ans == "s" or ans == "S"):
    print("Continuando...")
else:
    print("Opção inválida!")
    exit()

