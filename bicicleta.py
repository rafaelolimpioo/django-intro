class bicicleta:
    def __init__(self,modelo,cor,ano,valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("parando...")
        print("bicicleta parada")

    def correr(self):
        print("vrummm...")

b1 = bicicleta("bmx", "preta" , "2020" , "1200")
b1.buzinar()
b1.correr()
b1.parar()

b2 = bicicleta("caloi", "azul" , "2015", "550 \n")
b2.buzinar()
b2.correr()
b2.parar()
