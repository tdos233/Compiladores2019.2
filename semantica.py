import tabela
from tabeladesimbolos import simbolo
from tabeladesimbolos import tabelaS
import sintatico

def analise_semantica(aux, aux2, aux3, aux4, regra, entrada, tabsim, countsemantico, sentido):

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

                elif entrada[0].valor == "repita":
                    print('aqui')


                    if sentido == 0 and tabsim.lookup(entrada[3].valor).vireParaInicio == 1:
                        print('Erro semântico na linha', entrada[3].numLinha+1, ': funcao com inicio vire para direita logo apos comando vire para esquerda')
                        countsemantico = 1
                    elif sentido == 1 and tabsim.lookup(entrada[3].valor).vireParaInicio == 0:
                        print('Erro semântico na linha', entrada[3].numLinha+1, ': funcao com inicio vire para esquerda logo apos comando vire para direita')
                        countsemantico = 1

            #verificar se o movimento esta no final de uma funcao e atualizar tabela-simbolo

                elif entrada[0].tipo == "fim":
                    if sentido == 1:
                        aux3 = 1;
                    elif sentido == 0:
                        aux3 = 0;
                        
                    

	    #verificar se instrução DECLARADA já foi declarada anteriormente

            elif regra[0] == "DECLARACAO":

                if tabsim.lookup(aux) is not None:
                    print('Erro semântico na linha', aux2 + 1,': instrução', aux, 'já declarada anteriormente')
                    countsemantico = 1
                simbolaux = simbolo(aux, aux2, aux3, aux4)
                tabsim.inserir(simbolaux)
                if aux3-aux4 != 0 and aux3 >= 0 and aux4 >= 0:
                    print('Warning: funcao', aux, 'comecando com vire para sentido e terminando com vire para sentido oposto, seu loop pode ocasionar movimentos inuteis')

	    #verificar se instrução CHAMADA já foi declarada anteriormente

            elif regra[0] == "INSTRUCAO" and regra[1] == "identificador":
                if tabsim.lookup(aux) is None:
                    print('Erro semântico na linha', aux2 + 1,': chamada para', aux, 'porém instrução não declarada')
                    countsemantico = 1

           #caso instrucao termine com movimento vire para sentido, verificar se apos chamada tem vire para outro sentido

                elif entrada[3].valor == "esquerda" and tabsim.lookup(aux).vireParaFinal == 1:
                    print('Erro semântico na linha', entrada[3].numLinha+1, ': vire para esquerda apos instrucao com final vire para direita')
                    countsemantico = 1
                elif entrada[3].valor == "direita" and tabsim.lookup(aux).vireParaFinal == 0:
                    print('Erro semântico na linha', entrada[3].numLinha+1, ': vire para direita apos instrucao com final vire para esquerda')
                    countsemantico = 1

            return sentido, countsemantico, aux3






