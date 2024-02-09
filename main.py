#import ContasBancos #importando a classe que foi criada

#Importando por parte
from Exercicios_2 import CartaoDeCredito, ContaCorrente

"""
    Esse é o arquivo principal de utilizar das classes vistas na Aula 12. 
    Serão importados para este arquivo todas as classes ContasBancos.py
"""

cartao_gabriel = ContaCorrente(1000, "José Gabriel", "111.000.222-33", 1, 1234)
cartao_credito = CartaoDeCredito("José Gabriel", cartao_gabriel)

cartao_credito.senha = "1111"
