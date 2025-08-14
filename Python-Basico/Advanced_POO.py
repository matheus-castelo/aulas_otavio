"""
- Abstração
- Herança (simples e múltipla)
- Polimorfismo (duck typing + via hierarquia)
- Interfaces / Classes abstratas (abc)
- Sobrescrita (override) e chamada de método da superclasse (super() ~ base)
- "Sobrecarga" (overload) simulada com singledispatchmethod e parâmetros padrão
- Vários construtores (factory methods / classmethods)
- self (this) e super() (base)
- Encapsulamento (_protected, __private)
- Propriedades (property)
- Métodos estáticos e de classe
- MRO e herança múltipla
"""

from abc import ABC, abstractmethod
from functools import singledispatchmethod
from datetime import datetime

# ----------------------------
# INTERFACE / CLASSE ABSTRATA
# ----------------------------
class SerVivo(ABC):
    """Classe abstrata que age como 'interface' para seres vivos."""
    @abstractmethod
    def falar(self):
        """Toda subclasse deve implementar 'falar'."""
        pass

    # Método concreto disponível para todos (abstração parcial)
    def dormir(self):
        return "Zzz... dormindo"


class Calculavel(ABC):
    """Interface abstrata para formas que podem calcular área."""
    @abstractmethod
    def area(self):
        pass


# ----------------------------
# HERANÇA, ABSTRAÇÃO, OVERRIDE
# ----------------------------
class Animal(SerVivo): # Precisa implementar a Classe Abstrata SerVivo
    # Construtor básico
    def __init__(self, nome: str, idade: int):
        # self é o 'this' de C#
        self.nome = nome
        self._idade = idade          # _protected (convenção)
        self.__segredo = "não conte" # __private (name mangling)

    # Método "virtual" (em Python todos os métodos são potencialmente sobrescritos)
    def falar(self):
        return "<som genérico>"

    def idade(self):
        # Exemplo de método que poderia ser sobrescrito
        return self._idade

    def revelar_segredo(self):
        # Mostrar que __segredo sofre name-mangling (encapsulamento)
        return self.__segredo


class Cachorro(Animal): # Herança
    # Sobrescrita (override) do falar
    def falar(self):
        # chamando método da superclasse com super() ~ 'base' do C#
        base = super().falar()
        return f"Au au! (base: {base})"

    def buscar(self, objeto):
        return f"{self.nome} foi buscar {objeto}."


class Gato(Animal):
    def falar(self):
        return "Miau"


class Vaca(Animal):
    def falar(self):
        return "Muuu"


# ----------------------------
# POLIMORFISMO (duck typing + hierarquia)
# ----------------------------
def fazer_animal_falar(a: SerVivo):
    # Aceita qualquer SerVivo (ou duck-typed object com método falar)
    print(a.falar())


# ----------------------------
# "SOBRECARGA" (OVERLOAD) em Python
# Python não tem overload nativo; usamos técnicas:
# 1) parâmetros default / *args
# 2) singledispatchmethod (distribui por tipo)
# ----------------------------
class Calculadora:
    # Exemplo com parametros default (simula overload por número de args)
    def soma(self, a, b=0, c=0):
        return a + b + c

    # Exemplo com singledispatchmethod para sobrecarga por TIPO
    @singledispatchmethod
    def imprime(self, valor):
        print("Valor (default):", valor)

    @imprime.register
    def _(self, valor: int):
        print("Valor inteiro:", valor)

    @imprime.register
    def _(self, valor: str):
        print("Valor string:", valor.upper())

    @imprime.register
    def _(self, valor: list):
        print("Lista com", len(valor), "itens")


# ----------------------------
# VARIOS CONSTRUTORES (factory methods / classmethods)
# ----------------------------
class Pessoa:
    def __init__(self, nome: str, idade: int):
        # Construtor principal
        self.nome = nome
        self.idade = idade

    # Construtor alternativo: da data de nascimento
    @classmethod
    def from_birthyear(cls, nome: str, ano_nascimento: int):
        idade = datetime.now().year - ano_nascimento
        return cls(nome, idade)

    # Outro construtor alternativo (vazio)
    @classmethod
    def anonymous(cls):
        return cls("Anonimo", 0)

    def __repr__(self):
        return f"Pessoa(nome={self.nome!r}, idade={self.idade})"


# ----------------------------
# ENCAPSULAMENTO E PROPRIEDADES
# ----------------------------
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo      # "protected" por convenção

    @property
    def saldo(self):
        # Getter - transforma acesso em método
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        # Setter com validação
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self._saldo += valor


# ----------------------------
# HERANÇA MULTIPLA E MRO
# ----------------------------
class Nadador:
    def mover(self):
        return "Nadando"

class Voador:
    def mover(self):
        return "Voando"

class Pato(Nadador, Voador):
    # Herança múltipla: ordem (Nadador, Voador) influencia MRO
    def falar(self):
        return "Quack"

    # Podemos ainda chamar explicitamente o método de uma classe mãe:
    def mover_super_nadador(self):
        return Nadador.mover(self)

    def mover_super_voador(self):
        return Voador.mover(self)


# ----------------------------
# EXEMPLOS DE CLASSES ABSTRATAS PARA FORMAS GEOMETRICAS
# ----------------------------
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma, Calculavel):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * self.raio ** 2


# ----------------------------
# COMPOSIÇÃO (has-a) e AGGREGATION
# ----------------------------
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        return f"Motor {self.potencia}W ligado"

class Carro:
    def __init__(self, modelo, motor: Motor):
        # composição: Carro TEM um Motor
        self.modelo = modelo
        self.motor = motor

    def arrancar(self):
        return f"{self.modelo}: {self.motor.ligar()}"


# ----------------------------
# Demonstração / Testes
# ----------------------------
if __name__ == "__main__":
    print("=== HERANÇA & SOBRESCRITA ===")
    dog = Cachorro("Rex", 5)
    gato = Gato("Mimi", 3)
    vaca = Vaca("Bessie", 4)
    fazer_animal_falar(dog)
    fazer_animal_falar(gato)
    fazer_animal_falar(vaca)
    print(dog.buscar("bola"))

    print("\n=== ENCAPSULAMENTO (name mangling) ===")
    print("Segredo (via método):", dog.revelar_segredo())
    # Acesso direto a __segredo falharia; a forma real seria _Animal__segredo

    print("\n=== POLIMORFISMO (duck typing) ===")
    class Strange:
        def falar(self):
            return "Eu sou estranho mas falo!"
    fazer_animal_falar(Strange())

    print("\n=== SOBRECARGA (overload simulation) ===")
    calc = Calculadora()
    print("soma(1,2) =>", calc.soma(1,2))
    print("soma(1) =>", calc.soma(1))
    print("soma(1,2,3) =>", calc.soma(1,2,3))
    calc.imprime(42)
    calc.imprime("olá")
    calc.imprime([1,2,3])

    print("\n=== VARIOS CONSTRUTORES (factory methods) ===")
    p1 = Pessoa("Ana", 30)
    p2 = Pessoa.from_birthyear("Beatriz", 1990)
    p3 = Pessoa.anonymous()
    print(p1, p2, p3)

    print("\n=== PROPRIEDADES E VALIDAÇÃO ===")
    conta = ContaBancaria("Matheus", 100)
    print("Saldo:", conta.saldo)
    conta.depositar(50)
    print("Saldo após depósito:", conta.saldo)
    try:
        conta.saldo = -10
    except ValueError as e:
        print("Erro setter:", e)

    print("\n=== HERANÇA MÚLTIPLA E MRO ===")
    pato = Pato()
    print("Pato mover() ->", pato.mover())  # vem de Nadador por causa da ordem (MRO)
    print("Pato falar() ->", pato.falar())
    print("Chamar movimentos das superclasses:", pato.mover_super_nadador(), "/", pato.mover_super_voador())
    print("MRO de Pato:", [c.__name__ for c in Pato.mro()])

    print("\n=== CLASSES ABSTRATAS E INTERFACES ===")
    q = Quadrado(3)
    c = Circulo(2)
    print("Área quadrado:", q.area())
    print("Área círculo:", c.area())

    print("\n=== COMPOSIÇÃO ===")
    motor = Motor(500)
    carro = Carro("Fusca", motor)
    print(carro.arrancar())

    print("\n=== NOTAS RÁPIDAS ===")
    print("- self é o 'this' do C#.")
    print("- super() é o 'base' do C# (usado para chamar construtores/métodos da superclasse).")
    print("- Métodos em Python são 'virtuais' por padrão: uma subclasse pode sobrescrevê-los sem 'virtual'/'override'.")
    print("- 'Sobrecarga' clássica não existe: use parâmetros default, *args, ou singledispatchmethod para dispatch por tipo.")
