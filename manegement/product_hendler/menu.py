import original_menu from 

def get_product_by_id(_id: int) -> dict:
    # Caso o produto referente ao id seja encontrado no menu, retorná-lo.
    # Caso o produto referente ao id não seja encontrado no menu, retornar um dicionário vazio.
    ...

def get_products_by_type(type: str) -> list:
    # Caso nenhum produto referente ao tipo seja encontrado, retornar uma lista vazia.
    # Caso encontrados, deve ser retornada uma lista contendo todos os produtos do tipo especificado.
    ...

def menu_report() -> str:
    # Você deverá montar um report sobre algumas características do menu de produtos:
        # Product Count: Contagem do total de produtos do menu.
        # Average Price: Média dos preços de todos os produtos do menu, arredondada para 2 casas decimais no máximo.
        # Most Common Type: O tipo de produto mais comum, ou seja, o tipo que contém maior quantidade de produtos no menu.
    def get_product_count():
        ...
    def get_average_price():
        ...
    def get_most_common_type():
        ...

    
    report = {
        "Product Count":"",
        "Average Price":"",
        "Most Common Type":""
    }
    # O retorno deve ser uma string formatada exatamente como no exemplo abaixo, com o devido dinamismo de cada característica:
        # "Products Count: <contagem_de_produtos> - Average Price: $<preco_medio> - Most Common Type: <tipo_mais_comum>"