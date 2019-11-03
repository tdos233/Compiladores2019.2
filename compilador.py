import lexer
import string
import array
import sintatico

contaVazio = 0
entrada = []
vazias = []
while True:
    try:
        contaVazio+=1
        auxEntrada = input()
        if not auxEntrada.strip():
            vazias.append(contaVazio)
        entrada.append(auxEntrada)
    except (EOFError):
        break

marcaFinal = '\0'
pulaLinha = '\n'
x = pulaLinha.join(entrada)
entrada.append(marcaFinal)
print("ANÁLISE LÉXICA: ")
lexer = lexer.Lexer(x, vazias)
tokens = lexer.criaToken()
print("ANÁLISE SINTÁTICA: ")
sintatico.analise_sintatica(tokens)