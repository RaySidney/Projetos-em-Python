class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        vfinal = self.preco - (self.preco * (percentual / 100))
        print(f'O valor da camiseta com desconto é de: R${vfinal:.2f}')

    #Getter
    @property
    def preco(self):
        return self._preco

    def nome(self):
        return self._nome

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @nome.setter
    def nome(self, valor):
        if
        self.nome = valor




p1 = Produto('CAMISETA', 100)
p1.desconto(50)
print()

p2 = Produto('CALÇA', 'R$150')
p2.desconto(10)