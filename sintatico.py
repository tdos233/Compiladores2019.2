from bs4 import BeautifulSoup
import tabela
class state(object):
    def __init__(self,tipo,estado):
        self.tipo=tipo
        self.state=estado
        
gramatica="""START->PROGRAMA
PROGRAMA->programainicio DEC execucaoinicio CMD fimexecucao fimprograma
DEC->DECLARACAO DEC
DEC->''
DECLARACAO->definainstrucao identificador como DECAUX
DECAUX->COMANDO
DECAUX->BLOCO
BLOCO->inicio CMD fim
CMD->BLOCO
CMD->COMANDO CMD
CMD->''
COMANDO->ITERACAO
COMANDO->INSTRUCAO
COMANDO->LACO
COMANDO->CONDICIONAL
ITERACAO->repita numero vezes COMANDO fimrepita
LACO->enquanto CONDICAO faca COMANDO fimpara
CONDICIONAL->se CONDICAO entao COMANDO fimse CNDCNL
CNDCNL->senao COMANDO fimsenao
CNDCNL->''
INSTRUCAO->mova NUMPASSOS
INSTRUCAO->vire para SENTIDO
INSTRUCAO->identificador
INSTRUCAO->pare
INSTRUCAO->finalize
INSTRUCAO->apague lampada
INSTRUCAO->acenda lampada
INSTRUCAO->aguarde ate CONDICAO
CONDICAO->robo ESTADO
CONDICAO->DIRECAO robo bloqueada
CONDICAO->ESTADOLAMPADA a DIRECAO
ESTADO->pronto
ESTADO->ocupado
ESTADO->parado
ESTADO->movimentando
DIRECAO->frente
DIRECAO->SENTIDO
ESTADOLAMPADA->lampada acesa	
ESTADOLAMPADA->lampada apagada	
NUMPASSOS->numero passos
NUMPASSOS->''
SENTIDO->direita
SENTIDO->esquerda""".split('\n')



def analise_sintatica(tokens):
    pilha=[state('',0)]
    tabela_sintatica=tabela.tabela
    tokens+=' $'
    entrada=tokens.split(' ')
    while len(entrada)!=0:
        actions=tabela_sintatica[pilha[len(pilha)-1].state][entrada[0]]
        # print(actions,pilha[len(pilha)-1].state,entrada)
        if 's' in actions:
            pilha.append(state(entrada[0],int(actions.split('s')[1])))
            entrada=entrada[1:]
        elif 'r' in actions:
            regra=gramatica[int(actions.split('r')[1])].split('->')
            #print(regra,len(regra[1].split(' ')),regra[1])
            if regra[1]!= "''":
                for i in range(len(regra[1].split(' '))):
                    pilha.pop()
                stat=int(tabela_sintatica[pilha[len(pilha)-1].state][regra[0]])
                pilha.append(state(regra[0],stat))
            else :
                stat=int(tabela_sintatica[pilha[len(pilha)-1].state][regra[0]])
                pilha.append(state(regra[0],stat))
                   
        elif 'acc' == actions:
            entrada=entrada[1:]
            print('ANÁLISE SINTÁTICA:')
            print('SEM ERROS SINTÁTICOS')
        else :
            print('ANÁLISE SINTÁTICA:')
            print('PROGRAMA CONTÉM ERROS SINTÁTICOS')
            break
        
        

# e=''
# tokens = ["programainicio", "definainstrucao", "identificador"]
# str1 = ' '.join(str(e) for e in tokens)
    

# analise_sintatica("""programainicio definainstrucao identificador como inicio mova numero passos se robo pronto entao mova fimse senao mova fimsenao aguarde ate robo pronto vire para esquerda apague lampada se robo parado entao vire para esquerda fimse repita numero vezes identificador fimrepita enquanto robo parado faca mova numero passos fimpara vire para direita mova numero passos aguarde ate robo pronto apague lampada fim execucaoinicio vire para direita fimexecucao fimprograma""")
# analise_sintatica(str1)