# =========================================================
# TRABALHO PRÁTICO - ALGORITMOS E PROGRAMAÇÃO
# Sistema de Atendimento e Pedidos de Lanchonete
# =========================================================

def exibir_cardapio():
    """Exibe o cardápio da lanchonete com códigos, nomes e preços."""
    print("\n" + "=" * 40)
    print("           CARDÁPIO DA LANCHONETE       ")
    print("=" * 40)
    print(" Código | Produto            | Preço   ")
    print("-" * 40)
    print("   101  | X-Burguer          | R$ 18.00")
    print("   102  | X-Salada           | R$ 20.00")
    print("   103  | X-Bacon            | R$ 24.00")
    print("   104  | Batata Frita       | R$ 12.00")
    print("   105  | Refrigerante Lata  | R$  6.00")
    print("   106  | Suco Natural       | R$  8.00")
    print("=" * 40)

def obter_preco_produto(codigo):
    """Retorna o preço do produto correspondente ao código.
    Retorna 0.0 se o código for inválido.
    """
    if codigo == "101":
        return 18.00
    elif codigo == "102":
        return 20.00
    elif codigo == "103":
        return 24.00
    elif codigo == "104":
        return 12.00
    elif codigo == "105":
        return 6.00
    elif codigo == "106":
        return 8.00
    else:
        return 0.0

def calcular_desconto(total_original):
    """Calcula o valor e o percentual de desconto com base no total acumulado."""
    if total_original < 50.00:
        percentual = 0
    elif total_original < 100.00:
        percentual = 5
    else:
        percentual = 10
    
    valor_desconto = total_original * (percentual / 100)
    total_final = total_original - valor_desconto
    return percentual, valor_desconto, total_final

def obter_nome_pagamento(opcao_pagamento):
    """Retorna a descrição textual da forma de pagamento selecionada."""
    if opcao_pagamento == "1":
        return "Dinheiro"
    elif opcao_pagamento == "2":
        return "PIX"
    elif opcao_pagamento == "3":
        return "Cartão"
    else:
        return ""

def exibir_resumo(nome_cliente, total_original, percentual_desc, valor_desc, total_final, forma_pagamento):
    """Apresenta o resumo detalhado e organizado da compra."""
    print("\n" + "=" * 45)
    print("            RESUMO FINAL DO PEDIDO           ")
    print("=" * 45)
    print(f" Cliente:            {nome_cliente}")
    print(f" Valor Original:     R$ {total_original:.2f}")
    print(f" Desconto Aplicado:  {percentual_desc}%")
    print(f" Valor do Desconto:  R$ {valor_desc:.2f}")
    print(f" Valor Final a Pagar: R$ {total_final:.2f}")
    print(f" Forma de Pagamento: {forma_pagamento}")
    print("=" * 45)
    print("        Obrigado pela preferência!           ")
    print("=" * 45 + "\n")

def main():
    """Função principal que gerencia o fluxo de atendimento da lanchonete."""
    print("=" * 45)
    print("    SEJA BEM-VINDO À LANCHONETE PYTHON!    ")
    print("=" * 45)
    
    # Identificação do cliente
    nome_cliente = input("Por favor, informe seu nome para iniciar: ").strip()
    while nome_cliente == "":
        nome_cliente = input("O nome não pode ser vazio. Digite seu nome: ").strip()
    
    total_compra = 0.0
    continuar_pedindo = True
    
    # Loop principal para inclusão de itens no pedido
    while continuar_pedindo:
        exibir_cardapio()
        codigo_str = input("\nDigite o código do produto desejado: ").strip()
        preco_unitario = obter_preco_produto(codigo_str)
        
        # Validação do produto escolhido
        if preco_unitario == 0.0:
            print("\n[ERRO] Código de produto inválido! Tente novamente.")
            continue
        
        # Leitura e validação da quantidade
        try:
            qtd = int(input("Informe a quantidade desejada: "))
            if qtd <= 0:
                print("\n[ERRO] A quantidade deve ser um número maior que zero!")
                continue
        except ValueError:
            print("\n[ERRO] Digite um número inteiro válido para a quantidade!")
            continue
        
        # Cálculo do subtotal do item e acúmulo no total
        subtotal = preco_unitario * qtd
        total_compra = total_compra + subtotal
        
        print(f"\n[SUCESSO] Item adicionado! Subtotal: R$ {subtotal:.2f}")
        print(f"Total acumulado até o momento: R$ {total_compra:.2f}")
        
        # Pergunta se deseja adicionar mais produtos
        resposta = input("\nDeseja adicionar outro produto? (S para Sim / N para Não): ").strip().upper()
        while resposta != "S" and resposta != "N":
            resposta = input("Opção inválida! Responda com 'S' (Sim) ou 'N' (Não): ").strip().upper()
            
        if resposta == "N":
            continuar_pedindo = False

    # Verificação se algum produto foi selecionado antes de prosseguir
    if total_compra == 0.0:
        print("\nNenhum produto foi adicionado. Atendimento finalizado sem compras.")
        return

    # Processamento de desconto
    percentual_desc, valor_desc, total_final = calcular_desconto(total_compra)
    
    # Seleção e validação da forma de pagamento
    forma_pagamento_nome = ""
    while forma_pagamento_nome == "":
        print("\n-------------------------------------------")
        print("FORMA DE PAGAMENTO:")
        print(" 1 - Dinheiro")
        print(" 2 - PIX")
        print(" 3 - Cartão")
        op_pagamento = input("Escolha a forma de pagamento (1-3): ").strip()
        
        forma_pagamento_nome = obter_nome_pagamento(op_pagamento)
        if forma_pagamento_nome == "":
            print("\n[ERRO] Opção de pagamento inválida. Digite 1, 2 ou 3.")

    # Apresentação do recibo final
    exibir_resumo(
        nome_cliente,
        total_compra,
        percentual_desc,
        valor_desc,
        total_final,
        forma_pagamento_nome
    )

# Execução do programa
if __name__ == "__main__":
    main()