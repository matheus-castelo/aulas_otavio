class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setIdade(self, nova_idade):
        self.idade = nova_idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."


pessoa1 = Pessoa("Matheus", 20)
print(pessoa1.getNome())
print(pessoa1.getIdade())
print(pessoa1.apresentar())

pessoa1.setIdade(21)
print(pessoa1.apresentar())