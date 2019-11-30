#start=robot.exe#
mov cx, 3
iteracao0: call Trilha
loop iteracao0
hlt
Trilha proc
mov al, 4
out 9, al
busy0: in al, 11
cmp al, 00000001b
jne busy0
in al, 10
cmp al, 255
je if0
jne else0
else0:
mov al, 3
out 9,al
mov al, 0
out 9, al
jmp if0fim
if0: mov al, 2
out 9,al
mov al, 0
out 9, al
if0fim:
ret
Trilha endp
