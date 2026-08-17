import pytest

from app.frete.frete import classificar_frete

@pytest.mark.parametrize(
    "peso_kg, regiao, premium, retorno_esperado",
    [
        (0, "local", True, "invalido"),
        (-1, "estadual", False, "invalido"),
        (5, "internacional", False, "regiao_invalida"),
        (2, "local", True, "frete_gratis"),
        (3, "local", False, "frete_reduzido"),
        (3, "estadual", False, "frete_padrao"),
        (3, "nacional", False, "frete_padrao")
    ],
)
def test_classificar_frete_caixa_preta(
    peso_kg, regiao, premium, retorno_esperado
):
    assert classificar_frete(peso_kg, regiao, premium) == retorno_esperado