from tests.data import original_products
from management.product_handler import product_handler
import pandas as pd

from typing import List, Dict

def calculate_tab(pedidos):
    # laço de repetição para cada item da lista
    list_prices = []
    list_amount = []

    for pedido in pedidos:

        get_product = product_handler.get_product_by_id(pedido["_id"])
        amount = pedido["amount"]
        
        products_prices = get_product["price"]
        list_prices.append(products_prices)
        list_amount.append(amount)
    
    df1 = pd.DataFrame(list_prices, columns=['precos'])
    df2 = pd.DataFrame(list_amount, columns=['quantidade'])

    df1['resultado'] = df1['precos'] * df2['quantidade']
    list_total = list(df1['resultado'])
    
    total = round(sum(list_total,2),2)


    print({'subtotal': f'{total}'})