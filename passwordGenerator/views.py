from django.shortcuts import render
from django.http import HttpResponse
import random
import math

# Create your views here.

def home(request):
    return render(request, "passwordGenerator/home.html")

def geraSenha(request):
    length = int (request.GET.get('length'))
    if 5 < length < 16:
        criterios = ''
        characters = list('abcdefghijklmnopqrstuvwxyz')

        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            criterios = 'Letras Maiúsculas;'

        if request.GET.get('numbers'):
            characters.extend(list('1234567890'))
            criterios = criterios + 'Números; '

        if request.GET.get('special'):
            characters.extend(list('&*()$%#@!_-+={}][|\/?><,.:;'))
            criterios = criterios + 'Caracteres especiais; '

        senha= ''
        length = int (request.GET.get('length'))

            #length = str(length)

        for x in range(length):
            senha += random.choice(characters)

            #return render(request, "passwordGenerator/senha.html", {"characters":characters, "length":length, "senha":senha})
        return render(request, "passwordGenerator/senha.html", {"senha":senha, "criterios": criterios})
    else:
        return render(request,"passwordGenerator/tracker-pass.html")

def calculate(request):
    resultado = 0.0
    ops = request.GET.get('operation')
    operations = 'A operação solicitada foi: '

    if ops=='soma':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = numum + numdois
        operations = operations + str(numum) + '+' + str(numdois)
    if ops=='subtracao':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = numum - numdois
        operations = operations + str(numum) + '-' + str(numdois)
    if ops=='multiplicacao':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = numum * numdois
        operations = operations + str(numum) + 'x' + str(numdois)
    if ops=='divisao':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = numum / numdois
        operations = operations + str(numum) + '/' + str(numdois)
    if ops=='raiz':
        numum = int(request.GET.get('numum'))
        numum = float(numum)
        resultado = math.sqrt(numum)#corrigir aqui, o erro com base 10.
        operations = operations + 'raiz quadrada de: ' +str(numum)
    if ops=='percentual':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = (numum * numdois)/100
        operations = operations + str(numum) + '% de ' + str(numdois)
    if ops=='rest':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = math.fmod(numum, numdois)
        operations = 'o resto da divisão de ' + str(numum) + ' por ' + str(numdois)
    if ops=='gcd':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = math.gcd(numum, numdois)
        operations ='O menor divisor comum aos números' + str(numum) + ' e ' + str(numdois) + '.'
    if ops=='expoent':
        numum = int(request.GET.get('numum'))
        numdois = int(request.GET.get('numdois'))
        resultado = math.pow(numum, numdois)
        operations ='A elevação de ' + str(numum) + ' a ' + str(numdois) + ' potência.'
    if ops=='euler':
        numum = int(request.GET.get('numum'))
        resultado = math.exp(numum)
        operations ='A constante de euler elevado a ' + str(numum) + ' potência.'
    if ops=='euler-1':
        numum = int(request.GET.get('numum'))
        resultado = math.expm1(numum)
        operations ='A constante de euler elevado a ' + str(numum) + ' potência -1.'
    if ops=='logbe':
        numum = int(request.GET.get('numum'))
        resultado = math.log(numum)
        operations ='Log de ' + str(numum) + ' na base constante e.'
    if ops=='logx2':
        numum = int(request.GET.get('numum'))
        resultado = math.log2(numum)
        operations ='Log de ' + str(numum) + ' na base 2.'
    if ops=='logx10':
        numum = int(request.GET.get('numum'))
        resultado = math.log10(numum)
        operations ='Log de ' + str(numum) + ' na base 10.'
    if ops=='senx':
        numum = int(request.GET.get('numum'))
        resultado = math.sin(numum)
        operations ='Seno de ' + str(numum) + ' .'
    if ops=='cosx':
        numum = int(request.GET.get('numum'))
        resultado = math.cos(numum)
        operations ='Cosseno de ' + str(numum) + ' .'
    if ops=='tangx':
        numum = int(request.GET.get('numum'))
        resultado = math.tan(numum)
        operations ='Tangente de ' + str(numum) + ' .'
    if ops=='radx':
        numum = int(request.GET.get('numum'))
        resultado = math.degrees(numum)
        operations ='Converter ' + str(numum) + ' raios em graus.'
    if ops=='radd':
        numum = int(request.GET.get('numum'))
        resultado = math.radians(numum)
        operations ='Converter ' + str(numum) + 'graus em raio.'
    return render(request, "passwordGenerator/calculate.html", {'resultado':resultado, 'operations':operations})


def madeby(request):
    return render(request, "passwordGenerator/madeby.html")
