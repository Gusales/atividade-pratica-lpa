print("Bem-vindo a Loja do Gustavo Sales")

valor_unitario = float(input("Entre com o valor do produto: R$"))
quantidade_do_produto = int(input("Entre com a quantidade do produto: "))

valor_sem_desconto = valor_unitario * quantidade_do_produto
print(f"O valor SEM desconto: R${valor_sem_desconto:.2f}")

desconto = 0

if valor_sem_desconto < 2500:
    # Para valores abaixo de R$ 2.500 não será aplicado desconto, então ele continua como 0
    desconto = 0
elif valor_sem_desconto >= 2500 and valor_sem_desconto < 6000:
    # Aplicando 4% de desconto, pois 0.04 x 100 = 4%
    desconto = 0.04
elif valor_sem_desconto >= 6000 and valor_sem_desconto < 10000:
    # Aplicando 7% de desconto, pois 0.07 x 100 = 4%
    desconto = 0.07
else:
    # Aplicando 11% de desconto, pois 0.11 x 100 = 4%
    desconto = 0.11

# Calculando quanto será diminuido do preço bruto
preco_descontado = valor_sem_desconto * desconto

valor_com_desconto = valor_sem_desconto - preco_descontado
print(f"O valor COM desconto({(desconto * 100):.0f}%): R${valor_com_desconto:.2f}")
