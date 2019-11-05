import tabela
from tabeladesimbolos import simbolo
from tabeladesimbolos import tabelaS
import sintatico

def analise_semantica(aux, aux2, regra, entrada, tabsim, countsemantico, sentido):

	    #salvar sempre o ultimo valor de sentido

            if regra[1] == "direita":
                sentido = 1
            elif regra[1] == "esquerda":
                sentido = 0

            #verificar se um 'mova n passos' é precedido de 'aguarde até pronto'

            elif regra[0] == "NUMPASSOS" and not (entrada[0].tipo == "aguarde" and entrada[1].tipo == "ate" and entrada[2].valor == "robo" and entrada[3].valor == "pronto"):
                print('Erro na linha', entrada[0].numLinha, 'instrucao [mova n passos] necessita ser precedida de [aguarde ate robo pronto]')
                countsemantico = 1
            #verificar se existe movimento para dois sentidos opostos consecutivos

            elif regra[0] == "INSTRUCAO" and regra[1] == "vire para SENTIDO":
                if entrada[0].tipo == "vire":
                    if sentido == 0 and entrada[2].valor == "direita":
                        countsemantico = 1
                        print('Erro semântico nas linhas', entrada[2].numLinha, 'e', entrada[2].numLinha+1, ': comando [vire para direita] logo após [vire para esquerda]')
                    elif sentido == 1 and entrada[2].valor == "esquerda":
                        countsemantico = 1
                        print('Erro semântico nas linhas', entrada[2].numLinha, 'e', entrada[2].numLinha+1, ': comando [vire para esquerda] logo após [vire para direita]')

	    #verificar se instrução DECLARADA já foi declarada anteriormente

            elif regra[0] == "DECLARACAO":

                if tabsim.lookup(aux) is not None:
                    print('Erro semântico na linha', aux2 + 1,': instrução', aux, 'já declarada anteriormente')
                    countsemantico = 1
                simbolaux = simbolo(aux, aux2)
                tabsim.inserir(simbolaux)

	    #verificar se instrução CHAMADA já foi declarada anteriormente

            elif regra[0] == "INSTRUCAO" and regra[1] == "identificador":
                if tabsim.lookup(aux) is None:
                    print('Erro semântico na linha', aux2 + 1,': chamada para', aux, 'porém instrução não declarada')
                    countsemantico = 1
            return sentido, countsemantico

