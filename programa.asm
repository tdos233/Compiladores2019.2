#start=robot.exe#
mov cx,50
busy:
loop busy
call Trilha
hlt
virar proc
mov al,3
out 9,al
mov cx,50
busy0:
loop busy0
mov al,0
out 9,al
mov cx,50
busy1:
loop busy1
ret
virar endp
Trilha proc
while0: mov al,1
out 9,al
mov cx,50
busy2:
loop busy2
mov al,0
out 9,al
mov cx,50
busy3:
loop busy3
mov cx,50
busy4:
loop busy4
aguarde0: in al,11
test al,00000010b
jnz aguarde0
mov al,4
out 9,al
busy5: in al, 11
test al, 00000001b
jz busy5
in al,10
cmp al,255
je if0
jmp if0fim
if0: call virar
if0fim:
mov al,4
out 9,al
busy6: in al, 11
test al, 00000001b
jz busy6
in al,10
cmp al,7
je if1
jmp if1fim
if1: mov al,3
out 9,al
mov cx,50
busy7:
loop busy7
mov al,0
out 9,al
mov cx,50
busy8:
loop busy8
if1fim:
in al,11
test al,00000010b
jz while0
ret
Trilha endp
