print(f"\nBem-vindo a Loja do Gustavo Sales\n")

# Função para exibir a tabela com o cardápio
def exibir_cardapio():
    print("-------------------Cardápio---------------------")
    print("|---| Tamanho | Cupuaçu (CP) |   Açaí (AC) |---|")
    print("|---|---------|--------------|-------------|---|")
    print("|---|    P    |   R$  9.00   |   R$ 11.00  |---|")
    print("|---|    M    |   R$ 14.00   |   R$ 16.00  |---|")
    print("|---|    G    |   R$ 18.00   |   R$ 20.00  |---|")
    print("------------------------------------------------")


# Inicia a variável do total da compra do cliente
totalDaCompra = 0

exibir_cardapio()

# Verifica se o cliente quer fazer mais de um pedido 
while True:
    # Verificando o sabor que o cliente quer
    # Criei essa variável mensagem só para deixar o código mais limpo
    mensagem = f"Qual sabor você vai querer? Digite o código: "

    sabor = str(input(mensagem))
    # Loop para garantir que o cliente digite apenas os sabores da lista
    while ((sabor.lower() != "cp") and (sabor.lower() != "ac")):
        print("Sabor inválido, tente novamente!")
        sabor = str(input(mensagem))

    # Verificando o tamanho da sobremesa que o cliente quer
    # Reutilizei a variável mensagem para continuar a manter o código limpo
    mensagem = f"Agora, qual você tamanho você irá querer? "

    tamanho = str(input(mensagem))
    # Loop para garantir que o cliente digite apenas os tamanhos da lista
    while ((tamanho.lower() != "p") and (tamanho.lower() != "m") and (tamanho.lower() != "g")):
        print("Tamanho inválido, tente novamente!")
        tamanho = str(input(mensagem))
    
    if tamanho == "p":
        if sabor == "cp":
            preco = 9
            print(f"Um cupuaçu de tamanho pequeno saindo! R${preco:.2f}")
            totalDaCompra += preco
        else: 
            preco = 11
            print(f"Um açaí de tamanho pequeno na hora indo direto pro balcão! R${preco:.2f}")
            totalDaCompra += preco
    
    elif tamanho == "m":
        if sabor == "cp":
            preco = 14
            print(f"Um cupuaçu de tamanho médio pra já! R${preco:.2f}")
            totalDaCompra += preco  
        else: 
            preco = 16
            print(f"Um açaí de tamanho médio prontinho! R${preco:.2f}")
            totalDaCompra += preco
      
    else:
        if sabor == "cp":
            preco = 18
            print(f"Um cupuaçu de tamanho grande bem geladinho subindo! R${preco:.2f}")
            totalDaCompra += preco  
        else: 
            preco = 20
            print(f"Um açaí de tamanho grande pronto para entregar! R${preco:.2f}")
            totalDaCompra += preco    
            
    # Verificando se o cliente quer mais alguma coisa:
    print("------------------------------------------------")
    escolhaDoCliente = str(input("Deseja mais algo? (S/N): "))
    while escolhaDoCliente.lower() != "s" and escolhaDoCliente.lower() != "n":
        print("Não entendi sua escolha", end=" ")
        escolhaDoCliente = str(input("Quer mais algo? (S/N): "))
        
    if escolhaDoCliente.lower() == "n":
        break

print(f"Total da compra: R${totalDaCompra:.2f}")
