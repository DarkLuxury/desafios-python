print("Qual a sua idade?:")
idade = int(input(""))
if idade >=25 and idade <= 60:
    print("Quanto você quer emprestado?:")
    valor = int(input(""))
    print("Quanto você ganha?:")
    salario = int(input(""))
    if salario >= valor * 1.5:
        print(f"Empréstimo de {valor} aprovado")
    else:
        print(f"Empréstimo de {valor} reprovado devido ao valor ser incompativel com o salario")
else:
    print("Empréstimo rejeitado devido a idade")


