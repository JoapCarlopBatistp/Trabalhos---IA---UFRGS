from typing import Iterable, Set, Tuple
from queue import PriorityQueue

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
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


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    estados = []
    vazio = estado.find('_')
    novoEstado: str
    if vazio - 4 > 0:
        novoEstado = estado
        novoEstado = novoEstado[0:(vazio-4)] + novoEstado[vazio] + novoEstado[(vazio-4)+1:vazio] + novoEstado[vazio - 4] + novoEstado[vazio+1:]
        estados.append(tuple('abaixo',novoEstado))
    if vazio + 4 < 8:
        novoEstado = estado
        novoEstado = novoEstado[0:(vazio+4)] + novoEstado[vazio] + novoEstado[(vazio+4)+1:vazio] + novoEstado[vazio + 4] + novoEstado[vazio+1:]
        estados.append(tuple('acima',novoEstado))
    if (vazio != 0 and vazio != 3 and vazio != 6):
        novoEstado = estado
        novoEstado = novoEstado[0:(vazio-1)] + novoEstado[vazio] + novoEstado[(vazio-1)+1:vazio] + novoEstado[vazio - 1] + novoEstado[vazio+1:]
        estados.append(tuple('direita',novoEstado))
    if (vazio != 2 and vazio != 5 and vazio != 8):
        novoEstado = estado
        novoEstado = novoEstado[0:(vazio+1)] + novoEstado[vazio] + novoEstado[(vazio+1)+1:vazio] + novoEstado[vazio + 1] + novoEstado[vazio+1:]
        estados.append(tuple('esquerda',novoEstado))
        
    return estados


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    nodos = []
    custo = Nodo.custo + 1
    estados = sucessor(Nodo.estado)
    for iteration in estados:
        acoesEestados = estados[iteration]
        nodos.append(Nodo(acoesEestados[1], Nodo, acoesEestados[0], custo))
    return nodos


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
    NodosVisitados = []
    filaDePrioridade = PriorityQueue()
    filaDePrioridade.put(0, estado)
    while filaDePrioridade:
        if filaDePrioridade == None:
            return None
        v = filaDePrioridade.get()
        if v == "12345678_":
            return (None)#mudar daqui a pouco
        if v not in NodosVisitados:
            NodosVisitados.append(v)
            filaDePrioridade.put()
    
    raise NotImplementedError


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
    raise NotImplementedError

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
    raise NotImplementedError

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
    raise NotImplementedError

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
