class simbolo(object):
    def __init__(self, nome, numLinha, vireParaFinal = None, vireParaInicio = None):
        self.nome = nome
        self.numLinha = numLinha
        self.vireParaFinal = vireParaFinal
        self.vireParaInicio = vireParaInicio

class tabelaS(object):
    def __init__(self):
        self.simbolos = {}

    def inserir(self, simbolo):
        self.simbolos[simbolo.nome] = simbolo

    def lookup(self, nome):

        simbolo = self.simbolos.get(nome)
        
        return simbolo

    
        
