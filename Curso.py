
class Curso:
    def __init__(self, tema, descricao, preco, cpfDoCliente, numeroDeTransacao):
        self.tema = tema
        self.descricao = descricao
        self.preco = preco
        self.__cpfDoCliente = cpfDoCliente
        self.__numeroDeTransacao = numeroDeTransacao

    def get_tema(self):
        return self.tema

    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        return self.preco

    def InformacoesDaCompra(self):
        print("--- INFORMAÇÕES DA COMPRA ---")
        print(f"Tema: {self.tema}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"CPF do Cliente: {self.__cpfDoCliente}")
        print(f"Número da Transação: {self.__numeroDeTransacao}")

curso1 = Curso("Python Do Básico", "Aprenda do zero", 45.90, "390335618-24", "00123")


curso1.InformacoesDaCompra()

print("-----------------------------")


print(curso1)
