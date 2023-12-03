lista=[]
numertask=0
xp=0
nivel=1

def add_tarefa():
    tarefa=input("Qual tarefa a ser adicionada?")
    listline=(str(numertask)+"-"+tarefa)
    lista.append(listline)

def removar_tarefa(xp):
    tarefa=input("Tarefa realizada?")  
    for exemplare in lista:
        numero=exemplare.split("-")[0]
        if numero==tarefa:
            indice=lista.index(exemplare)
            lista[indice]=("X"+"-"+exemplare.split("-")[1])
    xp=xp+10
    return xp
    
def subir_de_nivel(xp, nivel):
    if xp==100:
        nivel=nivel+1
        print("Parabéns, você alcançou o nível ", nivel)
        xp=0
    return xp, nivel


while True:
    
    for exemplare in lista:
        print(exemplare) 

    print("XP=",xp)
    action=input("Adicionar tarefa/Tarefa realizada:")

    if action=="adicionar tarefa":
        numertask=numertask+1
        add_tarefa()

    elif action=="tarefa realizada":
        xp=removar_tarefa(xp)
        xp, nivel=subir_de_nivel(xp,nivel)
    

    