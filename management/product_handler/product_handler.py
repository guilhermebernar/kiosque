from tests.data import original_products
import pandas as pd

from collections import Counter

def get_product_by_id(id: int) -> dict:
    for product in original_products:  
        _id = product["_id"]
        if _id == id:    
            return product
    return {}

def get_products_by_type(search_type: str) -> list:
    new_list = []
    for product in original_products:
        find_type = product["type"]
        if find_type == search_type:
            new_list.append(product)
    
    return new_list

def menu_report() -> str:

    get_product_count = len(original_products)

    sum_prices = sum(d['price'] for d in original_products)
        
    get_average_price = round(sum_prices/get_product_count, 2)

    df = pd.DataFrame(original_products)
    most_common = df['type'].value_counts().idxmax()

    report = {
        "Product Count":get_product_count,
        "Average Price":get_average_price,
        "Most Common Type":most_common
    }
    
    return str(report)

def add_product(menu: list, product: dict) -> str:
    
    id_list = []

    for item in menu:  
        id_list.append(item["_id"]) 
    id_generation = max(id_list)+1 
    if id_generation == 0: 
        id_generation = 1
    
    new_product = {
        "_id":id_generation,
        "description": product['description'],
        "price": product['price'],
        "rating": product['rating'],
        "title": product['title'],
        "type": product['type'],
    }
    
    menu.append(new_product)

    return new_product