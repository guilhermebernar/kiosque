import sys
sys.path.append("..")
from tests.data import original_products

from collections import Counter

def get_product_by_id(id: int) -> dict:

    for product in original_products:  
        _id = product.values()
        if _id == id:    
            return product
    return {}

def get_products_by_type(search_type: str) -> list:

    for product in original_products:
        type = product.values()
        if type == search_type:
            return [product]
    return []

def menu_report() -> str:

    def get_product_count() -> int:
         return len(
            [
                product for product in original_products 
                if isinstance(product, dict)
            ]
        )

    def get_average_price() -> int:
        sum_products = get_product_count()
        sum_prices = sum(d['price'] for d in original_products)
        
        return round(sum_prices/sum_products, 2)

    def get_most_common_type(): 
        counter = Counter(original_products.values())
        
        return counter.most_common[0]

    report = {
        "Product Count":get_product_count,
        "Average Price":get_average_price,
        "Most Common Type":get_most_common_type
    }
    
    return str(report)

def add_product(menu: list, product: dict) -> str:
    def id_generation () -> int:
        for product in menu:  
            _id = product.values()
            
            if _id > 0:
                return max(_id)+1
            
            return 1
    
    return menu.append({
        "_id":id_generation,
        "description": product.value('description'),
        "price": product.value('price'),
        "rating": product.value('rating'),
        "title": product.value('title'),
        "type": product.value('type'),
    })