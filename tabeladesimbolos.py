class simbolo(object):
    def __init__(self, nome, numLinha, tipo=None):
        self.nome = nome
        self.tipo = tipo
        self.numLinha = numLinha



class tabelaS(object):
    def __init__(self):
        self.simbolos = {}

    def inserir(self, simbolo):
        self.simbolos[simbolo.nome] = simbolo

    def lookup(self, nome):

        simbolo = self.simbolos.get(nome)
        
        return simbolo
