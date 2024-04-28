João Carlos Batista - 00343016 - Turma B
Ian dos Reis Nodari - XXXXXXXX - Turma A
Miguel Lemmertz Schwarzbold  - 00342191 - Turma A

REGRESSÃO LINEAR-------------------------------------------------------------------------------------------------
Utilizando os seguintes valores:
b = 1
w = 0.82
alpha = 0.01
num_interactions = 1000

Conseguimos chegar ao EQM = 8.530436476216975
A função depois das 1000 iterações retornou a reta --> 1.148441065455297 * x - 3.327198820480755

Utilizando a normalização por meio da fórmula de mean normalization, implementada na função "feature_scaling" no arquivo 
normalizacao.py, utilizando os mesmos b, w, alpha e num_interactions obtemos os seguintes dados:

EQM = 0.014802682822142161  (o que faz sentido, considerando que este tipo de normalização visa reduzir o erro quadrático médio)
Curva encontrada: 0.8264668737085059 * x + 1.6829673781979458 (o que não é tão distante do obtido sem normalização)

Ademais, ao que parece, ao realizar a operação de normalização dos dados, a operação de gradiente descendente precisou de menos
iterações para chegar em uma aproximação satisfatória da função

Para fazer os testes com e sem a normalização, colocamos a linha de código que normaliza os dados logo depois do carregamento
do .csv no arquivo .ipynb, para que possa ser comentada a fim de testar os dois casos.


TENSORFLOW------------------------------------------------------------------------------------------------------

Análise dos datasets:
  Cifar10
    - 10 classes
    - 60000 amostras (6000 por classe)
    - Imagens 32x32
    - 3 canais de cor (RGB)
  Cifar100
    - 100 classes (divididas em 20 superclasses)
    - 60000 amostras (600 por classe) 
    - Imagens 32x32
    - 3 canais de cor (RGB)
  MNIST
    - 10 classes
    - 60000 amostras (6000 por classe)
    - Imagens 28x28
    - 1 canal de cor
  Fashion MNIST
    Feito para ser uma versão mais complexa do MNIST mantendo exatamente os mesmos parametros de entradas, para reutilizar implementações.
    - 10 classes
    - 60000 amostras (6000 por classe)
    - Imagens 28x28
    - 1 canal de cor
    
Como o treino das redes estava a restrito a 10 épocas, redes menores, mais rapidamente treináveis sofreram desvantagens pela limitação estar em épocas e não em treino
A redução do tamanho das imagems com MaxPooling gera uma perda muito grande de informação, mas é necessário para garantir o treino em tempo adequado.
Devido à pequena quantidade de dados, especialmente no datacet cifar100, que contem somente 600 imagens de cada classe, cria situações frequentes de Overfitting.
Isso poderia ser remediado por técnicas de aumento de dados, como rotação e translação das imagens já obtidas.

//Parte do Ian
