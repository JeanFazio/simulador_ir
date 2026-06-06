def formatar_moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def formatar_porcentagem(valor):
    return f"{valor * 100:.1f}%".replace(".", ",")