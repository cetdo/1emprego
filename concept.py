from random import randint
## Caracterísicas
valors = ["Lealdade","Honestidade","Liderança","Conhecimento","Comunicação","Organização","Dedicação","Motivação","Auto-gerenciamento","Iniciativa"]
## ID das características
val_valors = [0,1,2,3,4,5,6,7,8,9]

## Classe de usuário
class User:
    val = []
    name = ''

    def __init__(self, n, v):
        self.name = n
        self.val = v

## Função que sorteia 3 valores e retorna-os em um vetor
def select_valors(valors):
    i = 0
    val = []

    while (i < 3): ## loop que termina quando 3 valors distintos forem selecionados
        v = valors[randint(0,9)] ## seleciona um valor aleatório
        if (v not in val): ## Caso a qualidade não esteja no vetor adiciona-a e soma i ao contador
            val.append(v)
            i += 1
    return val ## retorna os valores já sorteados

def create_users(qtd, valors): ## função pra criar quantidade X de usuários
    users = [] ## vetor vazio onde serão armazenadas as intâncias de usuarios
    for i in range(0, qtd): ## loop para criar os usuários
        v = select_valors(valors) ## chama a função que sorteia os valores
        users.append(User(i, v)) ## adiciona um usuário na lista
    return users ## retorna a lista de usuários estanciados

users = create_users(10, val_valors) ## variável que recebe a lista de usuários

## a parte a seguir do código serve para demostrar a comparação entre dois usuários

u1 = users[randint(0,9)] ## seleciona um usuário aleatório
u2 = users[randint(0,9)] ## seleciona um segundo usuário aleatório

print(u1.val, u2.val) ## mostra os valores dos dois
sim = len([i for i, j in zip(u1.val, u2.val) if i == j]) ## calcula quantos valores os dois tem na mesma posição

print(sim) ## imprime o resultado

## Sim é um a similaridade entre dois usuarios, quanto maior esse numero mais proximos sao os dois usuarios
## Assim podemos fazer a recomendação
## A ideia é que a vaga tenha também um vetor com os ids os valores assim como os usuarios e usando a logica desse código
## podemos fazer a combinação entre a vaga e o candidato, algo do gênero "ter duas das 3 caracteristicas necessarias"
## 