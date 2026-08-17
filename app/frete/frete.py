def classificar_frete(peso_kg: float, regiao: str, premium: bool) -> str:
    if peso_kg <= 0:
        return "invalido"

    regiao_limpa = regiao.strip().lower()

    if regiao_limpa not in {"local", "estadual", "nacional"}:
        return "regiao_invalida"

    if premium:
        return "frete_gratis"

    if regiao_limpa == "local":
        return "frete_reduzido"

    return "frete_padrao"