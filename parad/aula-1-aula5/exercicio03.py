while True:
    texto = input("Digite sua idade: ")
    try:
        idade = int(texto)
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue
        print(f"Idade registrada: {idade}")
        break
    except ValueError:
        print("Entrada inválida, tente novamente.")
