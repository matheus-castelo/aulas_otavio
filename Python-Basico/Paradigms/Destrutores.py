class Pessoa:
    # Construtor
    def __init__(self, nome):
        self.nome = nome
        print(f"{self.nome} foi criado.")  # Executa quando o objeto é criado

    # Destrutor
    def __del__(self):
        print(f"{self.nome} foi destruído.")  # Executa quando o objeto é destruído

# Criando o objeto: chama __init__
p = Pessoa("Matheus")
# Saída: Matheus foi criado.
print(p) # <__main__.Pessoa object at 0x7f3389b36a50>


# Aqui podemos usar o objeto normalmente
print(f"O nome da pessoa é {p.nome}")
# Saída: O nome da pessoa é Matheus

# Deletando o objeto manualmente: chama __del__
del p
# Saída: Matheus foi destruído

try:
    print(p)
except:
    print("Erro ao dar print(p) ! Não existe o objeto P")