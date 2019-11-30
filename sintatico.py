# -*- Coding: UTF-8 -*-
#coding: utf-8

import tabela
import geracaoDeCodigo as gdc
class state(object):
    def __init__(self,tipo,estado,valor):
        self.tipo=tipo
        self.state=estado
        self.code=''
        self.valor=valor

from tabeladesimbolos import simbolo
from tabeladesimbolos import tabelaS
import semantica
        
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
ITERACAO->repita numero vezes DECAUX fimrepita
LACO->enquanto CONDICAO faca DECAUX fimpara
CONDICIONAL->se CONDICAO entao DECAUX fimse CNDCNL
CNDCNL->senao DECAUX fimsenao
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
    func = ''
    aux3 = -1
    aux4 = -1
    contif=0
    contwhile=0
    contelse=0
    contbusy=0
    contiter=0
    contaguarde=0
    countsemantico = 0
    sentido = 0
    aux=''
    aux2=''
    tabsim = tabelaS()
    pilha=[state('',0,'')]
    tabela_sintatica=tabela.tabela
    entrada=tokens
    while len(entrada)!=0:
        actions=tabela_sintatica[pilha[len(pilha)-1].state][entrada[0].tipo]
        
        # print(actions,pilha[len(pilha)-1].state)
        if 's' in actions:

            pilha.append(state(entrada[0].tipo,int(actions.split('s')[1]),entrada[0].valor))
            #print(pilha[-1].tipo,pilha[-1].code,entrada[0].valor)
            #codigo para auxiliar na análise semântica. pegar os valores do token do identificador

                

            if entrada[0].valor == 'definainstrucao':
                aux = entrada[1].valor
                aux2 = entrada[1].numLinha
                aux3 = -1
                if entrada[6].valor == 'direita':
                    aux4 = 1
                elif entrada[6].valor == 'esquerda':
                    aux4 = 0
                else:
                    aux4 = -1;

            
                
                

            entrada=entrada[1:]

            
            
        elif 'r' in actions:
            regra=gramatica[int(actions.split('r')[1])].split('->')
            code,contif,contelse,contwhile,contbusy,contiter,contaguarde=gdc.gerarCodigo(pilha,regra,contif,contelse,contwhile,contbusy,contiter,contaguarde)

            #ANÁLISE SEMÂNTICA
            sentido, countsemantico, aux3 = semantica.analise_semantica(aux, aux2, aux3, aux4, regra, entrada, tabsim, countsemantico, sentido)
            if regra[1]!= "''":
                for i in range(len(regra[1].split(' '))):
                    pilha.pop()
                                    
                stat=int(tabela_sintatica[pilha[len(pilha)-1].state][regra[0]])
                st=state(regra[0],stat,'-')
                st.code=code
                pilha.append(st)
                #print(pilha[-1].tipo,pilha[-1].code,entrada[0].valor)
            else :
                stat=int(tabela_sintatica[pilha[len(pilha)-1].state][regra[0]])
                st=state(regra[0],stat,'-')
                st.code=code
                pilha.append(st)
                #print(pilha[-1].tipo,pilha[-1].code,entrada[0].valor)
                   
        elif 'acc' == actions:
            print('Sem erros sintáticos')
            if countsemantico == 0:
                print('Sem erros semânticos\n')
                open('programa.asm','w').write(code)
            entrada=entrada[1:]
        else :
            print('Erro sintático na linha: ',entrada[0].numLinha+1)
            break


