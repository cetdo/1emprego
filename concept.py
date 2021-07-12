from random import randint

valors = ["Lealdade","Honestidade","Liderança","Conhecimento","Comunicação","Organização","Dedicação","Motivação","Auto-gerenciamento","Iniciativa"]
val_valors = [0,1,2,3,4,5,6,7,8,9]
class User:
    val = []
    name = ''

    def __init__(self, n, v):
        self.name = n
        self.val = v


def select_valors(valors):
    i = 0
    val = []

    while (i < 3):
        v = valors[randint(0,9)]
        if (v not in val):
            val.append(v)
            i += 1
    return val

def create_users(qtd, valors):
    users = []
    for i in range(0, qtd):
        v = select_valors(valors)
        users.append(User(i, v))
    return users

users = create_users(10, val_valors)

u1 = users[randint(0,9)]
u2 = users[randint(0,9)]

print(u1.val, u2.val)
sim = len([i for i, j in zip(u1.val, u2.val) if i == j])

print(sim)

## Sim é um a similaridade entre dois usuarios, quanto maior esse numero mais proximos sao os dois usuarios
## Assim podemos fazer a recomendação