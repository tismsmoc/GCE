from app.domain.consumo import calcular_quantidade_copias


def test_calcular_quantidade_copias():
    resultado = calcular_quantidade_copias(
        contador_inicial=301234,
        contador_final=304813,
    )

    assert resultado == 3579