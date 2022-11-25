from .original_menu import original_products

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
    # Você deverá montar um report sobre algumas características do menu de produtos:
        # Product Count: Contagem do total de produtos do menu.
    def get_product_count():
        ...
        # Average Price: Média dos preços de todos os produtos do menu, arredondada para 2 casas decimais no máximo.
    def get_average_price():
        ...
        # Most Common Type: O tipo de produto mais comum, ou seja, o tipo que contém maior quantidade de produtos no menu.
    def get_most_common_type():
        ...

    report = {
        "Product Count":get_product_count,
        "Average Price":get_average_price,
        "Most Common Type":get_most_common_type
    }
    
    return str(report)
    # O retorno deve ser uma string formatada exatamente como no exemplo abaixo, com o devido dinamismo de cada característica:
        # "Products Count: <contagem_de_produtos> - Average Price: $<preco_medio> - Most Common Type: <tipo_mais_comum>"