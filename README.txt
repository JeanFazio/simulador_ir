# Simulador de Cálculo de IR Mensal

Projeto em Python com interface gráfica para simular o cálculo do Imposto de Renda Retido na Fonte (IRRF) sobre salário mensal.

## Visão geral

O sistema permite informar:

- salário bruto
- desconto de INSS
- quantidade de dependentes
- outras deduções

Com esses dados, o aplicativo calcula:

- base de cálculo
- alíquota aplicada
- parcela a deduzir
- imposto de renda devido
- salário líquido aproximado

## Funcionalidades

- interface gráfica simples e intuitiva com Tkinter
- validação de valores negativos e entradas inválidas
- formatação monetária em reais
- exibição detalhada do resultado da simulação
- botão para limpar os campos rapidamente

## Estrutura do projeto

```text
simulador_ir/
├── main.py
├── calculadora_ir.py
├── dados_ir.py
├── formatador.py
└── README.txt
```

## Arquivos principais

### `main.py`
Responsável pela interface gráfica, leitura dos dados digitados pelo usuário e exibição do resultado.

### `calculadora_ir.py`
Contém a lógica de cálculo do IR com base na tabela mensal e nas deduções informadas.

### `dados_ir.py`
Armazena a tabela do IR e o valor de dedução por dependente.

### `formatador.py`
Possui funções auxiliares para formatar valores monetários e percentuais.

## Requisitos

- Python 3.10 ou superior
- Tkinter instalado no ambiente Python

> Em muitas instalações do Python, o Tkinter já vem incluído.

## Como executar

1. Abra um terminal na pasta do projeto.
2. Execute o arquivo principal:

```bash
python main.py ou py main.py
```

Se o seu ambiente usar o comando `python3`, use:

```bash
python3 main.py
```

## Como usar

1. Informe o salário bruto.
2. Informe o desconto de INSS.
3. Informe a quantidade de dependentes.
4. Informe outras deduções, se houver.
5. Clique em **Calcular IR**.

O resultado será exibido com os valores detalhados da simulação.

## Observações importantes

- O cálculo considera a tabela mensal do IRPF de 2026 definida em `dados_ir.py`.
- O projeto utiliza uma lógica simplificada de simulação.
- A regra de redução mensal de 2026 ainda não foi implementada no código.
- O valor final apresentado deve ser entendido como estimativa.

## Exemplo de entrada

- Salário bruto: `5000`
- Desconto INSS: `550,00`
- Dependentes: `1`
- Outras deduções: `200,00`

## Exemplo de saída

O aplicativo exibirá informações como:

- salário bruto
- desconto INSS
- dedução por dependentes
- base de cálculo
- alíquota aplicada
- parcela a deduzir
- IR devido
- salário líquido aproximado

## Limpeza dos campos

O botão **Limpar** apaga os campos e redefine os valores padrões de dependentes e outras deduções para zero.

## Possíveis melhorias futuras

- incluir a nova regra de redução mensal do IR que ainda nao foi oficializada para salarios de até 5k
- adicionar cálculo por faixa com mais detalhes
- adaptar a interface para tema escuro
- criar versão web do simulador

## Autor

Projeto acadêmico desenvolvido para fins de estudo e simulação de cálculo de IR.
```
