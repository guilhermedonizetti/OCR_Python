#modulo para as FUNCOES internas do programa
import re

#A funcao busca CPF usando expressoes regulares e retorna a lista, ou False
def buscar_cpf(texto):
    CPF = re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', texto)
    if len(CPF)>0:
        return CPF
    else:
        False

#A funcao busca Datas usando expressoes regulares e retorna a lista, ou False
def buscar_data(texto):
    DATA = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', texto)
    if len(DATA)>0:
        return DATA
    else:
        False

#A funcao verifica quantas palavras 'mas' aparecem no texto
def buscar_palavras_mas(texto):
    cont_mau = 0
    palavras_mas = open("functions/palavras_mas.txt").read()
    palavras_mas = palavras_mas.split("\n")
    palavras_texto = set(re.split('[,;.?!/-: ]', texto))
    for i in palavras_texto:
        if i.upper() in palavras_mas:
            cont_mau += 1
    percentual = calcula_percentual(cont_mau, len(palavras_texto))

    return cont_mau, percentual

#A funcao verifica quantas palavras de 'bem' aparecem no texto
def buscar_palavras_boas(texto):
    cont_bem = 0
    palavras_boas = open("functions/palavras_boas.txt").read()
    palavras_boas = palavras_boas.split("\n")
    palavras_texto = set(re.split('[,;.?!/-: ]', texto))
    for i in palavras_texto:
        if i.upper() in palavras_boas:
            cont_bem += 1
    percentual = calcula_percentual(cont_bem, len(palavras_texto))

    return cont_bem, percentual

#A funcao retorna quantos porcento a quantidade de palavra (boa ou ma) representa
def calcula_percentual(quantidade, tamanho):
    percentual = (quantidade / tamanho) * 100
    return percentual

#A funcao remove o CPF da estrutura de lista e coloca em string
def sumarizar_cpf(cpf):
    CPF = ""
    for i in cpf:
        CPF += i+". "
    return CPF

#A funcao remove a Data da estrutura de lista e coloca em string
def sumarizar_datas(datas):
    DATA = ""
    for i in datas:
        DATA += i+". "
    return DATA