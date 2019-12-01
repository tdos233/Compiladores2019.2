#start=robot.exe#
mov cx,50
busy:
loop busy
while0: mov al,1
out 9,al
mov cx,50
busy1:
loop busy1
mov al,0
out 9,al
mov cx,50
busy2:
loop busy2
mov al,1
out 9,al
mov cx,50
busy3:
loop busy3
mov al,0
out 9,al
mov cx,50
busy4:
loop busy4
mov cx,50
busy5:
loop busy5
aguarde0: in al,11
test al,00000010b
jnz aguarde0
mov al,3
out 9,al
mov cx,50
busy6:
loop busy6
mov al,0
out 9,al
mov cx,50
busy7:
loop busy7
mov al,4
out 9,al
busy8: in al, 11
test al, 00000001b
jz busy8
in al,10
cmp al,255
je if0
jmp if0fim
if0: mov al,0
out 9,al
mov cx,50
busy9:
loop busy9
if0fim:
mov al,1
out 9,al
mov cx,50
busy10:
loop busy10
mov al,0
out 9,al
mov cx,50
busy11:
loop busy11
mov cx,50
busy12:
loop busy12
aguarde1: in al,11
test al,00000010b
jnz aguarde1
mov al,4
out 9,al
busy0: in al, 11
test al, 00000001b
jz busy0
in al,10
cmp al,255
je while0
hlt
