import unittest
from src.model.product_model import ProductModel

class TestProductModel(unittest.TestCase):

    def test_set_nome(self):
        #preparacao
        product = ProductModel()
        #acao
        product.set_nome = 'teste'
        #assercao
        self.assertEqual(product.get_nome, 'teste')

    def test_set_descricao(self):
        #preparacao
        product = ProductModel()
        #acao
        product.set_descricao = 'teste'
        #assercao
        self.assertEqual(product.get_descricao, 'teste')
    
    def test_set_valor(self):
        #preparacao
        product = ProductModel()
        #acao
        product.set_valor = 10.90
        #assercao
        self.assertEqual(product.get_valor, 10.90)