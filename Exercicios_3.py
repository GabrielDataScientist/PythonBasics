"""
    Esse arquivo se refere a Aula12(Classes), com o adicional de polimorfismos e herança de classe.
"""

class Agencia:
    def __init__(self, telefone: str, cnpj: str, numero: int) -> None:
        
        """
            telefone: (DD)9XXXX-XXXX
            cnpj: XX-XXX-XXX/XXXX-XX
            numero: XXX
        """
        self.telefone = telefone
        self.cnpj = cnpj
        self.agencia = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa <= 0:
            print("O caixa está vazio!")
        else:
            print(f"O valor do caixa é: R${self.caixa}")

    def emprestar_dinheiro(self, valor: int, cpf: str, juros: float):
        if self.caixa < valor:
            print("Valor do empréstimo maior do que o valor em caixa.")
            print(f"Valor empréstimo: {valor}. Valor em caixa: {self.caixa}")
        else:
            self.emprestimos.append((valor, cpf, juros))
            print("Empréstimo contratado com sucesso!")

    def adicionar_cliente(self, nome: str, cpf: str, patrimonio: int):
        self.clientes.append((nome, cpf, patrimonio))





class AgenciaVirtual(Agencia):
    #Construtor de classe da Agencia Virtual
    def __init__(self, site: str):
        self.site = site
        #Chamando o __init__ da classe principal(Agencia)
        super().__init__("telefone", "12.222.222/0001-33", 1000 )
        


class AgenciaComum(Agencia):
    pass

class AgenciaPremium(Agencia):
    pass



minha_agencia = Agencia("(31)91111-2222", "11-111-111/0001-22", 100)
minha_agencia.caixa = 10000000

minha_agencia.verificar_caixa()
minha_agencia.emprestar_dinheiro(10000, "111.222.333-44", 0.02)
print(minha_agencia.emprestimos)

minha_agencia.adicionar_cliente("José Gabriel", "111.222.333-44", 10000)
print(minha_agencia.clientes)

agencia_virtual = AgenciaVirtual("www.minhaagencia.com.br")
print(agencia_virtual.site)
print(agencia_virtual.agencia)
print(agencia_virtual.cnpj)