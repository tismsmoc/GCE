## Descrição

Descreva de forma clara e objetiva o que foi implementado ou alterado neste Pull Request.

Exemplo:

> Adiciona o cálculo da quantidade de cópias a partir do contador inicial e contador final.

---

## Motivação

Explique por que esta alteração é necessária e qual problema ela resolve.

Exemplo:

> Essa regra será utilizada para calcular o consumo mensal de impressão das unidades.

---

## Tipo de alteração

Marque as opções aplicáveis:

- [ ] Nova funcionalidade (`feat`)
- [ ] Correção de erro (`fix`)
- [ ] Refatoração (`refactor`)
- [ ] Testes (`test`)
- [ ] Documentação (`docs`)
- [ ] Configuração/manutenção (`chore`)

---

## Regra de negócio envolvida

Descreva a regra de negócio implementada ou alterada.

Caso não exista regra de negócio envolvida, escreva:

> Não se aplica.

Exemplo:

> Quantidade de cópias = contador final - contador inicial.

---

## Como foi implementado

Explique resumidamente a solução adotada.

Evite apenas repetir o código. Descreva a ideia da implementação.

Exemplo:

> Foi criada uma função no módulo de domínio `consumo.py` que recebe os contadores inicial e final e retorna a diferença entre eles.

---

## Testes realizados

Informe quais testes foram executados.

Exemplo:

`uv run pytest -v`

Resultado esperado:

`1 passed`

Caso tenham sido adicionados novos testes, descreva brevemente quais comportamentos eles validam.

---

## Checklist

Antes de solicitar a revisão, confirme:

- [ ] O código executa corretamente.
- [ ] Os testes automatizados estão passando.
- [ ] Foram adicionados ou atualizados testes quando necessário.
- [ ] Não existe código comentado ou código temporário desnecessário.
- [ ] Não foram adicionadas credenciais, senhas, tokens ou dados sensíveis.
- [ ] Os nomes de funções, classes e variáveis são claros.
- [ ] A alteração está limitada ao objetivo deste Pull Request.
- [ ] Revisei meu próprio código antes de solicitar a revisão.
- [ ] A branch está atualizada com a `main`, quando necessário.

---

## Observações para o revisor

Informe aqui qualquer ponto que mereça atenção especial durante o Code Review.

Exemplos:

- Dúvida sobre uma decisão de implementação.
- Comportamento que ainda precisa ser discutido.
- Impacto em outra parte do sistema.
- Possível refatoração futura.

Caso não exista nenhuma observação:

> Nenhuma.