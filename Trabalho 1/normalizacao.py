import numpy as np

def feature_scaling(data):
    """
    Retorna os dados de "data" normalizados
    Utilizando "mean normalization":
    X' = (x - x_medio)/(x_maximo - x_minimo)
    """
    
    x = data[:,0]                                                         #Primeira coluna do parâmetro "data" é separada (X)
    y = data[:,1]                                                         #Segunda coluna do parâmetro "data" é separada (Y)
    size = data.shape[0]                                                  #Conta o tamanho de x e y
    
    x_max = np.max(x)                                                     #Valor máximo do banco de x
    y_max = np.max(y)                                                     #Valor máximo do banco de y
    
    x_min = np.min(x)                                                     #Valor mínimo do banco de x
    y_min = np.min(y)                                                     #Valor mínimo do banco de y
    
    x_gap = x_max - x_min                                                 #Calcula a diferença x_max - x_min
    y_gap = y_max - y_min                                                 #Calcula a diferença y_max - y_min
    
    x_average = np.divide(np.sum(x, axis=0), size)                        #Calcula o valor médio da coluna de x
    y_average = np.divide(np.sum(y, axis=0), size)                        #Calcula o valor médio da coluna de y
    
    data[:,0] = np.divide(x - x_average, x_gap)                           #Implementa a função de mean normalization para x
    data[:,1] = np.divide(y - y_average, y_gap)                           #Implementa a função de mean normalization para y
    
    return data                                                           #Retorna os dados normalizados
