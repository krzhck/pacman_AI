from game import Directions
import random, util

from game import Agent

#######################################################
#            This portion is written for you          #
#######################################################

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        we assume ghosts act in turn after the pacman takes an action
        so your minimax tree will have multiple min layers (one for each ghost)
        for every max layer

        gameState.generateChild(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state

        self.evaluationFunction(state)
        Returns pacman SCORE in current state (useful to evaluate leaf nodes)

        self.depth
        limits your minimax tree depth (note that depth increases one means
        the pacman and all ghosts has already decide their actions)
        """
        def miniMax(self, gameState, level=1, agent_index=0):
            if level > self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            agent_num = gameState.getNumAgents()
            if agent_index==0: #max
                vmax = -float('inf')
                for action in gameState.getLegalActions(agent_index):
                    v = miniMax(self, gameState.generateChild(agent_index,action), level, agent_index + 1)
                    v = max(v, vmax)
                return v
            else: #min
                vmin = float('inf')
                if agent_index == agent_num - 1:
                    level += 1
                for action in gameState.getLegalActions(agent_index):
                    v = miniMax(self, gameState.generateChild(agent_index,action), level, (agent_index + 1) % agent_num)
                    v = min(v, vmin)
                return v
       
        pacman_actions = gameState.getLegalPacmanActions()
        valid_actions = []
        vmax = -float('inf')
        for action in pacman_actions:
            next_state=gameState.generatePacmanChild(action)
            v = miniMax(self, next_state, 1, 1)
            if v > vmax:
                vmax = v
                valid_actions = [action]
            elif v == vmax:
                valid_actions.append(action)
                continue
        return valid_actions[random.randint(0,len(valid_actions)-1)]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def miniMax(self, gameState, level=1, agent_index=0, alpha = -float('inf'), beta = float('inf')):
            if level > self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            agent_num = gameState.getNumAgents()
            if agent_index==0: #max
                vmax = -float('inf')
                for action in gameState.getLegalActions(agent_index):
                    if alpha > beta: break
                    v = miniMax(self, gameState.generateChild(agent_index,action), level, agent_index + 1, alpha, beta)
                    v = max(v, vmax)
                    alpha = max(alpha, v)
                return v
            else: #min
                vmin = float('inf')
                if agent_index == agent_num - 1:
                    level += 1
                for action in gameState.getLegalActions(agent_index):
                    if alpha > beta: break
                    v = miniMax(self, gameState.generateChild(agent_index,action), level, (agent_index + 1) % agent_num, alpha, beta)
                    v = min(v, vmin)
                    beta = min(beta, v)
                return v
       
        pacman_actions = gameState.getLegalPacmanActions()
        valid_actions = []
        vmax = -float('inf')
        for action in pacman_actions:
            next_state=gameState.generatePacmanChild(action)
            v = miniMax(self, next_state, 1, 1)
            if v > vmax:
                vmax = v
                valid_actions = [action]
            elif v == vmax:
                valid_actions.append(action)
                continue
        return valid_actions[random.randint(0,len(valid_actions)-1)]
