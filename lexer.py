
#coding: utf-8

import string
import array

class Token(object):
    reservadas = ['programainicio', 'execucaoinicio', 'fimexecucao',
    'definainstrucao', 'como',
    'inicio', 'fim', 
    'repita', 'vezes', 'fimrepita',
    'enquanto', 'faca', 'fimpara', 
    'se', 'entao', 'fimse', 'senao', 'fimsenao',
    'mova', 'passos', 'vire', 'para',
    'pare', 'finalize', 'apague', 'lampada', 'acenda', 'aguarde', 'ate',
    'robo', 'pronto', 'ocupado', 'parado', 'movimentando', 'frente', 'bloqueada', 'direita', 'esquerda', 'a', 'acesa', 'apagada', 'apagar', 'fimprograma', 'passo' ]

    reservada = 'reservadas'
    identificador = 'identificador'
    numero = 'numero'
    programainicio = 'programainicio'
    como = 'como'
    inicio = 'inicio'
    fim = 'fim'
    repita = 'repita'
    vezes = 'vezes'
    fimrepita = 'fimrepita'
    enquanto = 'enquanto'
    faca = 'faca'
    fimpara = 'fimpara'
    se = 'se'
    entao = 'entao'
    fimse = 'fimse'
    senao = 'senao'
    fimsenao = 'fimsenao'
    mova = 'mova'
    passos = 'passos'
    vire = 'vire'
    para = 'para'
    pare = 'pare'
    finalize = 'finalize'
    apague = 'apague'
    lampada = 'lampada'
    acenda = 'acenda'
    aguarde = 'aguarde'
    ate = 'ate'
    robo = 'robo'
    pronto = 'pronto'
    ocupado = 'ocupado'
    parado = 'parado'
    movimentando = 'movimentando'
    frente = 'frente'
    bloqueada = 'bloqueada'
    direita = 'direita'
    esquerda = 'esquerda'
    a = 'a'
    acesa = 'acesa'
    apagada = 'apagada'
    apague = 'apague'
    fimprograma = 'fimprograma'
    passo = 'passo'


    finalArquivo = 'EOF'

    def __init__(self, tipo, valor, linha, numLinha, posLinha):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
        self.posLinha = posLinha - len(valor)
        self.numLinha = numLinha

    def __str__(self):
        return  self.tipo.ljust(15) + self.valor

class Lexer(object):
    marcaFinal = '\0'
    branco = ' \t\n'
    pulaLinha = '\n'

    def __init__(self, entrada, linhasVazias=[]):
        super(Lexer, self).__init__()
        self.entrada = entrada
        self.marcador = 0
        self.tokens = []
        self.linhaAtual = entrada.split(Lexer.pulaLinha)
        self.numLinha = 0
        self.posLinha = 0
        self.linhasVazias = []

    def proxChar(self):
        self.marcador += 1
        self.posLinha += 1
        if self.marcador > len(self.entrada):
            return Lexer.marcaFinal
        return self.entrada[self.marcador - 1]

    def criaToken(self):
        contErro = 0
        leuDigito = 0
        leuBranco = 0
        erroId = 0
        stringId = ''
        stringNum = ''
        marcaFinal = '\x00'

        char = self.proxChar()

        while char != Lexer.marcaFinal:
            if char in Lexer.branco:
                leuDigito = 0
                # atualiza as coordenadas
                if char in Lexer.pulaLinha:
                    self.numLinha += 1
                    self.posLinha = 0   
                char = self.proxChar()

            ########### ID #######
            elif char in string.ascii_letters:
                    # leu um número seguido de uma letra -> erro léxico
                if leuDigito==1:
                    print ("Erro léxico na posição", self.numLinha+1, self.posLinha-1)
                    contErro+=1
                    leuDigito = 0
                else:
                    erroId = 0
                    stringId = char
                    char=self.proxChar()
                    while char in (string.ascii_letters + string.digits):
                            # excedeu o tamanho máximo
                        if len(stringId)==128:
                            print ("Erro léxico na posição", self.numLinha+1, self.posLinha-1)
                            erroId=1
                            contErro+=1
                            break
                        stringId+=char
                        char=self.proxChar()
                            # se não tem erro, cria o token
                    if not erroId:
                        if stringId.casefold() in Token.reservadas:
                            # verifica se é palavra
                            token = Token(Token.reservada, stringId.lower(), self.linhaAtual[self.numLinha], self.numLinha, self.posLinha)
                            token.tipo = stringId.lower()
                        # é identificador
                        else:
                            token = Token(Token.identificador, stringId, self.linhaAtual[self.numLinha], self.numLinha, self.posLinha)
                        self.tokens.append(token)

            ########## NUMERO ######
            elif char in string.digits:
                erroNum = 0
                leuDigito = 1
                stringNum = char
                char = self.proxChar()
                while char in string.digits:
                    # excedeu o tamanho máximo
                    if len(stringNum) == 128:
                        print ("Erro léxico na posição", self.numLinha+1, self.posLinha-1)
                        contErro+=1
                        erroNum=1
                        break
                    stringNum+=char
                    char=self.proxChar()

                if char in string.ascii_letters:
                    erroNum=1

                    # se não tem erro, cria o token
                if not erroNum:
                        token = Token(Token.numero, stringNum, self.linhaAtual[self.numLinha], self.numLinha,
                                          self.posLinha)
                        self.tokens.append(token)
                    
            ########## IGNORA COMENTÁRIOS 
            elif char == '#':
                char = self.proxChar()
                while char != Lexer.pulaLinha and char != marcaFinal:
                    char = self.proxChar()
           
            #### CARACTERE INVALIDO ########
            else:
                leuDigito = 0
                print ("Erro léxico na posição", self.numLinha+1, self.posLinha)
                contErro += 1
                char=self.proxChar()

        
        if contErro == 0:
            print ("Sem erros léxicos")
            token = Token('$', "$", self.linhaAtual[self.numLinha], self.numLinha,
                                          self.posLinha+1)
            self.tokens.append(token)
            # for token in self.tokens:
                # print(token)

        return self.tokens, contErro
