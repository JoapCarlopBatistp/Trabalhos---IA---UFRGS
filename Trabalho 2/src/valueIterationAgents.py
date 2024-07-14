# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        prox = util.Counter()                                                   #Dict temporario para valores pré atualização da mdp
        for i in range(0, self.iterations):                                     #Para cada iteração
            for state in mdp.getStates():                                       #Para cada estado
                values = []                                                     #Dict de valores computados
                
                if self.mdp.isTerminal(state):                                  #Se está em estado terminal
                    values.append(0)                                            #Adiciona 0 no final do dict
                   
                for act in mdp.getPossibleActions(state):                       #Para cada ação
                    values.append(self.computeQValueFromValues(state, act))     #Dá append no valor computado na função computeQValueFromValues
                
                prox[state] = max(values)                                       #Prox do estado correspondente é substituido pelo maior valor presente no dict de valores

            self.values = prox.copy()                                           #Valor de prox é copiado em values


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        transAndProbs = self.mdp.getTransitionStatesAndProbs(state,action)       #Probabilidades de transição e estados de transição
        result = []                                                              #Dict para os valores da função de cálculo do Q valor
        
        for trans in transAndProbs:
            result.append(trans[1] * (self.mdp.getReward(state,action,trans[0]) + self.discount * self.values[trans[0]]))
                                     #Recompensa imediada + fator de desconto * valores 
        return sum(result)
        

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        possibleActions = self.mdp.getPossibleActions(state)
        next = None
        
        if possibleActions is False:                            #Caso o dict esteja vazio (i.e. nao existem ações posiveis)
            return next                                         #Retorna o valor de next (inicialmente == None)
        
        bestValue = float('-inf')                               #Inicializa o melhor valor como -infinito
        
        for act in possibleActions:                             #Para cada ação possivel no estado
            value = self.computeQValueFromValues(state,act)     #Encontra o valor da ação
            
            if value > bestValue:                               #Se esse valor for maior que o melhor valor já encontrado (inicia com -infinito)
                bestValue = value                               #Troca o melhor valor pelo atual
                next = act                                      #Troca a próxima ação para a atual
        
        return next                                             #Retorna a ação com melhor valor

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
