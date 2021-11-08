class Pessoa:
    # Atributos de classe
    olhos = 2

    def __init__(self, *filhos,nome=None, idade=None):
        # Atributos de instância
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
    del luciano.filhos  # Removendo o atributo complexo criado anteriormente

    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)  # Ver os atributos presentes no objeto
    print(renzo.__dict__)  # Ver os atributos presentes no objeto

    Pessoa.olhos = 3


    print(luciano.olhos)
    print(renzo.olhos)
    print(Pessoa.olhos)
    print(id(luciano.olhos), id(renzo.olhos), id(Pessoa.olhos))
