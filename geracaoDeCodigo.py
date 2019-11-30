def gerarCodigo(pilha,regra,contIf,contElse,contWhile,contbusy,contiter,contaguarde):
    code=''
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
            code='in al,11\ncmp al,00000000b\nje label\n'
        elif(regra[1]=='ocupado'):
            code='in al,11\ncmp al,00000010b\nje label\n'
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
                code='mov al, 4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 255\nje label\n'.replace('busy-num','busy'+str(contbusy))
                contbusy+=1
            elif(pilha[-3].code=='direita'):
                code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 15\nje label\n'.replace('busy-num','busy'+str(contbusy))
                contbusy+=1
            else:
                code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 240\nje label\n'.replace('busy-num','busy'+str(contbusy))
                contbusy+=1
        elif(regra[1]=='ESTADOLAMPADA a DIRECAO'):
            if(pilha[-3].code=='lampada acesa'):
                if(pilha[-1].code=='frente'):
                    code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 7\nje label\n'.replace('busy-num','busy'+str(contbusy))
                    contbusy+=1
                elif(pilha[-1].code=='direita'):
                    code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 11\nje label\n'.replace('busy-num','busy'+str(contbusy))
                    contbusy+=1
                else:
                    code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 9\nje label\n'.replace('busy-num','busy'+str(contbusy))
                    contbusy+=1
            else:
                if(pilha[-1].code=='frente'):
                    code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 8\nje label\n'.replace('busy-num','busy'+str(contbusy))
                    contbusy+=1
                elif(pilha[-1].code=='direita'):
                    code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 12\nje label\n'.replace('busy-num','busy'+str(contbusy))
                    contbusy+=1
                else:
                    code='mov al,4\nout 9, al\nbusy-num: in al, 11\ncmp al, 00000001b\nje busy-num\nin al, 10\ncmp al, 10\nje label\n'.replace('busy-num','busy'+str(contbusy))
                    contbusy+=1
    elif (regra[0]=='INSTRUCAO'):
        if(regra[1]=='mova NUMPASSOS'):
            if(pilha[-1].code=='0'):
                code='mov al, 1\nout 9,al\nmov al, 0\nout 9, al\n'
            else:
                for i in range(int(pilha[-1].code)):
                    code+='mov al, 1\nout 9,al\nmov al, 0\nout 9, al\n'
                    
        elif(regra[1]=='vire para SENTIDO'):
            if(pilha[-1].code=='direita'):
                code='mov al, 3\nout 9,al\nmov al, 0\nout 9, al\n'
            else:
                code='mov al, 2\nout 9,al\nmov al, 0\nout 9, al\n'
        elif(regra[1]=='identificador'):
            code='call '+pilha[-1].valor+'\n'
        elif(regra[1]=='pare'):
            code='mov al, 0\nout 9, al\n' 
        elif (regra[1]=='finalize'):
            code='hlt\n'
        elif(regra[1]=='apague lampada'):
            code='mov al, 6\nout 9,al\n'
        elif(regra[1]=='acenda lampada'):
            code='mov al, 5\nout 9,al\n'
        else:
            code='label: '+pilha[-1].code
            code=code.replace('label','aguarde'+str(contaguarde)).replace('je','jne')
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
        code='mov cx, ' + pilha[-4].valor + '\nlabel: '+ pilha[-2].code +'loop label\n'
        code=code.replace('label','iteracao'+str(contiter))
        contiter+=1
    elif(regra[0]=='LACO'):
        code='label: ' + pilha[-4].code + pilha[-2].code
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
        code='#start=robot.exe#\n'+pilha[-3].code +'hlt\n'+ pilha[-5].code
    return code,contIf,contElse,contWhile,contbusy,contiter,contaguarde


