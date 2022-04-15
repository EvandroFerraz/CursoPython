"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.conta = None
    
    def inserir_conta(self, conta):
        self.conta = conta

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()
        
    def detalhes(self):
        print(f'Agência: {self.agencia}'
              f'Conta: {self.conta}'
              f'Saldo: {self.saldo}')
    
    @abstractmethod    
    def sacar(self, valor): pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
        
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        self.detalhes()

class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
    
banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')