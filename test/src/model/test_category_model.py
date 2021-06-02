import os, sys
import unittest
sys.path.append(os.getcwd())

from src.model.category_model import CategoryModel



class TestCategoryModel(unittest.TestCase):

    def test_set_nome(self):
        #preparação
        category = CategoryModel()
        #ação
        category.set_nome = 'teste'
        #Assercao
        self.assertEqual(category.get_nome, 'teste')

    def test_set_descricao(self):
        #preparacao
        category = CategoryModel()
        #acao
        category.set_descricao = 'teste'
        #assercao
        self.assertEqual(category.get_descricao, 'teste')

    # def test_get_nome(self):
    #     #preparacao
    #     category = CategoryModel()
    #     #acao
    #     category.get_nome = "Teste"
    #     #assercao
    #     self.assertEqual(category.get_nome, 'Teste')

    # def test_lista_para_objeto(self):
    #     #preparacao
    #     category = CategoryModel()
    #     #acao
    #     category.lista_para_objeto(lista_categoria=list)
    #     category.set_nome = 'teste'
    #     category.set_descricao = 'teste'
    #     #assercao
    #     self.assertEquals(category.lista_para_objeto(lista_categoria=[]), 'item1', 'item2')

    #teste