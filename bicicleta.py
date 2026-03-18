class bicicleta:
    def __init__(self,modelo,cor,ano,valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("parando...")
        print("bicicleta parada!!!")

    def correr(self):
        print("vrummm...")

b1 = bicicleta("bmx", "preta" , "2020" , "1200")
print (f"cor: {b1.cor} \nmodelo: {b1.modelo} \nano: {b1.ano} \nvalor: {b1.valor}")
b1.buzinar()
b1.correr()
b1.parar() 
print("\n")

b2 = bicicleta("caloi", "azul" , "2015", "550")
print(f"cor: {b2.cor} \nmodelo: {b2.modelo} \nano: {b2.ano} \nvalor: {b2.valor}")
b2.buzinar()
b2.correr()
b2.parar()
