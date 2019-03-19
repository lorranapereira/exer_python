#import datetime 

#def func(year,month,day,aux):
#    x = datetime.datetime(year,month,day)
#    if aux==1:
#        print(x.strftime('%Y')+','+x.strftime('%d')+' of '+x.strftime('%B'))
#    if aux==2:
#        print(x.strftime('%d')+'/'+x.strftime('%m')+'/'+x.strftime('%Y'))
#func(2000,9,8,1)
#func(2000,9,8,2)
#---------

#from datetime import datetime

#def func(nome,dt,vet):
#    dt = dt.split("/")
#    date = datetime(int(dt[2]),int(dt[1]),int(dt[0]))
#    vet = vet.split(';')
#    d = dict()
#    d = {"nome": nome, "dataNascimento":date, "telefone":vet } 
#    print(d["telefone"][0])

#nome = input("Dígite seu nome: ")
#dt = input("Dígite sua Data de aniversario no formato dia/mes/ano: ")
#vet = input("Dígite seu número de telefone, sem pontos ou traços. Caso tenha mais de um número, os separe com ;:  ")
#teste = func(nome,dt,vet)

#class Pessoa:
#    def __init__(self,nome):
#        self._nome = nome
#    def _get_nome(self):
#        return self._nome
#    def _set_nome(self, nome):
#        self._nome = nome
#    nome = property(_get_nome, _set_nome)

# p = Pessoa('Julio')
# print(p.nome)


#9) Em Python, para a geração de um número aleatório usamos o pacote random. Escreva um programa
#(jogo) que gere um número entre 0 e 1000 e peça para o usuário adivinhar o número. A cada tentativa o
#programa informa se o número informado pelo usuário é maior ou menor que o número a ser
#descoberto. Ao final o programa deve informar quantas tentativas foram feitas até a descoberta do
#número. 

import random 
number = random.randint(0, 1000)
def c(number):
    x = int(input("Qual é o número "))
    while x!=number:
        if x < number:
            print("O número é maior")
        if x > number:
            print("O número é menor")
        x = int(input("Qual é o número "))

    print("Você acertou o número é : "+str(number))        


#10) Faça uma função para cada situação:
#a) Gere a matriz transposta;
#b) Some duas matrizes;
#c) Faça a multiplicação de duas matrizes. 

def matriz_transposta(vet):
    cont=0
    vet2 = []
    for x in vet:
        vet2[0][1] = vet1[1][0]
        
        cont+=1

        print(cont)
matriz_transposta([[0,1,2],[3,4,5])
                  [0][3] - > [0,3]
                  [1][4]
                  [2][5]