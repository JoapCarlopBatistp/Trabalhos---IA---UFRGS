import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    x = data[:,0]                                                   #Primeira coluna do parâmetro "data" é separada (X)
    y = data[:,1]                                                   #Segunda coluna do parâmetro "data" é separada (Y)
    N = data.shape[0]                                               #Conta a quantidade de combinações (x, y) na matriz
    y_prediction = w*x + b                                          #Substitui X na função de regressão linear para encontrar o Y predito pela função
    mse = np.divide(np.sum((y - y_prediction)**2, axis=0), N)       #Calcula a função de loss (somatório dos quadrados das difetenças de y por y predito dividido pelo número de pares (x,y))
    
    return mse                                                      #Retorna o valor float de loss


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    x = data[:,0]                                                   #Primeira coluna do parâmetro "data" é separada (X)
    y = data[:,1]                                                   #Segunda coluna do parâmetro "data" é separada (Y)
    N = data.shape[0]                                               #Conta a quantidade de combinações (x, y) na matriz
    partial_derivative_b = 0.0                                      #Derivada parcial em relação a B inicializada em 0
    partial_derivative_w = 0.0                                      #Derivada parcial em relação a B inicializada em 0
    
    for i, j in zip(x,y):                                           #Itera por x e y sob os rótulos i e j
        partial_derivative_b += -2*(j - (w*i + b))                  #Calcula a derivada parcial em relação a b para todos os x's e y's 
        partial_derivative_w += -2*(j - (w*i + b))*i                #Calcula a derivada parcial em relação a w para todos os x's e y's
        
    partial_derivative_b = partial_derivative_b/(N)                 #Média das derivadas parciais em relação a b
    partial_derivative_w = partial_derivative_w/(N)                 #Média das derivadas parciais em relação a w      
    w = w - partial_derivative_w*alpha                              #Gradiente descendente (multiplicando a derivada parcial pela taxa de aprendizado alfa)
    b = b - partial_derivative_b*alpha                              #Gradiente descendente (multiplicando a derivada parcial pela taxa de aprendizado alfa)
    
    return w, b
    


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    list_b = [b]
    list_w = [w]
    
    for epoch in range(num_iterations):
        w, b = step_gradient(b, w, data, alpha)
        list_b.append(b)
        list_w.append(w)
        
    return list_b, list_w
