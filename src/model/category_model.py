class CategoryModel:
    __nome:str
    __descricao:str

    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def get_descricao(self):
        return self.__descricao
    
    @get_nome.setter
    def set_nome(self, nome):
        self.__nome = nome
    
    @get_descricao.setter
    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def __str__(self) -> str:
        return f'{self.get_nome}; {self.get_descricao}'
    
    @staticmethod
    def lista_para_objeto(lista_categoria:list) -> object:
        categoria = CategoryModel()
        categoria.set_nome = lista_categoria[0]
        categoria.set_descricao = lista_categoria[1]
        return categoria