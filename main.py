from menu import products
from management import product_handler
from management import tab_handler

if __name__ == "__main__":

    print(product_handler.get_product_by_id(25))
    
    print(product_handler.get_products_by_type('vegetable'))
    
    print(product_handler.menu_report())
    
    print(product_handler.add_product(products,{
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }))
    
    print(tab_handler.calculate_tab(
        [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    ))