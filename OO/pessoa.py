class Pessoa:
    # Atributos de classe
    olhos = 2

    # Métodos de Instância
    def __init__(self, *filhos,nome=None, idade=None):
        # Atributos de instância
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    # Métodos de Classe
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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

    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(id(Pessoa.metodo_estatico), id(luciano.metodo_estatico))

    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
