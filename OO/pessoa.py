class Pessoa:
    def __init__(self, *filhos,nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho'  # Adicionando atributos dinâmicos

    print(luciano.__dict__)  # Ver os atributos presentes no objeto
    print(renzo.__dict__)  # Ver os atributos presentes no objeto

    del luciano.sobrenome  # Removendo o atributo dinâmico criado anteriormente