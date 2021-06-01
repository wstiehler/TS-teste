from src.dao.dao import Dao
from src.model.product_model import ProductModel

class ProductDao(Dao):

    def __init__(self, nome_arquivo) -> None:
        nome_arquivo = 'product.txt'
        super().__init__(nome_arquivo)
    
    def cadastrar(self, product:ProductModel):
        return super().cadastrar(product)
    
    def ler(self):
        lista = super().ler()
        lista__produtos = []
        for linha in lista:
            linha_dados = str(linha).split(';')
            produto = ProductModel.lista_para_objeto(linha_dados)
            lista__produtos.append(produto)
        return lista__produtos

