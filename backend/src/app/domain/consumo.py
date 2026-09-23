from decimal import Decimal

VALOR_POR_COPIA = Decimal("0.04")

def calcular_quantidade_copias(
    contador_inicial: int,
    contador_final: int,
) -> int:
    return contador_final - contador_inicial

def calcular_valor_consumido(
    quantidade_copias: int,
) -> Decimal:
    return quantidade_copias * VALOR_POR_COPIA