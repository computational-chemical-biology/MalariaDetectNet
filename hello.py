# Código para saudar visitante
# Autor: Luiz Scurachio 
# Data: 10/02/25
# python hello.py <nome do visitante>
import sys

def hello(nome_visitante):
    '''
    Função que imprime uma mensagem de boas vindas.
    '''
    print(f'Olá {nome_visitante}, seja bem-vindo!')

if __name__=='__main__':
    hello(sys.argv[1])
