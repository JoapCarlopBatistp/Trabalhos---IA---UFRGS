from __future__ import annotations
from asyncio.windows_events import NULL
from typing import Iterable, Set, Tuple
from copy import deepcopy
from queue import PriorityQueue

class Coord:
    x = -1
    y = -1
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    estado = "12345678_"
    pai = NULL
    acao = NULL
    custo = -1
    children = set()

    def __init__(self, estado:str, pai:Nodo, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
    def __lt__(self, other):
        return self.estado < other.estado


objective = "12345678_"

def stringToSquare(estado:str):
    a = estado[0]
    b = estado[1]
    c = estado[2]
    d = estado[3]
    e = estado[4]
    f = estado[5]
    g = estado[6]
    h = estado[7]
    i = estado[8]
    square = [[a, b, c], [d, e, f], [g, h, i]]
    return square

def squareToString(square:list)->str:
    estado = ""
    for row in square:
        for char in row:
            estado += char
    return estado


def swap(square:list, a:Coord, b:Coord)->list:
    
    new_square = deepcopy(square)
    achar = square[a.y][a.x]
    bchar = square[b.y][b.x]
    new_square[a.y][a.x] = bchar
    new_square[b.y][b.x] = achar

    #possible inneficiency FIX
    return deepcopy(new_square)

    
def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    sucessores = set()
    square = stringToSquare(estado)
    coord = getBlankCoords(square)
    #print(estado)
    #print(square)
    x = coord.x
    y = coord.y
    
    #print(x)
    #print(y)
    if x != 0:
        #Can move left
        move = ("esquerda", squareToString(moveLeft(square, coord)))
        sucessores.add(move)
    if x != 2:
        #Can move right
        move = ("direita", squareToString(moveRight(square, coord)))
        sucessores.add(move)
    if y != 0:
        #Can move up
        move = ("acima", squareToString(moveUp(square, coord)))
        sucessores.add(move)
    if y != 2:
        #Can move down
        move = ("abaixo", squareToString(moveDown(square, coord)))
        sucessores.add(move)
    return sucessores

    
def moveLeft(square:list, a:Coord)->list:
    b = Coord(a.x - 1, a.y)
    new_square = swap(square, a, b)
    return new_square

def moveRight(square:list, a:Coord)->list:
    b = Coord(a.x + 1, a.y)
    new_square = swap(square, a, b)
    return new_square

def moveUp(square:list, a:Coord)->list:
    b = Coord(a.x, a.y - 1)
    new_square = swap(square, a, b)
    return new_square

def moveDown(square:list, a:Coord)->list:
    #print("move down")
    #print(square)
    b = Coord(a.x, a.y + 1)
    new_square = swap(square, a, b)

    #print(str(a.x) + str(a.y))
    #print(str(b.x) + str(b.y))
    #print(new_square)

    return new_square

def getBlankCoords(square:list)->Coord:
    for i in range(3):
        for j in range(3):
            if(square[j][i] == '_'):
                return Coord(i,j)
    



def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    children = set()
    estado = nodo.estado
    successors = sucessor(estado)
    for s in successors:
        move = s[0]
        next_state = s[1]
        child = Nodo(next_state, nodo, move, nodo.custo + 1)
        nodo.children.add(child)
        children.add(child)
    return children

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    iterations = 0

    initial = Nodo(estado, NULL, NULL, 0)

    explorados = set()
    fronteira = PriorityQueue()
    fronteira.put((0,initial))
    while(True):
        iterations += 1
        #if((iterations % 1000) == 0):
            #print("Size explorados")
            #print(len(explorados))
            #print("Size fronteira")
            #print(fronteira.qsize())
        if(fronteira.empty()):
            break
        v = getBest(fronteira) 
        #print(v.pathCost)
        if(isObjective(v)):
            return path(v)
        if(notExplored(v.estado, explorados)):
            explorados.add(v.estado)
            
            neighborns = expande(v)
            for neighborn in neighborns:
                if notExplored(neighborn.estado, explorados):
                    #print(type(neighborn))
                    fronteira.put((neighborn.custo + hamming_heuristic(neighborn), neighborn))
                    

def notExplored(estado:str, explorados:Set[str])->bool:


    return not estado in explorados

    for nodo in explorados:
        if(nodo.estado == estado):

            return False
    return True

def isObjective(nodo:Nodo)->bool:
    estado = nodo.estado

    return estado == objective

def getBest(queue:PriorityQueue)->Nodo:
    return queue.get()[1]

        
def path(nodo:Nodo)->str:
    node = nodo
    action_list = []

    while(node.pai != NULL):
        action_list.insert(0, node.acao)
        node = node.pai
    return action_list
    



   
   

def hamming_heuristic(nodo:Nodo)->int:
    estado = nodo.estado
    distance = 0
    for i in range(len(estado)):
        if((estado[i] != objective[i]) and (estado[i] != '_')):
            distance += 1

    return distance


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    iterations = 0

    initial = Nodo(estado, NULL, NULL, 0)

    explorados = set()
    fronteira = PriorityQueue()
    fronteira.put((0,initial))
    while(True):
        iterations += 1

        if(fronteira.empty()):
            break
        v = getBest(fronteira) 
        #print(v.pathCost)
        if(isObjective(v)):
            return path(v)
        if(notExplored(v.estado, explorados)):
            explorados.add(v.estado)
            
            neighborns = expande(v)
            for neighborn in neighborns:
                if notExplored(neighborn.estado, explorados):
                    #print(type(neighborn))
                    fronteira.put((neighborn.custo + manhattan_heuristic(neighborn), neighborn))

def manhattan_heuristic(nodo:Nodo)->int:
    distance = 0
    estado = nodo.estado
    square = stringToSquare(estado)

    for row in range(3):
        for col in range(3):
            distance += single_distance(square[row][col], row, col)
    return distance


def single_distance(piece:str, row:int, col:int)->int:

    targetCoord = find(piece, stringToSquare(objective))

    target_col = targetCoord.x
    target_row = targetCoord.y

    distance = abs(row - target_row) + abs(col - target_col)

    return distance

def find(piece:str, square:list)->Coord:

    for row in range(3):
        for col in range(3):
            if square[row][col] == piece:
                return Coord(col,row)

    return 
#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    initial = Nodo(estado, NULL, NULL, 0)

    explorados = set()
    fronteira = []
    fronteira.append(initial)
    while(True):
        
        if(len(fronteira) == 0):
            return None
        v = fronteira.pop(0)
        if(isObjective(v)):
            return path(v)
        if(notExplored(v.estado, explorados)):
            explorados.add(v.estado)
            
            neighborns = expande(v)
            for neighborn in neighborns:
                if notExplored(neighborn.estado, explorados):
                    #print(type(neighborn))
                    fronteira.append(neighborn)


#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    initial = Nodo(estado, NULL, NULL, 0)

    explorados = set()
    fronteira = []
    fronteira.append(initial)
    while(True):
        
        if(len(fronteira) == 0):
            return None
        v = fronteira.pop(-1)
        if(isObjective(v)):
            return path(v)
        if(notExplored(v.estado, explorados)):
            explorados.add(v.estado)
            
            neighborns = expande(v)
            for neighborn in neighborns:
                if notExplored(neighborn.estado, explorados):
                    #print(type(neighborn))
                    fronteira.append(neighborn)


#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#print("start")
#initial_State = "12_573486"#"1235764_8"
#print(astar_hamming(initial_State))
#print(astar_manhattan(initial_State))
#print(bfs(initial_State))
#print(dfs(initial_State))