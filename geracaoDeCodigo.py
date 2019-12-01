def gerarCodigo(pilha,regra,contIf,contElse,contWhile,contbusy,contiter,contaguarde):
    code=''
    delay='mov cx,50\nbusy:\nloop busy\n'
    moverFrente='mov al,1\nout 9,al\nmov cx,50\nbusy:\nloop busy\n'
    moverDireita='mov al,3\nout 9,al\nmov cx,50\nbusy:\nloop busy\n'
    moverEsquerda='mov al,2\nout 9,al\nmov cx,50\nbusy:\nloop busy\n'
    pare='mov al,0\nout 9,al\nmov cx,50\nbusy:\nloop busy\n'
    examine='mov al,4\nout 9,al\nbusy: in al, 11\ntest al, 00000001b\njz busy\nin al,10\n'
    bloqueio='cmp al,255\nje label\n'
    lampadaAcesa='cmp al,7\nje label\n'
    lampadaApaguada='cmp al,8\nje label\n'
    acendalampada='mov al,5\nout 9,al\nmov cx,50\nbusy:\nloop busy\n'
    apaguelampada='mov al,6\nout 9,al\nmov cx,50\nbusy:\nloop busy\n'
    if (regra[0]=='SENTIDO'):
        code=pilha[-1].tipo
    elif(regra[0]=='NUMPASSOS'):
        if (regra[1]=='numero passos'):
            code=pilha[-2].valor
        else:
            code='0'
    elif(regra[0]=='ESTADOLAMPADA'):
        if(regra[1]=='lampada acesa'):
            code='lampada acesa'
        else:
            code='lampada apagada'
    elif(regra[0]=='ESTADO'):
        if(regra[1]=='pronto'):
            code='in al,11\ntest al,00000010b\njz label\n'
        elif(regra[1]=='ocupado'):
            code='in al,11\ntest al,00000010b\njnz label\n'
        elif(regra[1]=='parado'):
            code='in al,9\ncmp al,0\nje label\n'
        else:
            code='in al,9\ncmp al,0\njne label\n'
    elif(regra[0]=='DIRECAO'):
        if(regra[1]=='frente'):
            code='frente'
        else:
            code=pilha[-1].code
    elif (regra[0]=='CONDICAO'):
        if(regra[1]=='robo ESTADO'):
            code=pilha[-1].code
        elif(regra[1]=='DIRECAO robo bloqueada'):
            if(pilha[-3].code=='frente'):
                code=examine.replace('busy','busy'+str(contbusy))+bloqueio
                contbusy+=1
            elif(pilha[-3].code=='direita'):
                code=moverDireita.replace('busy','busy'+str(contbusy))+examine.replace('busy','busy'+str(contbusy+1))+bloqueio+moverEsquerda.replace('busy','busy'+str(contbusy+2))+pare.replace('busy','busy'+str(contbusy+3))
                contbusy+=4
            else:
                code=moverEsquerda.replace('busy','busy'+str(contbusy))+examine.replace('busy','busy'+str(contbusy+1))+bloqueio+moverDireita.replace('busy','busy'+str(contbusy+2))+pare.replace('busy','busy'+str(contbusy+3))
                contbusy+=4
        elif(regra[1]=='ESTADOLAMPADA a DIRECAO'):
            if(pilha[-3].code=='lampada acesa'):
                if(pilha[-1].code=='frente'):
                    code=examine.replace('busy','busy'+str(contbusy))+lampadaAcesa
                    contbusy+=1
                elif(pilha[-1].code=='direita'):
                    code=moverDireita.replace('busy','busy'+str(contbusy))+examine.replace('busy','busy'+str(contbusy+1))+lampadaAcesa+moverEsquerda.replace('busy','busy'+str(contbusy+2))+pare.replace('busy','busy'+str(contbusy+3))
                    contbusy+=4
                else:
                    code=moverEsquerda.replace('busy','busy'+str(contbusy))+examine.replace('busy','busy'+str(contbusy+1))+lampadaAcesa+moverDireita.replace('busy','busy'+str(contbusy+2))+pare.replace('busy','busy'+str(contbusy+3))
                    contbusy+=4
            else:
                if(pilha[-1].code=='frente'):
                    code=examine.replace('busy','busy'+str(contbusy))+lampadaApaguada
                    contbusy+=1
                elif(pilha[-1].code=='direita'):
                    code=moverDireita.replace('busy','busy'+str(contbusy))+examine.replace('busy','busy'+str(contbusy+1))+lampadaApaguada+moverEsquerda.replace('busy','busy'+str(contbusy+2))+pare.replace('busy','busy'+str(contbusy+3))
                    contbusy+=4
                else:
                    code=moverEsquerda.replace('busy','busy'+str(contbusy))+examine.replace('busy','busy'+str(contbusy+1))+lampadaApaguada+moverDireita.replace('busy','busy'+str(contbusy+2))+pare.replace('busy','busy'+str(contbusy+3))
                    contbusy+=4
    elif (regra[0]=='INSTRUCAO'):
        if(regra[1]=='mova NUMPASSOS'):
            if(pilha[-1].code=='0'):
                code=moverFrente.replace('busy','busy'+str(contbusy))+pare.replace('busy','busy'+str(contbusy+1))
                contbusy+=2
            else:
                for i in range(int(pilha[-1].code)):
                    code+=moverFrente.replace('busy','busy'+str(contbusy))+pare.replace('busy','busy'+str(contbusy+1))
                    contbusy+=2
                    
        elif(regra[1]=='vire para SENTIDO'):
            if(pilha[-1].code=='direita'):
                code=moverDireita.replace('busy','busy'+str(contbusy))+pare.replace('busy','busy'+str(contbusy+1))
                contbusy+=2
            else:
                code=moverEsquerda.replace('busy','busy'+str(contbusy))+pare.replace('busy','busy'+str(contbusy+1))
                contbusy+=2
        elif(regra[1]=='identificador'):
            code='call '+pilha[-1].valor+'\n'
        elif(regra[1]=='pare'):
            code=pare.replace('busy','busy'+str(contbusy))
            contbusy+=1
        elif (regra[1]=='finalize'):
            code='hlt\n'
        elif(regra[1]=='apague lampada'):
            code=apaguelampada.replace('busy','busy'+str(contbusy))+pare.replace('busy','busy'+str(contbusy+1))
            contbusy+=2
        elif(regra[1]=='acenda lampada'):
            code=acendalampada.replace('busy','busy'+str(contbusy))+pare.replace('busy','busy'+str(contbusy+1))
            contbusy+=2
        else:
            code='label: '+pilha[-1].code
            code=delay.replace('busy','busy'+str(contbusy))+code.replace('label','aguarde'+str(contaguarde)).replace('jz','jnz')
            contbusy+=1
            contaguarde+=1
    elif(regra[0]=='CONDICIONAL'):
        code=pilha[-5].code + pilha[-1].code + 'label: '+ pilha[-3].code +'labelfim:\n'
        code=code.replace('label','if'+str(contIf))
        contIf+=1
    elif(regra[0]=='CNDCNL'):
        if(regra[1]=='senao DECAUX fimsenao'):
            code='jne label\n'+ 'label:\n' + pilha[-2].code + 'jmp finalCondicional\n'
            code=code.replace('label','else'+str(contElse)).replace('finalCondicional','if'+str(contIf)+'fim')
            contElse+=1
        else:
            code='jmp finalCondicional\n'.replace('finalCondicional','if'+str(contIf)+'fim')
            contElse+=1
    elif(regra[0]=='ITERACAO'):
        code='mov cx, ' + pilha[-4].valor + '\nlabel: push cx\n'+ pilha[-2].code +'pop cx\nloop label\n'
        code=code.replace('label','iteracao'+str(contiter))
        contiter+=1
    elif(regra[0]=='LACO'):
        code='label: ' + pilha[-2].code+pilha[-4].code 
        code=code.replace('label','while'+str(contWhile))
        contWhile+=1
    elif(regra[0]=='COMANDO'):
        code=pilha[-1].code
    elif(regra[0]=='BLOCO'):
        code=pilha[-2].code
    elif(regra[0]=='CMD'):
        if(regra[1]=='BLOCO'):
            code=pilha[-1].code
        elif(regra[1]=='COMANDO CMD'):
            code=pilha[-2].code + pilha[-1].code
        elif(regra[1]==''):
            code=''
    elif(regra[0]=='DECAUX'):
        code=pilha[-1].code
    elif(regra[0]=='DECLARACAO'):
        code=pilha[-3].valor + ' proc\n'+ pilha[-1].code  +'ret\n'+ pilha[-3].valor +' endp\n'
    elif(regra[0]=='DEC'):
        if(regra[1]==''):
            code=''
        elif(regra[1]=='DECLARACAO DEC'):
            code=pilha[-2].code + pilha[-1].code
    elif(regra[0]=='PROGRAMA'):
        code='#start=robot.exe#\n'+delay+pilha[-3].code +'hlt\n'+ pilha[-5].code
    return code,contIf,contElse,contWhile,contbusy,contiter,contaguarde


