def caixa_eletronico(valor_saque):
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = [0, 0, 0, 0, 0]  # para armazenar a quantidade de cada nota
    
    if valor_saque < 10 or valor_saque > 600:
        print("Valor de saque não permitido.")
        return
    
    for i, nota in enumerate(notas):
        while valor_saque >= nota:
            quantidade_notas[i] += 1
            valor_saque -= nota
    
    print(f"Notas fornecidas para o saque de {valor_saque} reais:")
    for i, qtd in enumerate(quantidade_notas):
        if qtd > 0:
            print(f"{qtd} nota(s) de {notas[i]} reais")

# Exemplo de uso:
# valor = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))
# caixa_eletronico(valor)
