# -*- coding: utf-8 -*-
estados = input("").split()
simbalf = input("").split()
pilha_simbalf = input("").split()
qtdtrans = int(input())
afd = {}

for estado in estados:
    afd[estado] = {}

for i in range(0, qtdtrans):
    a, b, c, d, e = input("").split()
    if b not in afd[a]:
        afd[a][b] = []
    afd[a][b].append([c,d,e])

estado_inicial = input()
estado_f = input("").split()
palavras = input("").split()

estados_finais = {}
for k in estado_f:
    estados_finais[k] = 1

for palavra in palavras:
    pilha = []
    estados_atuais = [(estado_inicial, palavra, pilha)]
    aceitar = 0
    pilha_vazia = 1

    
    
    while aceitar == 0 and len(estados_atuais) > 0 and len(palavra) > 0: 
        t = estados_atuais.pop()
        t_estado = t[0] 
        t_palavra = t[1] 
        t_pilha = t[2] 

        if(afd[t_estado].get('*') and t_palavra != '*'): 
            estado_novo = afd[t_estado]['*'] 
            ok_um = 1
            for estado in estado_novo: 

                novo_t_pilha = t_pilha.copy() 

                if(estado[0] != '*'): 
                    if len(novo_t_pilha) == 0:
                        ok_um = 0
                        break
                    else:
                        top = novo_t_pilha.pop()
                        if top != estado[0]:
                            ok_um = 0
                            
                if(estado[2] != '*' and ok_um == 1):
                    for st in estado[2]:
                        novo_t_pilha.append(st)
                        pilha_vazia = 0
                
                if(ok_um == 1):
                    estados_atuais.append((estado[1], t_palavra, novo_t_pilha))

                ok_um = 1

        if len(t_palavra) == 0:
            if t_estado in estados_finais and len(t_pilha) == 0:
                aceitar = 1
                break
            else:
                continue
        
        novo_palavra = t_palavra[1:]

        if(afd[t_estado].get(t_palavra[0])):
            estado_novo = afd[t_estado][t_palavra[0]] 
            ok_um = 1
            for estado in estado_novo: 

                novo_t_pilha = t_pilha.copy() 

                if(estado[0] != '*'): 
                    if len(novo_t_pilha) == 0:
                        ok_um = 0
                        break
                    else:
                        top = novo_t_pilha.pop()
                        if top != estado[0]:
                            ok_um = 0
                            #break

                if(estado[2] != '*' and ok_um == 1): 
                    for st in estado[2]:
                        novo_t_pilha.append(st)
                        pilha_vazia = 0
                
                if(ok_um == 1): 
                    estados_atuais.append((estado[1], novo_palavra, novo_t_pilha))
                ok_one = 1

    if aceitar:
        print('S')
    else:
        print('N')
