#start=robot.exe#
mov cx, 3
iteracao0: call Trilha
loop iteracao0
busy14: in al, 11
test al, 00000010b
jnz busy14
mov al, 3
out 9,al
busy15: in al, 11
test al, 00000010b
jnz busy15
hlt
Trilha proc
busy0: in al, 11
test al, 00000010b
jnz busy0
mov al, 1
out 9,al
busy1: in al, 11
test al, 00000010b
jnz busy1
busy2: in al, 11
test al, 00000010b
jnz busy2
mov al, 1
out 9,al
busy3: in al, 11
test al, 00000010b
jnz busy3
busy4: in al, 11
test al, 00000010b
jnz busy4
mov al, 1
out 9,al
busy5: in al, 11
test al, 00000010b
jnz busy5
aguarde0: in al,11
test al,00000000b
jnz aguarde0
busy6: in al, 11
test al, 00000010b
jnz busy6
mov al, 2
out 9,al
busy7: in al, 11
test al, 00000010b
jnz busy7
busy8: in al, 11
test al, 00000010b
jnz busy8
mov al, 6
out 9,al
busy9: in al, 11
test al, 00000010b
jnz busy9
busy10: in al, 11
test al, 00000010b
jnz busy10
mov al, 3
out 9,al
busy11: in al, 11
test al, 00000010b
jnz busy11
busy12: in al, 11
test al, 00000010b
jnz busy12
mov al, 1
out 9,al
busy13: in al, 11
test al, 00000010b
jnz busy13
aguarde1: in al,11
test al,00000000b
jnz aguarde1
ret
Trilha endp
