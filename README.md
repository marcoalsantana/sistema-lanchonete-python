# Sistema de Atendimento e Pedidos de Lanchonete

**Estudante:** Marco Aurélio Landim de Santana  
**Disciplina:** Algoritmos e Programação  

---

## 📝 Descrição do Projeto
O programa simula o processo de atendimento e gerenciamento de pedidos de uma pequena lanchonete, operado via terminal interativo. Desenvolvido para aplicar conceitos básicos da lógica de programação sem o uso de estruturas de dados avançadas (como listas, dicionários ou tuplas).

---

## ⚙️ Funcionalidades Implementadas
- **Identificação do Cliente:** Captura e validação do nome do cliente ao iniciar o pedido.
- **Cardápio Interativo:** Apresentação clara de códigos, nomes e valores dos produtos.
- **Acúmulo de Pedidos:** Permite a seleção contínua de múltiplos itens e quantidades, calculando subtotais individualmente.
- **Tratamento de Exceções e Validação:** Impede falhas do sistema caso o usuário digite códigos inexistentes, quantidades inválidas ou textos incorretos.
- **Cálculo Automático de Descontos:**
  - Compras abaixo de R$ 50,00: **0% de desconto**
  - Compras entre R$ 50,00 e R$ 99,99: **5% de desconto**
  - Compras iguais ou superiores a R$ 100,00: **10% de desconto**
- **Formas de Pagamento:** Suporte para Dinheiro, PIX e Cartão com validação estruturada em `match-case`.
- **Recibo de Fechamento:** Exibição clara e organizada contendo o resumo completo das operações realizadas.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Possuir o **Python 3.10+** instalado em sua máquina.

### Passos
1. Clone ou baixe este repositório:
   ```bash
   git clone [https://github.com/marcoalsantana/sistema-lanchonete-python.git](https://github.com/marcoalsantana/sistema-lanchonete-python.git)