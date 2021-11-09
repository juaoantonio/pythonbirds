"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar

A Direção terá a responsabilidade de controlar a direção. Ela
oferece os seguintes atributos:
1) Valor de direção com valores possíveis: 'Norte', 'Sul', 'Leste', 'Oeste'
2) Método girar à direita
3) Método girar à esquerda

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0

    >>> motor.acelerar()
    >>> motor.velocidade
    1

    >>> motor.acelerar()
    >>> motor.velocidade
    2

    >>> motor.acelerar()
    >>> motor.velocidade
    3

    >>> motor.frear()
    >>> motor.velocidade
    1

    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando Direção
    >>> # Virando para a direita
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'

    >>> # Virando para a esquerda
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> # Construindo o carro
    >>> carro = Carro()
    >>> # Testetando a velocidade
    >>> carro.calcular_velocidade()
    0

    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1

    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2

    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0

    >>> # Testetando a direção
    >>> carro.calcular_direcao()
    'Norte'

    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'

    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotacao_direita_dict = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE,
    }

    rotacao_esquerda_dict = {
        NORTE: OESTE,
        LESTE: NORTE,
        SUL: LESTE,
        OESTE: SUL,
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_esquerda_dict[self.valor]


class Carro:
    def __init__(self):
        self.motor = Motor()
        self.direcao = Direcao()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
