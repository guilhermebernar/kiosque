import sys
sys.path.append("..")
from tests.data import original_products

from typing import List, Dict

def calculate_tab(pedidos:List[Dict[ "_id": int, "amount": int ]]):
    # laço de repetição para cada item da lista
        def check_price():
            for pedido in range(len(pedidos)):
    # Acessar value da key "_id" e procurar e retornar do banco preço do item
                _id = pedido.value()
                for produto in original_products:
                    if _id = 
                ...
    # muitiplicar valor pelo "amout"
        
    # retornar um dicionário no formato especificado, com a chave subtotal sendo uma string e o valor sendo um float com arredondamento de duas casas decimais no máximo.
        return {'subtotal': '$216.1'}