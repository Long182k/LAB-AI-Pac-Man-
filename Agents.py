from game import Agent
from game import Directions
import random

# class DumbAgent(Agent):
#     #  "An agent that goes East until it can't"
#     def getAction(self, state):
#     #  "The agent always goes East"
#         return Directions.EAST

class DumbAgent(Agent):
#  "An agent that goes East until it can't."
    def getAction(self, state):
#  "The agent receives a GameState (defined in pacman.py)."
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP


class RandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        availableActions = state.getLegalPacmanActions()
        action = random.choice(availableActions)
        return action

class BetterRandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition())
        availableActions = state.getLegalPacmanActions()
        availableActions = availableActions[:-1] 
        print("Actions available: ",availableActions)
        action = random.choice(availableActions)
        return action

# class ReflexAgent(Agent):
#  def getAction(self, state):
#         print("Location: ", state.getPacmanPosition())
#         availableActions = state.getLegalPacmanActions()
#         availableActions = availableActions[:-1] 

#         print("Actions available: ",availableActions)
#         currentFood = state.getNumFood()
#         print("The number of current food:",currentFood)
#         for action in availableActions:
#             nextState = state.generatePacmanSuccessor(action)
#             print("The number of Pacman Successor:",nextState)
#             nextFood = [] 
#             nextFood= next(state.getNumFood())
#             # nextFood = next(currentFood)
            
#             if nextFood < currentFood:
#                 return action
#             else:
#                 action = random.choice(availableActions)
#                 return action
