print(f"\nBem-vindo a Copiadora do Gustavo Sales\n")

def escolha_servico():
    # Tabela de Preços da Copiadora
    print(f"{'Serviço':<22} {'Código':<6} {'Preço por Página'}")
    print("-" * 45)
    print(f"{'Digitalização':<22} {'DIG':<6} {'R$ 1,10'}")
    print(f"{'Impressão colorida':<22} {'ICO':<6} {'R$ 1,00'}")
    print(f"{'Impressão P&B':<22} {'IPB':<6} {'R$ 0,40'}")
    print(f"{'Fotocópia':<22} {'FOT':<6} {'R$ 0,20'}")
    print("-" * 45)

    # Escolha do cliente
    servico = str(input("O que irá querer, cliente? (Digite o código do serviço): ")).upper()
    while servico != "DIG" and servico != "ICO" and servico != "IPB" and servico != "FOT":
        print("Não consegui encontrar esse serviço na lista", end=", ")
        servico = str(input("escolha um dos serviços da lista: ")).upper()

    # Validando serviço que usuário necessita]
    if servico == "DIG":
        return 1.1
    elif servico == "ICO":
        return 1
    elif servico == "IPB":
        return 0.40
    else:
        return 0.20

def num_pagina():
    # Tabela de Preços da quantidade de páginas
    print(f"{'Quantidade de Páginas':<35} {'Desconto Aplicado'}")
    print("-" * 60)
    print(f"{'Menor que 20':<35} {'Sem desconto'}")
    print(f"{'20 até 199':<35} {'15%'}")
    print(f"{'200 até 1.999':<35} {'20%'}")
    print(f"{'2.000 até 19.999':<35} {'25%'}")
    print(f"{'20.000 ou mais':<35} {'Pedido não aceito'}")
    print("-" * 60)

    # Escolha do cliente
    num_paginas = 0
    desconto = 0
    while num_paginas == 0 or num_paginas > 20000:
        try:
            num_paginas = int(input("Agora, digite a quantidade de páginas: "))

            # Validações para saber se o usuário está a digitar certo a quantidade de páginas
            if num_paginas == 0:
                print("Precisamos ter pelo menos uma (1) página para realizar as cópias!")
            elif num_paginas >= 20000:
                print("Não aceitamos pedidos com mais de 20.000 páginas!")
            else:
                # Passadas as validações anteriores, vamos fazer o cálculo da quantidade do desconto
                if num_paginas > 0 and num_paginas < 20:
                    desconto = 0
                elif num_paginas >= 20 and num_paginas < 200:
                    desconto = 15 / 100 # 15% ou 0.15
                elif num_paginas >= 200 and num_paginas < 2000:
                    desconto = 20 / 100 # 20% ou 0.20
                elif num_paginas >= 2000 and num_paginas < 20000:
                    desconto = 25 / 100  # 25% ou 0.25

        except ValueError:
            print("Apenas valores numéricos são aceitos!")
        except Exception as error:
            print("Ocorreu um erro ao receber quantidade de páginas!\n" + str(error))

    # Para uma melhor estruturação do código, optei por retornar um array de números onde
    # a primeira posição é o número de páginas e a última é o total do desconto
    return [num_paginas, desconto]

def servico_extra():
    # Tabela de serviços extras
    print(f"{'Código':<8} {'Adicional':<35} {'Valor Extra (R$)'}")
    print("-" * 60)
    print(f"{'1':<8} {'Encadernação simples':<35} {'R$ 15,00'}")
    print(f"{'2':<8} {'Encadernação capa dura':<35} {'R$ 40,00'}")
    print(f"{'0':<8} {'Sem adicional':<35} {'R$ 0,00'}")
    print("-" * 60)

    # Escolha do tipo de serviço extra do usuário
    extra = str(input("Escolha o tipo de encadernação: ")).upper()
    while extra != "1" and extra != "2" and extra != "0":
        extra = str(input("Nenhuma opção foi encontrada! Digite novamente:")).upper()

    # Validando o preço conforme o pedido do usuário
    if extra == "1":
        return 15
    elif extra == "2":
        return 40
    else:
        return 0

def main():
    servico = escolha_servico()
    [paginas, desconto] = num_pagina()
    extra = servico_extra()

    total = (servico * paginas) + extra
    print(f"Preço total: R${total:.2f}")
    total -= total * desconto

    print(f"Total: R$ {total:.2f}, (Serviço: {servico}; Páginas {paginas}; Extra {extra:.2f}); Desconto {(desconto * 100):.0f}%")

main()