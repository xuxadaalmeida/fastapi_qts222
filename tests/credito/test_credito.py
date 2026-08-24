import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrição_cadastral, saida_esperada",
    [
        (-2, 50, 50, "renda_invalida"),
        (-5, -10, True, "renda_invalida"),
        (30, -15, False, "score_invalido"),
        (40, 1500, False, "score_invalido"),
        (50, 500, True, "reprovado"),
        (60, 280, False, "reprovado"),
        (700, 585, False, "aprovado_padrao"),
        (390, 950, False, "aprovado_premium")
    ],
)
def test_classificar_frete_caixa_preta(
    renda_mensal, score_credito, restrição_cadastral, saida_esperada
):
    assert classificar_credito(renda_mensal, score_credito, restrição_cadastral) == saida_esperada