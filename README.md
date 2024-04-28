# Trabalhos---IA---UFRGS
Três trabalhos da disciplina de Inteligência Artificial da universidade UFRGS

Integrantes:
João Carlos
Miguel Lemmertz Schwarzbold - 00342191
Ian


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
