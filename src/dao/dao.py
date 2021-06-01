class Dao:

    def __init__(self, nome_arquivo) -> None:
        self.arquivo = nome_arquivo
    
    def cadastrar(self, dado):
        with open(self.arquivo, 'a') as arquivo:
            arquivo.write(f'{dado}\n')
    
    def ler(self):
        with open(self.arquivo, 'r') as arquivo:
            lista = []
            for linha in arquivo:
                dado = linha.strip()
                lista.append(dado)
        return lista
    
    