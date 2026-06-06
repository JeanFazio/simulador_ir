from dados_ir import TABELA_IR, DEDUCAO_DEPENDENTE


def encontrar_faixa(base_calculo):
    for faixa in TABELA_IR:
        limite_max = faixa["limite_max"]

        if limite_max is None:
            return faixa

        if base_calculo <= limite_max:
            return faixa

    """
    Regra de redução mensal de 2026:
    - até R$ 5.000,00: redução até zerar o imposto
    - de R$ 5.000,01 até R$ 7.350,00: redução decrescente
    - acima disso: sem redução
    - Nao fiz nesse aplicativo a regra, pois ainda nao foi implementada oficialmente, e pode sofrer alteraçõees.
    """

def calcular_ir(salario_bruto, desconto_inss, dependentes, outras_deducoes):
    deducao_dependentes = dependentes * DEDUCAO_DEPENDENTE

    base_calculo = salario_bruto - desconto_inss - deducao_dependentes - outras_deducoes

    if base_calculo < 0:
        base_calculo = 0

    faixa = encontrar_faixa(base_calculo)

    aliquota = faixa["aliquota"]
    parcela_deduzir = faixa["deducao"]

    ir_antes_reducao = (base_calculo * aliquota) - parcela_deduzir

    if ir_antes_reducao < 0:
        ir_antes_reducao = 0


    ir_final = ir_antes_reducao

    if ir_final < 0:
        ir_final = 0

    salario_liquido = salario_bruto - desconto_inss - ir_final

    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto_inss,
        "dependentes": dependentes,
        "deducao_dependentes": deducao_dependentes,
        "outras_deducoes": outras_deducoes,
        "base_calculo": base_calculo,
        "aliquota": aliquota,
        "parcela_deduzir": parcela_deduzir,
        "ir_final": ir_final,
        "salario_liquido": salario_liquido
    }