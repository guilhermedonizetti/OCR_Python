#modulo para as FUNCOES internas do programa
import re

def buscar_cpf(texto):
    """Funcao para buscar CPF no texto que foi extraido.
    \nRetorna uma lista com os CPFs encontrados ou False se não existir.
    \nPara ser encontrado, o valor deve estar no formato xxx.xxx.xxx-xx.
    \nEx.:
    texto = texto extraido da imagem
    CPFs = buscar_cpf(texto)"""
    CPF = re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', texto)
    if len(CPF)>0:
        return CPF
    else:
        False


def buscar_data(texto):
    """Funcao para buscar datas no texto que foi extraido.
    \nRetorna uma lista com as datas encontradas ou False se não existir.
    \nPara ser encontrado, o valor deve estar no formato xx/xx/xxxx.
    \nEx.:
    texto = texto extraido da imagem
    Datas = buscar_data(texto)"""
    DATA = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', texto)
    if len(DATA)>0:
        return DATA
    else:
        False


def buscar_palavras_mas(texto):
    """Funcao para buscar palavras 'mas' (mau) no texto extraido.
    \nDespreza as palavras repetidas. Retorna um int, float.
    \nRespectivamente a quantidade de palavras mas encontradas e o percentual delas no texto todo.
    \nEx.:
    texto = texto extraido da imagem
    quantidade, percentual = buscar_palavras_mas(texto)"""
    cont_mau = 0
    palavras_mas = open("functions/palavras_mas.txt").read()
    palavras_mas = palavras_mas.split("\n")
    palavras_texto = set(re.split('[,;.?!/-: ]', texto))
    for i in palavras_texto:
        if i.upper() in palavras_mas:
            cont_mau += 1
    percentual = calcula_percentual(cont_mau, len(palavras_texto))

    return cont_mau, percentual


def buscar_palavras_boas(texto):
    """Funcao para buscar palavras de 'bem' no texto extraido.
    \nDespreza as palavras repetidas. Retorna um int, float.
    \nRespectivamente a quantidade de palavras boas encontradas e o percentual delas no texto todo.
    \nEx.:
    texto = texto extraido da imagem
    quantidade, percentual = buscar_palavras_boas(texto)"""
    cont_bem = 0
    palavras_boas = open("functions/palavras_boas.txt").read()
    palavras_boas = palavras_boas.split("\n")
    palavras_texto = set(re.split('[,;.?!/-: ]', texto))
    for i in palavras_texto:
        if i.upper() in palavras_boas:
            cont_bem += 1
    percentual = calcula_percentual(cont_bem, len(palavras_texto))

    return cont_bem, percentual


def calcula_percentual(quantidade, tamanho):
    """Funcao para calcular o percentual de palavras boas/mas.
    \nRetorna float, o percentual.
    \nEx.:
    quantidade = quantidade de palavras boas/mas
    tamanho = quantidade de palavras do texto
    percentual = calcula_percentual(quantidade, tamanho)"""
    percentual = (quantidade / tamanho) * 100
    return percentual


def sumarizar_cpf(cpf):
    """Funcao para deixar o CPF em string.
    \nRetorna string.
    \nEx.:
    cpf = lista de CPFs encontrados no texto
    CPF = sumarizar_cpf(cpf)"""
    CPF = ""
    for i in cpf:
        CPF += i+". "
    return CPF


def sumarizar_datas(datas):
    """Funcao para deixar a Data em string.
    \nRetorna string.
    \nEx.:
    datas = lista de datas encontradas no texto
    DATAS = sumarizar_datas(datas)"""
    DATA = ""
    for i in datas:
        DATA += i+". "
    return DATA