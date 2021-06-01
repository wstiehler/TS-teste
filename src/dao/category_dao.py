from src.dao.dao import Dao 
from src.model.category_model import CategoryModel

class CategoryDao(Dao):

    def __init__(self, nome_arquivo) -> None:
        nome_arquivo = 'category.txt'
        super().__init__(nome_arquivo)
    
    def cadastrar(self, category:CategoryModel):
        return super().cadastrar(category)
    
    def ler(self):
        lista = super().ler()
        lista_categorias = []
        for linha in lista:
            linha_dados = str(linha).split(';')
            categoria = CategoryModel.lista_para_objeto(linha_dados)
            lista_categorias.append(categoria)
        return lista_categorias