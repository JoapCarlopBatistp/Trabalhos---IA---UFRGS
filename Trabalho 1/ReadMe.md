João Carlos Batista - 00343016 - Turma B
Ian dos Reis Nodari - XXXXXXXX - Turma A

REGRESSÃO LINEAR-------------------------------------------------------------------------------------------------
Utilizando os seguintes valores:
b = -3
w = 1
alpha = 0.01
num_interactions = 1000

Conseguimos chegar ao EQM = 8.527737655723762
A função depois das 1000 iterações retornou a reta --> 1.1593592447726748 * x - 3.4372683407829783

Utilizando a normalização por meio da fórmula de mean normalization, implementada na função "feature_scaling" no arquivo 
normalizacao.py, utilizando os mesmos b, w, alpha e num_interactions obtemos os seguintes dados:

EQM = 0.014992103975467614  (o que faz sentido, considerando que este tipo de normalização visa reduzir o erro quadrático médio)
Curva encontrada: 0.890946459465156 * x - 5.0489020470416006 (o que não é tão distante do obtido sem normalização)

Ademais, ao que parece, ao realizar a operação de normalização dos dados, a operação de gradiente descendente precisou de menos
iterações para chegar em uma aproximação satisfatória da função

Para fazer os testes com e sem a normalização, colocamos a linha de código que normaliza os dados separada no arquivo .ipynb, para que possa ser comentada a fim de testar os dois casos


TENSORFLOW------------------------------------------------------------------------------------------------------

//Parte do Ian