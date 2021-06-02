from src.dao.category_dao import CategoryDao
from src.model.category_model import CategoryModel

from src.dao.produto_dao import ProductDao
from src.model.product_model import ProductModel

print('=' * 15, "Imprimindo lista de Categorias", '=' *15)
categoria1 = CategoryModel()
categoria1.set_nome = "TesteNome"
categoria1.set_descricao = "TesteDescricao"

categoria_dao = CategoryDao(categoria1)
categoria_dao.cadastrar(categoria1)

lista = categoria_dao.ler()
for item in lista:
    print(item)
    
print('=' * 15, "Imprimindo lista de Produtos", '=' *15)
product1 = ProductModel()
product1.set_nome = "TesteNome"
product1.set_descricao = "TesteDescricao"
product1.set_valor = 10.0

product_dao = ProductDao(product1)
product_dao.cadastrar(product1)

lista = product_dao.ler()
for item in lista:
    print(item)