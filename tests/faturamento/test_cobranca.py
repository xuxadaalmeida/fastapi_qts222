import pytest
import time

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, esperado",
    [
        (0.0, "PREMIUM", -5, -1.0),
        (100.0, "PREMIUM", -1, -1.0),
        (100.0, "INVALIDO", 0, -2.0),
        (100.0, "", 0, -2.0),
        (100.0, "BASICO", 0, 100.0),
        (100.0, "PREMIUM", 0, 90.0),
        (100.0, "EMPRESARIAL", 0, 80.0),
        (100.0, "basico", 0, 100.0),
        (100.0, " PREMIUM ", 0, 90.0),
        (100.0, "BASICO", 1, 105.5),
        (100.0, "PREMIUM", 10, 99.5),
        (100.0, "EMPRESARIAL", 30, 97.0),
        (100.0, "BASICO", 31, 156.0),
        (100.0, "PREMIUM", 40, 151.0),
        (100.0, "EMPRESARIAL", 60, 153.0),
    ]
)
def test_processar_cobranca(valor_base, plano, dias_atraso, esperado):
    assert processar_cobranca(valor_base, plano, dias_atraso) == esperado

def test_tempo_processamento_cobranca_nao_funcional():
    inicio = time.perf_counter()
    resultado = processar_cobranca (100.0, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado == 100.0
    assert tempo_decorrido < 0.1