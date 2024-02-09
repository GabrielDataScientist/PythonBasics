import pytz #Essa bib faz o ajuste de fuso horário (pytz - python timezone)
from datetime import datetime
from random import randint

"""
    Essa parte é exatemente igual a Aula 12(Classes), porém ao invés de utilizar o JupyterNotebook,
    vou utilizar o VSCode para separar as classes por módulos.

"""
class ContaCorrente:
    
    #Função estática declarada no escopo global da classe para retornar a hora

    """
        Classe para criação de uma conta no banco
    """
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime("%d/%m/%Y %H:%M:%S")
    
    def __init__(self, saldo: int, nome: str, cpf: str, agencia: int, num_conta: int):
        self._saldo = saldo
        self._nome = nome
        self._cpf = cpf
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacao = []
        self._cartoes = []
    
    def consultar_saldo(self):
        print(f"Seu saldo é: R${self._saldo}")
    
    def depositar(self, valor):
        self.saldo_inicial = self._saldo
        self._saldo += valor
        self.consultar_saldo()
        self.transacao.append({'TransactType':'Deposit', 'Datetime': ContaCorrente._data_hora(), 
                               'InitialAmmount':self.saldo_inicial, 'TransactValue': valor, 'TotalAmmount': self._saldo})
    
    def sacar(self, valor):
        self.saldo_inicial = self._saldo
        if (self._saldo < valor):
            print("Saldo insuficiente")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.consultar_saldo()
            self.transacao.append({'TransactType':'Withdraw', 'InitialAmmount':self.saldo_inicial, 
                               'TransactValue': valor, 'TotalAmmount': self._saldo})
    
    def mostra_hist_transacao(self):
        print("Histórico de transações")
        for transacao in self.transacao:
            print(self.transacao)
            
    def transferir(self, valor, conta_destino):
        self.saldo_inicial = self._saldo
        if (self._saldo < valor):
            print("Saldo insuficiente")
            self.consultar_saldo()
        else:
            #informações desta conta
            print("Trasnferência realizada com sucesso!")
            self.consultar_saldo()
            print(f"Valor transferido: R${valor}")
            self._saldo -= valor
            self.consultar_saldo()
            self.transacao.append({'TransactType':'Withdraw', 'InitialAmmount':self.saldo_inicial, 
                               'TransactValue': valor, 'TotalAmmount': self._saldo})
            #informações da conta destino
            conta_destino._saldo =+ valor
            conta_destino.transacao.append({'TransactType':'Withdraw', 'InitialAmmount':self.saldo_inicial, 
                               'TransactValue': valor, 'TotalAmmount': self._saldo})

class CartaoDeCredito():
    
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br
    
    def __init__(self, titular: str, conta_corrente: int):
        self._titular = titular
        self._conta_corrente = conta_corrente
        self._num_cartao = randint(1000000000000000, 9999999999999999)
        self._validade = "{}/{}".format(CartaoDeCredito._data_hora().month, CartaoDeCredito._data_hora().year + 4)
        self._cod_seguranca = "{}{}{}".format(randint(0, 9), randint(0, 9), randint(0, 9))
        self._limite = 5000
        self._senha = ""
        conta_corrente._cartoes.append(self)
    
    #Getter - Quando printa
    @property
    def senha(self):
        return self._senha
    
    #Setter - Quando define um novo valor para a variável
    #@property.setter
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print("Senha alterada com sucesso!")
        else:
            print("Senha inválida.")