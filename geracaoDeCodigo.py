def gerarCodigo(pilha,regra,contIf,contElse,contWhile,contbusy):
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
            code='in al,10\ncmp al,7\nje label\n'
        else:
            code='in al,10\ncmp al,8\nje label\n'
    elif(regra[0]=='ESTADO'):
        if(regra[1]=='pronto'):
            code='in al,11\ntest al,00000000b\n'
        elif(regra[1]=='ocupado'):
            code='in al,11\ntest al,00000010b\n'
        elif(regra[1]=='parado'):
            code='in al,11\ntest al,00000001b\njnz label\ntest al,00000000b\n'
        else:
            code='in al,11\ntest al,00000001b\n'
    elif(regra[0]=='DIRECAO'):
        if(regra[1]=='frente'):
            code='frente'
        else:
            code=pilha[-1].code
    elif (regra[0]=='CONDICAO'):
        if(regra[1]=='robo ESTADO'):
            code=pilha[-1].code + 'jnz label'
        elif(regra[1]=='DIRECAO robo bloqueada'):
            if(pilha[-3].code=='frente'):
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 4\nout 9, al\nbusy-num+1: in al, 11\ntest al, 00000001b\njz busy-num+1\nin al, 10\ncmp al, 255\nje lable\ncmp al, 7\nje label\ncmp al, 8\nje label\n'
            elif(pilha[-3].code=='direita'):
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 3\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\nmov al, 4\nout 9, al\nbusy-num+2: in al, 11\ntest al, 00000001b\njz busy-num+2\nin al, 10\ncmp al, 255\nje lable\ncmp al, 7\nje label\ncmp al, 8\nje label\n'
            else:
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 2\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\nmov al, 4\nout 9, al\nbusy-num+2: in al, 11\ntest al, 00000001b\njz busy-num+2\nin al, 10\ncmp al, 255\nje lable\ncmp al, 7\nje label\ncmp al, 8\nje label\n'
        elif(regra[1]=='ESTADOLAMPADA a DIRECAO'):
            if(pilha[-1].code=='frente'):
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 4\nout 9, al\nbusy-num+1: in al, 11\ntest al, 00000001b\njz busy-num+1\n'+pilha[-3].code
            elif(pilha[-1].code=='direita'):
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 3\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\nmov al, 4\nout 9, al\nbusy-num+2: in al, 11\ntest al, 00000001b\njz busy-num+2\n'+pilha[-3].code
            else:
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 2\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\nmov al, 4\nout 9, al\nbusy-num+2: in al, 11\ntest al, 00000001b\njz busy-num+2\n'+pilha[-3].code
    elif (regra[0]=='INSTRUCAO'):
        if(regra[1]=='mova NUMPASSOS'):
            if(pilha[-1].code=='0'):
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 2\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'
            else:
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 1\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'*int(pilha[-1].code)
        elif(regra[1]=='vire para SENTIDO'):
            if(pilha[-1].code=='direita'):
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 3\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'
            else:
                code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 2\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'
        elif(regra[1]=='identificador'):
            code='call '+pilha[-1].valor+'\n'
        elif(regra[1]=='pare'):
            code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 0\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'
        elif (regra[1]=='finalize'):
            code='ret\n'
        elif(regra[1]=='apague lampada'):
            code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 6\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'
        elif(regra[1]=='acenda lampada'):
            code='busy-num: in al, 11\ntest al, 00000010b\njnz busy-num\nmov al, 5\nout 9,al\nbusy-num+1: in al, 11\ntest al, 00000010b\njnz busy-num+1\n'
        else:
            code='label: '+pilha[-1].code
    elif(regra[0]=='CONDICIONAL'):
        code=pilha[-5].code + pilha[-1].code + 'label: '+ pilha[-3].code +'labelfim:\n'
    elif(regra[0]=='CNDCNL'):
        if(regra[1]=='senao DECAUX fimsenao'):
            code='jump label\n'+ 'label:\n' + pilha[-2].code + 'jump finalCondicional\n'
        else:
            code='jump finalCondicional\n'
    elif(regra[0]=='ITERACAO'):
        code='mov cx, ' + pilha[-4].valor + '\nlabel: '+ pilha[-2].code +'loop label\n'
    elif(regra[0]=='LACO'):
        code='label: ' + pilha[-4].code + pilha[-2].code
    elif(regra[0]=='COMANDO'):
        code=pilha[-1].code
    elif(regra[0]=='BLOCO'):
        code=pilha[-2].code
        #print('bloco\n',code+'\n###########################\n')
    elif(regra[0]=='CMD'):
        if(regra[1]=='BLOCO'):
            code=pilha[-1].code
            print('cmd1\n',code)
        elif(regra[1]=='COMANDO CMD'):
            code=pilha[-2].code + pilha[-1].code
            #print('cmd2\n',code)
        elif(regra[1]==''):
            code=''
            #print('cmd3\n',code)
    elif(regra[0]=='DECAUX'):
        code=pilha[-1].code
        #print('DECAUX',code+'\n###########################\n',pilha[-1].tipo)
    elif(regra[0]=='DECLARACAO'):
        code=pilha[-3].valor + ' proc\n'+ pilha[-1].code  +'ret\n'+ pilha[-3].valor +' endp\n'
        #print('DECLARACAO',code+'\n###########################\n',pilha[-1].tipo)
    elif(regra[0]=='DEC'):
        if(regra[1]==''):
            code=''
            print('DEC1',code+'\n###########################\n',pilha[-1].tipo,pilha[-2].tipo)
        elif(regra[1]=='DECLARACAO DEC'):
            code=pilha[-2].code + pilha[-1].code
            print('DEC2',code+'\n###########################\n',pilha[-1].tipo,pilha[-2].tipo)
    elif(regra[0]=='PROGRAMA'):
        code=pilha[-3].code + pilha[-5].code + '\nret\n'
    return code


