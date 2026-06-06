# Tabela mensal do IRPF de 2026
# Fonte: Receita Federal

DEDUCAO_DEPENDENTE = 189.59

TABELA_IR = [
    {
        "limite_min": 0.00,
        "limite_max": 2428.80,
        "aliquota": 0.00,
        "deducao": 0.00
    },
    {
        "limite_min": 2428.81,
        "limite_max": 2826.65,
        "aliquota": 0.075,
        "deducao": 182.16
    },
    {
        "limite_min": 2826.66,
        "limite_max": 3751.05,
        "aliquota": 0.15,
        "deducao": 394.16
    },
    {
        "limite_min": 3751.06,
        "limite_max": 4664.68,
        "aliquota": 0.225,
        "deducao": 675.49
    },
    {
        "limite_min": 4664.69,
        "limite_max": None,
        "aliquota": 0.275,
        "deducao": 908.73
    }
]