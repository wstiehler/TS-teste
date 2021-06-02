class ProductModel:
    __nome:str
    __descricao:str
    __valor:float

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_descricao(self):
        return self.__descricao

    @property
    def get_valor(self):
        return self.__valor

    @get_nome.setter
    def set_nome(self, nome):
        self.__nome = nome
        
    @get_descricao.setter
    def set_descricao(self, descricao):
        self.__descricao = descricao

    @get_valor.setter
    def set_valor(self, valor):
        self.__valor = valor

    def __str__(self) -> str:
        return f'{self.get_nome};{self.get_descricao};{self.get_valor}'
    
    @staticmethod
    def lista_para_objeto(lista:list) -> object:
        produto = ProductModel()
        produto.set_nome = lista[0]
        produto.set_descricao = lista[1]
        produto.set_valor = lista[2]
        return produto

prod = ProductModel()
assert type(prod) == ProductModel

nome = 'teste'
descricao = 'teste'
valor = 100.00

prod.set_nome = nome
prod.set_descricao = descricao
prod.set_valor = valor

assert isinstance(prod.get_nome, str)
assert isinstance(prod.get_descricao, str)
assert isinstance(prod.get_valor, float)