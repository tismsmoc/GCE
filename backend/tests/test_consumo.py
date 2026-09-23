from decimal import Decimal

from app.domain.consumo import (
    calcular_quantidade_copias,
    calcular_valor_consumido,
)

def test_calcular_quantidade_copias():
    resultado = calcular_quantidade_copias(
        contador_inicial=301234,
        contador_final=304813,
    )

    assert resultado == 3579

def test_calcular_valor_consumido():
    resultado = calcular_valor_consumido(
        quantidade_copias=3579,
    )

    assert resultado == Decimal("143.16")