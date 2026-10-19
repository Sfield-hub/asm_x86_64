global Function   ; 26 word without comments
section .text
Function:
    xor rax, rax  ; rax = 0
    test rdx, rdx ; rdx == 0?
    jz .done      ; if rdx == 0, jump to done

.loop:
    add rax, [rcx]
    add rcx, 8
    dec rdx
    jnz .loop

.done:
    ret
    